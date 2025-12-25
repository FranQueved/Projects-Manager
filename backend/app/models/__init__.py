"""
Modelos ORM de SQLAlchemy.

Define la estructura de todas las tablas de la base de datos.
"""

# Importar todos los modelos ORM para que SQLAlchemy los registre
from app.models.employee import Employee
from app.models.profile import Profile
from app.models.project import Project
from app.models.required_profile import RequiredProfile
from app.models.embedding import Embedding
from app.models.employee_project import employee_project

__all__ = [
    "Employee",
    "Profile",
    "Project",
    "RequiredProfile",
    "Embedding",
    "employee_project",
]