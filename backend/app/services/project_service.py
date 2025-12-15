# app/services/project_service.py

from typing import List, Optional
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.project import ProjectCreate, ProjectRead
from app.models.project import Project

class ProjectService:
    """
    Servicio completo para operaciones CRUD de proyectos.
    """

    def __init__(self):
        self.db: Session = SessionLocal()

    # CREATE
    def create_one(self, json_data: dict) -> Project:
        """Crea un único proyecto."""
        schema = ProjectCreate(**json_data)
        project = Project(**schema.dict())
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)
        return project

    def create_many(self, json_list: List[dict]) -> List[Project]:
        """Crea múltiples proyectos."""
        created_projects = []
        for json_data in json_list:
            schema = ProjectCreate(**json_data)
            project = Project(**schema.dict())
            self.db.add(project)
            created_projects.append(project)
        self.db.commit()
        for project in created_projects:
            self.db.refresh(project)
        return created_projects

    # READ
    def get_by_id(self, project_id: int) -> Optional[Project]:
        """Obtiene un proyecto por ID."""
        return self.db.query(Project).filter(Project.id == project_id).first()

    def get_all(self) -> List[Project]:
        """Obtiene todos los proyectos."""
        return self.db.query(Project).all()

    def get_by_client(self, client: str) -> List[Project]:
        """Obtiene proyectos por cliente."""
        return self.db.query(Project).filter(Project.client == client).all()

    def get_finished(self) -> List[Project]:
        """Obtiene proyectos terminados."""
        return self.db.query(Project).filter(Project.finished == True).all()

    def get_active(self) -> List[Project]:
        """Obtiene proyectos activos."""
        return self.db.query(Project).filter(Project.finished == False).all()

    # UPDATE
    def update_by_id(self, project_id: int, json_data: dict) -> Optional[Project]:
        """Actualiza un proyecto por ID."""
        project = self.get_by_id(project_id)
        if not project:
            return None

        schema = ProjectUpdate(**json_data)
        update_data = schema.dict(exclude_unset=True)

        for field, value in update_data.items():
            setattr(project, field, value)

        self.db.commit()
        self.db.refresh(project)
        return project

    # DELETE
    def delete_by_id(self, project_id: int) -> bool:
        """Elimina un proyecto por ID."""
        project = self.get_by_id(project_id)
        if not project:
            return False

        self.db.delete(project)
        self.db.commit()
        return True

    def delete_many(self, project_ids: List[int]) -> int:
        """Elimina múltiples proyectos por IDs. Retorna cantidad eliminada."""
        deleted_count = self.db.query(Project).filter(Project.id.in_(project_ids)).delete()
        self.db.commit()
        return deleted_count

    def close(self):
        """Cierra la sesión de base de datos."""
        self.db.close()