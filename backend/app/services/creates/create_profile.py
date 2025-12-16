# app/services/create_profile.py

from app.schemas.profile import ProfileCreate
from app.models.profile import Profile
from app.db.database import SessionLocal

class ProfileCreator:
    """
    Clase que permite crear uno o varios perfiles a partir de JSONs.
    """

    def __init__(self):
        self.db = SessionLocal()

    def create_one(self, json_data: dict) -> Profile:
        """
        Crea un único perfil a partir de un JSON.
        """
        # 1. Validar JSON → Schema
        schema = ProfileCreate(**json_data)

        # 2. Schema → Modelo SQLAlchemy
        profile = Profile(**schema.dict())

        # 3. Guardar en BD
        self.db.add(profile)
        self.db.commit()
        self.db.refresh(profile)

        return profile

    def create_many(self, json_list: list[dict]) -> list[Profile]:
        """
        Crea múltiples perfiles a partir de una lista de JSONs.
        """
        created_profiles = []

        for json_data in json_list:
            # 1. Validar JSON → Schema
            schema = ProfileCreate(**json_data)

            # 2. Schema → Modelo SQLAlchemy
            profile = Profile(**schema.dict())

            # 3. Añadir a la sesión
            self.db.add(profile)
            created_profiles.append(profile)

        # Commit único para optimizar rendimiento
        self.db.commit()

        # Refrescar para obtener IDs
        for profile in created_profiles:
            self.db.refresh(profile)

        return created_profiles

    def close(self):
        """Cierra la sesión de base de datos."""
        self.db.close()