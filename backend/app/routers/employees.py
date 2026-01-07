"""
Employee routes - CRUD operations for employees.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.employee import Employee
from app.models.profile import Profile
from app.schemas.employee import EmployeeCreate, EmployeeRead, EmployeeUpdate

router = APIRouter(prefix="/employees", tags=["employees"])


def format_employee_response(employee: Employee) -> dict:
    """Format employee response with profile data."""
    return {
        "id": employee.id,
        "name": employee.name,
        "office": employee.office,
        "profile_id": employee.profile_id,
        "hard_skills": employee.profile.hard_skills if employee.profile else "",
        "soft_skills": employee.profile.soft_skills if employee.profile else "",
        "languages": employee.profile.languages if employee.profile else "",
    }


@router.get("/", response_model=list[EmployeeRead])
def list_employees(db: Session = Depends(get_db)):
    """List all employees."""
    employees = db.query(Employee).all()
    return [format_employee_response(emp) for emp in employees]


@router.get("/{employee_id}", response_model=EmployeeRead)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    """Get a specific employee by ID."""
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return format_employee_response(employee)


@router.post("/", response_model=EmployeeRead)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    """Create a new employee with optional profile."""
    # Create profile if skills provided
    profile = None
    if employee.hard_skills or employee.soft_skills or employee.languages:
        profile = Profile(
            hard_skills=employee.hard_skills or "",
            soft_skills=employee.soft_skills or "",
            languages=employee.languages or ""
        )
        db.add(profile)
        db.flush()
    else:
        # Create empty profile
        profile = Profile(
            hard_skills="",
            soft_skills="",
            languages=""
        )
        db.add(profile)
        db.flush()

    # Create employee with profile
    db_employee = Employee(
        name=employee.name,
        office=employee.office,
        profile_id=profile.id
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return format_employee_response(db_employee)


@router.put("/{employee_id}", response_model=EmployeeRead)
def update_employee(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    """Update an employee and their profile."""
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    # Update employee fields
    if employee.name:
        db_employee.name = employee.name
    if employee.office:
        db_employee.office = employee.office

    # Update profile if it exists
    if db_employee.profile_id:
        profile = db.query(Profile).filter(Profile.id == db_employee.profile_id).first()
        if profile:
            if employee.hard_skills is not None:
                profile.hard_skills = employee.hard_skills
            if employee.soft_skills is not None:
                profile.soft_skills = employee.soft_skills
            if employee.languages is not None:
                profile.languages = employee.languages
    else:
        # Create profile if it doesn't exist
        if employee.hard_skills or employee.soft_skills or employee.languages:
            profile = Profile(
                hard_skills=employee.hard_skills or "",
                soft_skills=employee.soft_skills or "",
                languages=employee.languages or ""
            )
            db.add(profile)
            db.flush()
            db_employee.profile_id = profile.id

    db.commit()
    db.refresh(db_employee)
    return format_employee_response(db_employee)


@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    """Delete an employee."""
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(db_employee)
    db.commit()
    return {"message": "Employee deleted"}
