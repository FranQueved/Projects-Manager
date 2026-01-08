"""
Project routes - CRUD operations for projects.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectRead, ProjectUpdate

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("/", response_model=list[ProjectRead])
def list_projects(db: Session = Depends(get_db)):
    """List all projects."""
    projects = db.query(Project).all()
    return projects


@router.get("/{project_id}", response_model=ProjectRead)
def get_project(project_id: int, db: Session = Depends(get_db)):
    """Get a specific project by ID."""
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.post("/", response_model=ProjectRead)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    """Create a new project."""
    db_project = Project(
        name=project.name,
        description=project.description,
        client=project.client,
        start_date=project.start_date,
        end_date=project.end_date,
        finished=project.finished,
        budget=project.budget,
        presential=project.presential
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


@router.put("/{project_id}")
def update_project(
    project_id: int,
    project: ProjectUpdate,
    db: Session = Depends(get_db)
):
    """Update a project."""
    db_project = db.query(Project).filter(Project.id == project_id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")

    if project.name:
        db_project.name = project.name
    if project.description:
        db_project.description = project.description
    if project.client:
        db_project.client = project.client
    if project.start_date:
        db_project.start_date = project.start_date
    db_project.end_date = project.end_date
    db_project.finished = project.finished
    if project.budget:
        db_project.budget = project.budget
    db_project.presential = project.presential

    db.commit()
    
    # Format response to include employees
    return {
        "id": db_project.id,
        "name": db_project.name,
        "description": db_project.description,
        "client": db_project.client,
        "start_date": db_project.start_date,
        "end_date": db_project.end_date,
        "finished": db_project.finished,
        "budget": db_project.budget,
        "presential": db_project.presential,
        "employees": [
            {
                "id": emp.id,
                "name": emp.name,
                "office": emp.office
            }
            for emp in db_project.employees
        ] if db_project.employees else []
    }


@router.delete("/{project_id}")
def delete_project(project_id: int, db: Session = Depends(get_db)):
    """Delete a project."""
    db_project = db.query(Project).filter(Project.id == project_id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(db_project)
    db.commit()
    return {"message": "Project deleted"}
