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

    def add_required_profile(self, project_id: int, profile_id: int):
        """Agrega un perfil requerido a un proyecto"""
        try:
            # Verificar que no exista ya
            existing = self.db.query(RequiredProfile).filter(
                RequiredProfile.project_id == project_id,
                RequiredProfile.profile_id == profile_id
            ).first()
            
            if existing:
                return False  # Ya existe
            
            required = RequiredProfile(
                project_id=project_id,
                profile_id=profile_id
            )
            self.db.add(required)
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(f"Error agregando perfil requerido: {e}")
            return False

    def remove_required_profile(self, project_id: int, profile_id: int):
        """Elimina un perfil requerido de un proyecto"""
        try:
            self.db.query(RequiredProfile).filter(
                RequiredProfile.project_id == project_id,
                RequiredProfile.profile_id == profile_id
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

    def get_projects_requiring_profile(self, profile_id: int):
        """Obtiene todos los proyectos que requieren un perfil específico"""
        try:
            return self.db.query(RequiredProfile).filter(
                RequiredProfile.profile_id == profile_id
            ).all()
        except Exception as e:
            print(f"Error obteniendo proyectos: {e}")
            return []

    def verify_employee_matches_project(self, employee_id: int, project_id: int):
        """
        Verifica si el perfil del empleado es uno de los requeridos para el proyecto.
        Si no hay perfiles requeridos, retorna True (cualquiera puede trabajar).
        """
        try:
            from app.services.service_layer.employee_service import EmployeeService
            
            emp_service = EmployeeService()
            employee = emp_service.get_with_profile(employee_id)
            
            if not employee or not employee.profile:
                return False
            
            required_profiles = self.get_required_profiles_for_project(project_id)
            
            # Si no hay perfiles requeridos, cualquiera puede trabajar
            if not required_profiles:
                return True
            
            # Verificar si el perfil del empleado está en los requeridos
            for rp in required_profiles:
                if rp.profile_id == employee.profile_id:
                    return True
            
            return False
        except Exception as e:
            print(f"Error verificando compatibilidad: {e}")
            return False

    def close(self):
        """Cierra la sesión de la base de datos"""
        self.db.close()
