"""Employee-Project service - Manage relationships between employees and projects."""

from typing import List
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.employee import Employee
from app.models.project import Project
from app.models.employee_project import employee_project


class EmployeeProjectService:
    """Service for employee-project relationships."""

    def __init__(self):
        self.db: Session = SessionLocal()

    def assign_employee_to_project(self, employee_id: int, project_id: int) -> bool:
        """Assign employee to project."""
        employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        project = self.db.query(Project).filter(Project.id == project_id).first()

        if not employee or not project:
            return False

        existing = self.db.execute(
            employee_project.select().where(
                employee_project.c.employee_id == employee_id,
                employee_project.c.project_id == project_id
            )
        ).first()

        if existing:
            return False

        self.db.execute(
            employee_project.insert().values(
                employee_id=employee_id,
                project_id=project_id
            )
        )
        self.db.commit()
        return True

    def remove_employee_from_project(self, employee_id: int, project_id: int) -> bool:
        """Remove employee from project."""
        result = self.db.execute(
            employee_project.delete().where(
                employee_project.c.employee_id == employee_id,
                employee_project.c.project_id == project_id
            )
        )
        self.db.commit()
        return result.rowcount > 0

    def get_employees_by_project(self, project_id: int) -> List[Employee]:
        """Get all employees assigned to project."""
        project = self.db.query(Project).filter(Project.id == project_id).first()
        if not project:
            return []
        return project.employees

    def get_projects_by_employee(self, employee_id: int) -> List[Project]:
        """Get all projects assigned to employee."""
        employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
        if not employee:
            return []
        return employee.projects

    def assign_multiple_employees_to_project(self, employee_ids: List[int], project_id: int) -> int:
        """Assign multiple employees to project. Returns count assigned."""
        project = self.db.query(Project).filter(Project.id == project_id).first()
        if not project:
            return 0

        assigned_count = 0
        for employee_id in employee_ids:
            if self.assign_employee_to_project(employee_id, project_id):
                assigned_count += 1

        return assigned_count

    def remove_all_employees_from_project(self, project_id: int) -> int:
        """Remove all employees from project. Returns count removed."""
        result = self.db.execute(
            employee_project.delete().where(
                employee_project.c.project_id == project_id
            )
        )
        self.db.commit()
        return result.rowcount

    def remove_employee_from_all_projects(self, employee_id: int) -> int:
        """Remove employee from all projects. Returns count removed."""
        result = self.db.execute(
            employee_project.delete().where(
                employee_project.c.employee_id == employee_id
            )
        )
        self.db.commit()
        return result.rowcount

    def close(self):
        """Close database session."""
        self.db.close()
