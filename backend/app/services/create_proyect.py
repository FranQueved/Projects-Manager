# app/utils/project_creator.py

from app.schemas.project import ProjectCreate
from app.models.project import Project
from app.db.database import SessionLocal

class ProjectCreator:
    """
    Clase que permite crear uno o varios proyectos a partir de JSONs.
    """

    def __init__(self):
        self.db = SessionLocal()

    def create_one(self, json_data: dict) -> Project:
        """
        Crea un único proyecto a partir de un JSON.
        """
        # 1. Validar JSON → Schema
        schema = ProjectCreate(**json_data)

        # 2. Schema → Modelo SQLAlchemy
        project = Project(**schema.dict())

        # 3. Guardar en BD
        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)

        return project

    def create_many(self, json_list: list[dict]) -> list[Project]:
        """
        Crea múltiples proyectos a partir de una lista de JSONs.
        """
        created_projects = []

        for json_data in json_list:
            # 1. Validar JSON → Schema
            schema = ProjectCreate(**json_data)

            # 2. Schema → Modelo SQLAlchemy
            project = Project(**schema.dict())

            # 3. Añadir a la sesión
            self.db.add(project)
            created_projects.append(project)

        # Commit único para optimizar rendimiento
        self.db.commit()

        # Refrescar para obtener IDs
        for project in created_projects:
            self.db.refresh(project)

        return created_projects

    def close(self):
        """Cierra la sesión de base de datos."""
        self.db.close()
