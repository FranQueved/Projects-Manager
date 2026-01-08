"""
Recommendations routes - Get employee recommendations based on project requirements.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.project import Project
from app.models.employee import Employee
from app.models.required_profile import RequiredProfile
from app.services.vectorial_services.embedding_service import EmbeddingService
from app.services.vectorial_services.embedding_comparation import compare_embeddings

router = APIRouter(prefix="/recommendations", tags=["recommendations"])

embedding_service = EmbeddingService()


@router.get("/employees/{project_id}")
def get_employee_recommendations(project_id: int, db: Session = Depends(get_db)):
    """
    Get employee recommendations for a project based on required profile similarity.
    Returns all employees sorted by similarity score.
    """
    # Get project
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Get required profile for the project
    required_profile = db.query(RequiredProfile).filter(
        RequiredProfile.project_id == project_id
    ).first()
    
    if not required_profile:
        # If no required profile, return all employees
        employees = db.query(Employee).all()
        return [
            {
                "id": emp.id,
                "name": emp.name,
                "office": emp.office,
                "hard_skills": emp.profile.hard_skills if emp.profile else "",
                "soft_skills": emp.profile.soft_skills if emp.profile else "",
                "languages": emp.profile.languages if emp.profile else "",
                "similarity_score": 0.0,
                "recommendation_reason": "Sin perfil requerido"
            }
            for emp in employees
        ]
    
    # Get all employees
    all_employees = db.query(Employee).all()
    
    # Create profile strings
    required_profile_str = f"{required_profile.hard_skills} {required_profile.soft_skills} {required_profile.languages}"
    
    # Calculate embeddings
    required_embedding = embedding_service.generate_embedding(required_profile_str)
    
    if not required_embedding:
        raise HTTPException(status_code=500, detail="Failed to generate embedding for required profile")
    
    recommendations = []
    
    for employee in all_employees:
        if not employee.profile:
            continue
            
        employee_profile_str = f"{employee.profile.hard_skills} {employee.profile.soft_skills} {employee.profile.languages}"
        employee_embedding = embedding_service.generate_embedding(employee_profile_str)
        
        if not employee_embedding:
            continue
        
        # Calculate similarity
        similarity_score = compare_embeddings(required_embedding, employee_embedding)
        
        # Determine recommendation reason
        if similarity_score >= 0.8:
            reason = "Excelente coincidencia"
        elif similarity_score >= 0.6:
            reason = "Buena coincidencia"
        elif similarity_score >= 0.4:
            reason = "Coincidencia aceptable"
        else:
            reason = "Baja coincidencia"
        
        recommendations.append({
            "id": employee.id,
            "name": employee.name,
            "office": employee.office,
            "hard_skills": employee.profile.hard_skills,
            "soft_skills": employee.profile.soft_skills,
            "languages": employee.profile.languages,
            "similarity_score": float(similarity_score),
            "recommendation_reason": reason
        })
    
    # Sort by similarity score (highest first)
    recommendations.sort(key=lambda x: x["similarity_score"], reverse=True)
    
    return recommendations

@router.get("/required-profile/{required_profile_id}")
def get_recommendations_for_required_profile(required_profile_id: int, db: Session = Depends(get_db)):
    """
    Get employee recommendations for a specific required profile.
    Returns all employees sorted by similarity score to the required profile.
    """
    # Get required profile
    required_profile = db.query(RequiredProfile).filter(
        RequiredProfile.id == required_profile_id
    ).first()
    
    if not required_profile:
        raise HTTPException(status_code=404, detail="Required profile not found")
    
    # Get all employees
    all_employees = db.query(Employee).all()
    
    # Create profile strings
    required_profile_str = f"{required_profile.hard_skills} {required_profile.soft_skills} {required_profile.languages}"
    
    # Calculate embeddings
    required_embedding = embedding_service.generate_embedding(required_profile_str)
    
    if not required_embedding:
        raise HTTPException(status_code=500, detail="Failed to generate embedding for required profile")
    
    recommendations = []
    
    for employee in all_employees:
        if not employee.profile:
            continue
            
        employee_profile_str = f"{employee.profile.hard_skills} {employee.profile.soft_skills} {employee.profile.languages}"
        employee_embedding = embedding_service.generate_embedding(employee_profile_str)
        
        if not employee_embedding:
            continue
        
        # Calculate similarity
        similarity_score = compare_embeddings(required_embedding, employee_embedding)
        
        # Determine recommendation reason
        if similarity_score >= 0.8:
            reason = "Excelente coincidencia"
        elif similarity_score >= 0.6:
            reason = "Buena coincidencia"
        elif similarity_score >= 0.4:
            reason = "Coincidencia aceptable"
        else:
            reason = "Baja coincidencia"
        
        recommendations.append({
            "id": employee.id,
            "name": employee.name,
            "office": employee.office,
            "hard_skills": employee.profile.hard_skills,
            "soft_skills": employee.profile.soft_skills,
            "languages": employee.profile.languages,
            "similarity_score": float(similarity_score),
            "recommendation_reason": reason
        })
    
    # Sort by similarity score (highest first)
    recommendations.sort(key=lambda x: x["similarity_score"], reverse=True)
    
    return recommendations