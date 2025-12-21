"""Required Profile service - Manage required skills for projects."""

from typing import List, Optional
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.required_profile import RequiredProfile
from app.services.vectorial_services.embedding_service import EmbeddingService


class RequiredProfileService:
    """Service for managing required profiles by projects."""

    def __init__(self):
        self.db: Session = SessionLocal()
        self.embedding_service = EmbeddingService()

    def add_required_profile(self, project_id: int, hard_skills: str, soft_skills: str, languages: str) -> Optional[RequiredProfile]:
        """Add required profile to project and generate embedding."""
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
            
            self.embedding_service.create_embedding_for_required_profile(required.id)
            
            return required
        except Exception as e:
            self.db.rollback()
            print(f"Error adding required profile: {e}")
            return None

    def remove_required_profile(self, required_profile_id: int) -> bool:
        """Remove required profile by ID."""
        try:
            self.db.query(RequiredProfile).filter(
                RequiredProfile.id == required_profile_id
            ).delete()
            self.db.commit()
            return True
        except Exception as e:
            self.db.rollback()
            print(f"Error removing required profile: {e}")
            return False

    def get_required_profiles_for_project(self, project_id: int) -> List[RequiredProfile]:
        """Get all required profiles for project."""
        try:
            return self.db.query(RequiredProfile).filter(
                RequiredProfile.project_id == project_id
            ).all()
        except Exception as e:
            print(f"Error getting required profiles: {e}")
            return []

    def get_all(self) -> List[RequiredProfile]:
        """Get all required profiles."""
        try:
            return self.db.query(RequiredProfile).all()
        except Exception as e:
            print(f"Error getting all required profiles: {e}")
            return []

    def close(self):
        """Close database session and embedding service."""
        self.db.close()
        self.embedding_service.close()
