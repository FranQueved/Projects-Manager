# app/services/profile_service.py

from typing import List, Optional
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.profile import ProfileCreate, ProfileUpdate, ProfileRead
from app.models.profile import Profile

class ProfileService:
    """
    Servicio completo para operaciones CRUD de perfiles.
    """

    def __init__(self):
        self.db: Session = SessionLocal()

    # CREATE
    def create_one(self, json_data: dict) -> Profile:
        """Crea un único perfil."""
        schema = ProfileCreate(**json_data)
        profile = Profile(**schema.dict())
        self.db.add(profile)
        self.db.commit()
        self.db.refresh(profile)
        return profile

    def create_many(self, json_list: List[dict]) -> List[Profile]:
        """Crea múltiples perfiles."""
        created_profiles = []
        for json_data in json_list:
            schema = ProfileCreate(**json_data)
            profile = Profile(**schema.dict())
            self.db.add(profile)
            created_profiles.append(profile)
        self.db.commit()
        for profile in created_profiles:
            self.db.refresh(profile)
        return created_profiles

    # READ
    def get_by_id(self, profile_id: int) -> Optional[Profile]:
        """Obtiene un perfil por ID."""
        return self.db.query(Profile).filter(Profile.id == profile_id).first()

    def get_all(self) -> List[Profile]:
        """Obtiene todos los perfiles."""
        return self.db.query(Profile).all()

    def get_by_skill(self, skill: str) -> List[Profile]:
        """Obtiene perfiles que contienen una habilidad específica."""
        return self.db.query(Profile).filter(Profile.hardSkills.ilike(f"%{skill}%")).all()

    def get_by_language(self, language: str) -> List[Profile]:
        """Obtiene perfiles que contienen un idioma específico."""
        return self.db.query(Profile).filter(Profile.languages.ilike(f"%{language}%")).all()

    # UPDATE
    def update_by_id(self, profile_id: int, json_data: dict) -> Optional[Profile]:
        """Actualiza un perfil por ID."""
        profile = self.get_by_id(profile_id)
        if not profile:
            return None

        schema = ProfileUpdate(**json_data)
        update_data = schema.dict(exclude_unset=True)

        for field, value in update_data.items():
            setattr(profile, field, value)

        self.db.commit()
        self.db.refresh(profile)
        return profile

    # DELETE
    def delete_by_id(self, profile_id: int) -> bool:
        """Elimina un perfil por ID."""
        profile = self.get_by_id(profile_id)
        if not profile:
            return False

        self.db.delete(profile)
        self.db.commit()
        return True

    def delete_many(self, profile_ids: List[int]) -> int:
        """Elimina múltiples perfiles por IDs. Retorna cantidad eliminada."""
        deleted_count = self.db.query(Profile).filter(Profile.id.in_(profile_ids)).delete()
        self.db.commit()
        return deleted_count

    def close(self):
        """Cierra la sesión de base de datos."""
        self.db.close()