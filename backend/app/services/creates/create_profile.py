"""Profile creation service - Create professional profiles."""

from typing import List
from app.schemas.profile import ProfileCreate
from app.models.profile import Profile
from app.db.database import SessionLocal


class ProfileCreator:
    """Service for creating professional profiles."""

    def __init__(self):
        self.db = SessionLocal()

    def create_one(self, data: dict) -> Profile:
        """Create single profile."""
        schema = ProfileCreate(**data)
        profile = Profile(**schema.dict())
        self.db.add(profile)
        self.db.commit()
        self.db.refresh(profile)
        return profile

    def create_many(self, data_list: List[dict]) -> List[Profile]:
        """Create multiple profiles."""
        created = []
        for data in data_list:
            schema = ProfileCreate(**data)
            profile = Profile(**schema.dict())
            self.db.add(profile)
            created.append(profile)

        self.db.commit()
        for profile in created:
            self.db.refresh(profile)

        return created

    def close(self):
        """Close database session."""
        self.db.close()

        # Refrescar para obtener IDs
        for profile in created_profiles:
            self.db.refresh(profile)

        return created_profiles

    def close(self):
        """Cierra la sesión de base de datos."""
        self.db.close()