"""
Employee-Project assignment routes.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.employee import Employee
from app.models.project import Project

router = APIRouter(prefix="/assignments", tags=["assignments"])


@router.post("/assign/{employee_id}/{project_id}")
def assign_employee_to_project(
    employee_id: int,
    project_id: int,
    db: Session = Depends(get_db)
):
    """Assign an employee to a project."""
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if employee not in project.employees:
        project.employees.append(employee)
        db.commit()

    return {"message": f"Employee {employee_id} assigned to project {project_id}"}


@router.delete("/unassign/{employee_id}/{project_id}")
def unassign_employee_from_project(
    employee_id: int,
    project_id: int,
    db: Session = Depends(get_db)
):
    """Remove an employee from a project."""
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if employee in project.employees:
        project.employees.remove(employee)
        db.commit()

    return {"message": f"Employee {employee_id} removed from project {project_id}"}


@router.get("/project/{project_id}")
def get_project_employees(project_id: int, db: Session = Depends(get_db)):
    """Get all employees assigned to a project."""
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return {"project_id": project_id, "employees": project.employees}


@router.get("/employee/{employee_id}")
def get_employee_projects(employee_id: int, db: Session = Depends(get_db)):
    """Get all projects assigned to an employee."""
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"employee_id": employee_id, "projects": employee.projects}
