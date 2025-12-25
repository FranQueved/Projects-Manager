"""Profile service - CRUD operations for professional profiles."""

from typing import List, Optional
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.profile import ProfileCreate, ProfileUpdate
from app.models.profile import Profile



class ProfileService:
    """Profile CRUD service."""

    def __init__(self):
        self.db: Session = SessionLocal()

    def create_one(self, data: dict) -> Profile:
        """Create single profile and generate embedding."""
        schema = ProfileCreate(**data)
        profile = Profile(**schema.dict())
        self.db.add(profile)
        self.db.commit()
        self.db.refresh(profile)
        return profile

    def create_many(self, data_list: List[dict]) -> List[Profile]:
        """Create multiple profiles and generate embeddings."""
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

    def get_by_id(self, profile_id: int) -> Optional[Profile]:
        """Get profile by ID."""
        return self.db.query(Profile).filter(Profile.id == profile_id).first()

    def get_all(self) -> List[Profile]:
        """Get all profiles."""
        return self.db.query(Profile).order_by(Profile.id).all()

    def get_by_skill(self, skill: str) -> List[Profile]:
        """Get profiles containing specific skill."""
        return self.db.query(Profile).filter(Profile.hard_skills.ilike(f"%{skill}%")).all()

    def get_by_language(self, language: str) -> List[Profile]:
        """Get profiles with specific language."""
        return self.db.query(Profile).filter(Profile.languages.ilike(f"%{language}%")).all()

    def toString(self, profile_id: int) -> Optional[str]:
        """Convert profile to formatted string for embedding."""
        profile = self.get_by_id(profile_id)
        if profile:
            parts = []
            if profile.hard_skills:
                parts.append(profile.hard_skills.replace(",", " ").replace("-", " "))
            if profile.soft_skills:
                parts.append(profile.soft_skills.replace(",", " ").replace("-", " "))
            if profile.languages:
                parts.append(profile.languages.replace(",", " ").replace("-", " "))
            result = " ".join(parts)
            return " ".join(result.split())
        return None

    def update(self, profile_id: int, data: dict) -> Optional[Profile]:
        """Update profile."""
        profile = self.get_by_id(profile_id)
        if profile:
            schema = ProfileUpdate(**data)
            for key, value in schema.dict(exclude_unset=True).items():
                setattr(profile, key, value)
            self.db.commit()
            self.db.refresh(profile)
        return profile

    def delete(self, profile_id: int) -> bool:
        """Delete profile."""
        profile = self.get_by_id(profile_id)
        if profile:
            self.db.delete(profile)
            self.db.commit()
            return True
        return False

    def close(self):
        """Close database session."""
        self.db.close()
