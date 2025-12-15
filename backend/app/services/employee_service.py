# app/services/employee_service.py

from typing import List, Optional
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeRead
from app.models.epmloyees import Employee
from app.models.profile import Profile

class EmployeeService:
    """
    Servicio completo para operaciones CRUD de empleados.
    """

    def __init__(self):
        self.db: Session = SessionLocal()

    # CREATE
    def create_one(self, json_data: dict) -> Employee:
        """Crea un único empleado."""
        schema = EmployeeCreate(**json_data)
        employee = Employee(**schema.dict())
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)
        return employee

    def create_many(self, json_list: List[dict]) -> List[Employee]:
        """Crea múltiples empleados."""
        created_employees = []
        for json_data in json_list:
            schema = EmployeeCreate(**json_data)
            employee = Employee(**schema.dict())
            self.db.add(employee)
            created_employees.append(employee)
        self.db.commit()
        for employee in created_employees:
            self.db.refresh(employee)
        return created_employees

    # READ
    def get_by_id(self, employee_id: int) -> Optional[Employee]:
        """Obtiene un empleado por ID."""
        return self.db.query(Employee).filter(Employee.id == employee_id).first()

    def get_all(self) -> List[Employee]:
        """Obtiene todos los empleados."""
        return self.db.query(Employee).all()

    def get_by_office(self, office: str) -> List[Employee]:
        """Obtiene empleados por oficina."""
        return self.db.query(Employee).filter(Employee.office == office).all()

    def get_by_name(self, name: str) -> List[Employee]:
        """Obtiene empleados por nombre (búsqueda parcial)."""
        return self.db.query(Employee).filter(Employee.name.ilike(f"%{name}%")).all()

    def get_with_profile(self, employee_id: int) -> Optional[Employee]:
        """Obtiene un empleado con su perfil cargado."""
        return self.db.query(Employee).filter(Employee.id == employee_id).first()

    # UPDATE
    def update_by_id(self, employee_id: int, json_data: dict) -> Optional[Employee]:
        """Actualiza un empleado por ID."""
        employee = self.get_by_id(employee_id)
        if not employee:
            return None

        schema = EmployeeUpdate(**json_data)
        update_data = schema.dict(exclude_unset=True)

        for field, value in update_data.items():
            setattr(employee, field, value)

        self.db.commit()
        self.db.refresh(employee)
        return employee

    # DELETE
    def delete_by_id(self, employee_id: int) -> bool:
        """Elimina un empleado por ID."""
        employee = self.get_by_id(employee_id)
        if not employee:
            return False

        self.db.delete(employee)
        self.db.commit()
        return True

    def delete_many(self, employee_ids: List[int]) -> int:
        """Elimina múltiples empleados por IDs. Retorna cantidad eliminada."""
        deleted_count = self.db.query(Employee).filter(Employee.id.in_(employee_ids)).delete()
        self.db.commit()
        return deleted_count

    def assign_profile_to_employee(self, employee_id: int, profile_id: int) -> bool:
        """Asigna un perfil a un empleado (relación 1 a 1)."""
        employee = self.get_by_id(employee_id)
        if not employee:
            return False

        profile = self.db.query(Profile).filter(Profile.id == profile_id).first()
        if not profile:
            return False

        employee.profile_id = profile_id
        self.db.commit()
        return True

    def close(self):
        """Cierra la sesión de base de datos."""
        self.db.close()