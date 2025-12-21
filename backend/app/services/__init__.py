"""
Inicialización del paquete `app.services`.

Estructura actual:
- examples/: datos de ejemplo para pruebas y desarrollo
- creates/: helpers para crear entidades en bloque (create_employee.py, ...)
- service_layer/: servicios CRUD principales

Se exportan clases y datos más usados para permitir imports rápidos:
`from app.services import ProjectService, EmployeeCreator, PROFILES_DATA`, etc.
"""

from app.services.service_layer.project_service import ProjectService
from app.services.service_layer.employee_service import EmployeeService
from app.services.service_layer.profile_service import ProfileService
from app.services.service_layer.employee_project_service import EmployeeProjectService
from app.services.service_layer.required_profile_service import RequiredProfileService

from app.services.creates.create_employee import EmployeeCreator
from app.services.creates.create_profile import ProfileCreator
from app.services.creates.create_proyect import ProjectCreator


__all__ = [
    "ProjectService",
    "EmployeeService",
    "ProfileService",
    "EmployeeProjectService",
    "RequiredProfileService",
    "EmployeeCreator",
    "ProfileCreator",
    "ProjectCreator",
]
