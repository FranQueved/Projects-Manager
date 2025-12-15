# app/services/employee_project_service.py

from typing import List, Optional
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.epmloyees import Employee
from app.models.project import Project
from app.models.employee_project import employee_project

class EmployeeProjectService:
    """
    Servicio para manejar las relaciones entre empleados y proyectos.
    """

    def __init__(self):
        self.db: Session = SessionLocal()

    def assign_employee_to_project(self, employee_id: int, project_id: int) -> bool:
        """Asigna un empleado a un proyecto."""
        # Verificar que existen
        employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        project = self.db.query(Project).filter(Project.id == project_id).first()

        if not employee or not project:
            return False

        # Verificar que no esté ya asignado
        existing = self.db.execute(
            employee_project.select().where(
                employee_project.c.employee_id == employee_id,
                employee_project.c.project_id == project_id
            )
        ).first()

        if existing:
            return False  # Ya está asignado

        # Asignar
        self.db.execute(
            employee_project.insert().values(
                employee_id=employee_id,
                project_id=project_id
            )
        )
        self.db.commit()
        return True

    def remove_employee_from_project(self, employee_id: int, project_id: int) -> bool:
        """Remueve un empleado de un proyecto."""
        result = self.db.execute(
            employee_project.delete().where(
                employee_project.c.employee_id == employee_id,
                employee_project.c.project_id == project_id
            )
        )
        self.db.commit()
        return result.rowcount > 0

    def get_employees_by_project(self, project_id: int) -> List[Employee]:
        """Obtiene todos los empleados asignados a un proyecto."""
        project = self.db.query(Project).filter(Project.id == project_id).first()
        if not project:
            return []
        return project.employees

    def get_projects_by_employee(self, employee_id: int) -> List[Project]:
        """Obtiene todos los proyectos asignados a un empleado."""
        employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        if not employee:
            return []
        return employee.projects

    def assign_multiple_employees_to_project(self, employee_ids: List[int], project_id: int) -> int:
        """Asigna múltiples empleados a un proyecto. Retorna cantidad asignada."""
        # Verificar que el proyecto existe
        project = self.db.query(Project).filter(Project.id == project_id).first()
        if not project:
            return 0

        assigned_count = 0
        for employee_id in employee_ids:
            if self.assign_employee_to_project(employee_id, project_id):
                assigned_count += 1

        return assigned_count

    def remove_all_employees_from_project(self, project_id: int) -> int:
        """Remueve todos los empleados de un proyecto. Retorna cantidad removida."""
        result = self.db.execute(
            employee_project.delete().where(
                employee_project.c.project_id == project_id
            )
        )
        self.db.commit()
        return result.rowcount

    def remove_employee_from_all_projects(self, employee_id: int) -> int:
        """Remueve un empleado de todos sus proyectos. Retorna cantidad removida."""
        result = self.db.execute(
            employee_project.delete().where(
                employee_project.c.employee_id == employee_id
            )
        )
        self.db.commit()
        return result.rowcount

    def get_project_assignments(self) -> List[dict]:
        """Obtiene todas las asignaciones empleado-proyecto."""
        result = self.db.execute(
            employee_project.select()
        ).fetchall()

        return [
            {"employee_id": row.employee_id, "project_id": row.project_id}
            for row in result
        ]

    def close(self):
        """Cierra la sesión de base de datos."""
        self.db.close()