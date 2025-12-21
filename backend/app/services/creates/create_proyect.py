"""Project creation service - Create project records."""

from typing import List
from app.schemas.project import ProjectCreate
from app.models.project import Project
from app.db.database import SessionLocal


class ProjectCreator:
    """Service for creating projects."""

    def __init__(self):
        self.db = SessionLocal()

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

    def close(self):
        """Close database session."""
        self.db.close()
