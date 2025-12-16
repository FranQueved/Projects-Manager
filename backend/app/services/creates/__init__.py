"""
Paso intermedio entre los servicios y las operaciones CRUD.(Schema y modelos)
Aquí defines clases que facilitan la creación de entidades en bloque (create_employee.py, create_project.py, etc.)
Estas clases validan los JSONs de entrada, los convierten en modelos SQLAlchemy y los guardan en la base de datos.

"""

from app.services.creates.create_employee import EmployeeCreator
from app.services.creates.create_profile import ProfileCreator  
from app.services.creates.create_proyect import ProjectCreator

__all__ = [
    "EmployeeCreator",
    "ProfileCreator",
    "ProjectCreator",
]