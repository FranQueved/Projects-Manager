"""
Required Profiles routes - Manage required skills for projects.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.required_profile import RequiredProfile
from app.models.project import Project
from pydantic import BaseModel

router = APIRouter(prefix="/required-profiles", tags=["required_profiles"])


class RequiredProfileCreate(BaseModel):
    """Schema for creating a required profile."""
    project_id: int
    hard_skills: str
    soft_skills: str
    languages: str


class RequiredProfileUpdate(BaseModel):
    """Schema for updating a required profile."""
    hard_skills: str
    soft_skills: str
    languages: str


class RequiredProfileRead(BaseModel):
    """Schema for reading a required profile."""
    id: int
    project_id: int
    hard_skills: str
    soft_skills: str
    languages: str

    class Config:
        from_attributes = True


@router.get("/project/{project_id}")
def get_project_required_profiles(project_id: int, db: Session = Depends(get_db)):
    """Get all required profiles for a project."""
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    required_profiles = db.query(RequiredProfile).filter(
        RequiredProfile.project_id == project_id
    ).all()
    
    return [
        {
            "id": rp.id,
            "project_id": rp.project_id,
            "hard_skills": rp.hard_skills,
            "soft_skills": rp.soft_skills,
            "languages": rp.languages,
        }
        for rp in required_profiles
    ]


@router.post("")
def create_required_profile(data: RequiredProfileCreate, db: Session = Depends(get_db)):
    """Create a new required profile for a project."""
    project = db.query(Project).filter(Project.id == data.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    required_profile = RequiredProfile(
        project_id=data.project_id,
        hard_skills=data.hard_skills,
        soft_skills=data.soft_skills,
        languages=data.languages,
    )
    
    db.add(required_profile)
    db.flush()
    
    # Get the ID before commit
    required_profile_id = required_profile.id
    db.commit()
    
    return {
        "id": required_profile_id,
        "project_id": data.project_id,
        "hard_skills": data.hard_skills,
        "soft_skills": data.soft_skills,
        "languages": data.languages,
    }


@router.get("/{required_profile_id}")
def get_required_profile(required_profile_id: int, db: Session = Depends(get_db)):
    """Get a specific required profile."""
    required_profile = db.query(RequiredProfile).filter(
        RequiredProfile.id == required_profile_id
    ).first()
    
    if not required_profile:
        raise HTTPException(status_code=404, detail="Required profile not found")
    
    return {
        "id": required_profile.id,
        "project_id": required_profile.project_id,
        "hard_skills": required_profile.hard_skills,
        "soft_skills": required_profile.soft_skills,
        "languages": required_profile.languages,
    }


@router.put("/{required_profile_id}")
def update_required_profile(
    required_profile_id: int,
    data: RequiredProfileUpdate,
    db: Session = Depends(get_db)
):
    """Update a required profile."""
    required_profile = db.query(RequiredProfile).filter(
        RequiredProfile.id == required_profile_id
    ).first()
    
    if not required_profile:
        raise HTTPException(status_code=404, detail="Required profile not found")
    
    required_profile.hard_skills = data.hard_skills
    required_profile.soft_skills = data.soft_skills
    required_profile.languages = data.languages
    
    db.commit()
    
    return {
        "id": required_profile.id,
        "project_id": required_profile.project_id,
        "hard_skills": required_profile.hard_skills,
        "soft_skills": required_profile.soft_skills,
        "languages": required_profile.languages,
    }


@router.delete("/{required_profile_id}")
def delete_required_profile(required_profile_id: int, db: Session = Depends(get_db)):
    """Delete a required profile."""
    required_profile = db.query(RequiredProfile).filter(
        RequiredProfile.id == required_profile_id
    ).first()
    
    if not required_profile:
        raise HTTPException(status_code=404, detail="Required profile not found")
    
    db.delete(required_profile)
    db.commit()
    
    return {"message": "Required profile deleted successfully"}
