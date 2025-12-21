# app/services/create_employee.py

from app.schemas.employee import EmployeeCreate
from app.models.employee import Employee
from app.models.profile import Profile
from app.db.database import SessionLocal

class EmployeeCreator:
    """
    Clase que permite crear uno o varios empleados a partir de JSONs.
    """

    def __init__(self):
        self.db = SessionLocal()

    def create_one(self, json_data: dict) -> Employee:
        """
        Crea un único empleado a partir de un JSON.
        """
        # 1. Validar JSON → Schema
        schema = EmployeeCreate(**json_data)

        # 2. Schema → Modelo SQLAlchemy
        # Validar que el perfil exista y no esté asignado
        profile = self.db.query(Profile).filter(Profile.id == schema.profile_id).first()
        if not profile:
            raise ValueError(f"Perfil {schema.profile_id} no existe")

        existing = self.db.query(Employee).filter(Employee.profile_id == schema.profile_id).first()
        if existing:
            raise ValueError(f"Perfil {schema.profile_id} ya está asignado al empleado {existing.id}")

        employee = Employee(**schema.dict())

        # 3. Guardar en BD
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)

        return employee

    def create_many(self, json_list: list[dict]) -> list[Employee]:
        """
        Crea múltiples empleados a partir de una lista de JSONs.
        """
        created_employees = []

        for json_data in json_list:
            # 1. Validar JSON → Schema
            schema = EmployeeCreate(**json_data)

            # 2. Schema → Modelo SQLAlchemy
            profile = self.db.query(Profile).filter(Profile.id == schema.profile_id).first()
            if not profile:
                raise ValueError(f"Perfil {schema.profile_id} no existe")

            existing = self.db.query(Employee).filter(Employee.profile_id == schema.profile_id).first()
            if existing:
                raise ValueError(f"Perfil {schema.profile_id} ya está asignado al empleado {existing.id}")

            employee = Employee(**schema.dict())

            # 3. Añadir a la sesión
            self.db.add(employee)
            created_employees.append(employee)

        # Commit único para optimizar rendimiento
        self.db.commit()

        # Refrescar para obtener IDs
        for employee in created_employees:
            self.db.refresh(employee)

        return created_employees

    def close(self):
        """Cierra la sesión de base de datos."""
        self.db.close()