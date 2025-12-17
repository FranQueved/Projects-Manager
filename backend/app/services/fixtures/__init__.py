"""
Fixtures - Datos ficticios y scripts de seeding para la base de datos

Este módulo contiene toda la lógica para poblar la base de datos con:
- Datos de prueba (perfiles, empleados, proyectos, asignaciones)
- Scripts de seeding automatizados
- Embeddings de perfiles profesionales
"""

from .seed_data import PROFILES_DATA, EMPLOYEES_DATA, PROJECTS_DATA, ASSIGNMENTS_DATA
from .seed_service import SeedService
from .populate_embeddings import populate_embeddings

__all__ = [
    "PROFILES_DATA",
    "EMPLOYEES_DATA",
    "PROJECTS_DATA",
    "ASSIGNMENTS_DATA",
    "SeedService",
    "populate_embeddings",
]
