"""Project service - CRUD operations for projects."""

from typing import List, Optional
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.project import ProjectCreate, ProjectUpdate
from app.models.project import Project


class ProjectService:
    """Project CRUD service."""

    def __init__(self):
        self.db: Session = SessionLocal()

    def create_one(self, data: dict) -> Project:
        """Create single project."""
        schema = ProjectCreate(**data)
        project = Project(**schema.dict())
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def create_many(self, data_list: List[dict]) -> List[Project]:
        """Create multiple projects."""
        created = []
        for data in data_list:
            schema = ProjectCreate(**data)
            project = Project(**schema.dict())
            self.db.add(project)
            created.append(project)
        self.db.commit()
        for project in created:
            self.db.refresh(project)
        return created

    def get_by_id(self, project_id: int) -> Optional[Project]:
        """Get project by ID."""
        return self.db.query(Project).filter(Project.id == project_id).first()

    def get_all(self) -> List[Project]:
        """Get all projects."""
        return self.db.query(Project).all()

    def get_by_client(self, client: str) -> List[Project]:
        """Get projects by client."""
        return self.db.query(Project).filter(Project.client == client).all()

    def get_finished(self) -> List[Project]:
        """Get finished projects."""
        return self.db.query(Project).filter(Project.finished == True).all()

    def get_active(self) -> List[Project]:
        """Get active projects."""
        return self.db.query(Project).filter(Project.finished == False).all()

    def update_by_id(self, project_id: int, data: dict) -> Optional[Project]:
        """Update project."""
        project = self.get_by_id(project_id)
        if not project:
            return None

        schema = ProjectUpdate(**data)
        update_data = schema.dict(exclude_unset=True)

        for field, value in update_data.items():
            setattr(project, field, value)

        self.db.commit()
        self.db.refresh(project)
        return project

    def delete_by_id(self, project_id: int) -> bool:
        """Delete project."""
        project = self.get_by_id(project_id)
        if not project:
            return False

        self.db.delete(project)
        self.db.commit()
        return True

    def delete_many(self, project_ids: List[int]) -> int:
        """Delete multiple projects. Returns count deleted."""
        deleted_count = self.db.query(Project).filter(Project.id.in_(project_ids)).delete()
        self.db.commit()
        return deleted_count

    def close(self):
        """Close database session."""
        self.db.close()
