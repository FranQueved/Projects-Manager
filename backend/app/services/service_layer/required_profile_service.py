"""
Servicio para gestionar perfiles requeridos por proyectos
"""

from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.required_profile import RequiredProfile


class RequiredProfileService:
    """Servicio para gestionar la relación entre proyectos y perfiles requeridos"""

    def __init__(self):
        self.db = SessionLocal()

    def add_required_profile(self, project_id: int, hard_skills: str, soft_skills: str, languages: str):
        """Agrega un perfil requerido a un proyecto"""
        try:
            required = RequiredProfile(
                project_id=project_id,
                hard_skills=hard_skills,
                soft_skills=soft_skills,
                languages=languages
            )
            self.db.add(required)
            self.db.commit()
            self.db.refresh(required)
            return required
        except Exception as e:
            self.db.rollback()
            print(f"Error agregando perfil requerido: {e}")
            return None

    def remove_required_profile(self, required_profile_id: int):
        """Elimina un perfil requerido por su ID"""
        try:
            self.db.query(RequiredProfile).filter(
                RequiredProfile.id == required_profile_id
            ).delete()
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(f"Error eliminando perfil requerido: {e}")
            return False

    def get_required_profiles_for_project(self, project_id: int):
        """Obtiene todos los perfiles requeridos para un proyecto"""
        try:
            return self.db.query(RequiredProfile).filter(
                RequiredProfile.project_id == project_id
            ).all()
        except Exception as e:
            print(f"Error obteniendo perfiles requeridos: {e}")
            return []


    def get_all(self):
        """Obtiene todos los perfiles requeridos"""
        try:
            return self.db.query(RequiredProfile).all()
        except Exception as e:
            print(f"Error obteniendo todos los perfiles requeridos: {e}")
            return []

    def close(self):
        """Cierra la sesión de la base de datos"""
        self.db.close()
