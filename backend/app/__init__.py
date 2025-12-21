# 
# MÓDULO BACKEND/APP/__INIT__.PY
# ================================
# 
# Este archivo hace que la carpeta 'app' sea un paquete de Python.
# Exporta los módulos principales para imports simplificados.
# 

from app.db import SessionLocal, engine
from app.db.create_tables import InitDB
from app.services import (
    ProjectService,
    EmployeeService,
    ProfileService,
    RequiredProfileService,
    EmployeeProjectService,
    EmployeeCreator,
    ProfileCreator,
    ProjectCreator,
)

__all__ = [
    'SessionLocal',
    'engine',
    'InitDB',
    'ProjectService',
    'EmployeeService',
    'ProfileService',
    'RequiredProfileService',
    'EmployeeProjectService',
    'EmployeeCreator',
    'ProfileCreator',
    'ProjectCreator',
]
