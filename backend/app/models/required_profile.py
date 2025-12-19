"""
Modelo de Perfil Requerido por Proyecto.

Representa la relación N:M entre proyectos y perfiles requeridos.
Define qué perfiles profesionales son necesarios para ejecutar un proyecto.
"""

from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, func
from sqlalchemy.orm import relationship
from app.db.database import Base


class RequiredProfile(Base):
    """
    Representa un perfil requerido por un proyecto (relación N:M).
    
    Atributos:
        id: Identificador único
        project_id: ID del proyecto que requiere el perfil
        hard_skills: Habilidades técnicas requeridas
        soft_skills: Habilidades blandas requeridas
        languages: Idiomas requeridos
        created_at: Timestamp de creación
    
    Relaciones:
        project: El proyecto que requiere este perfil
    """
    
    __tablename__ = "required_profiles"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True)
    
    hard_skills = Column(String, nullable=False)
    soft_skills = Column(String, nullable=False)
    languages = Column(String, nullable=False)
    
    created_at = Column(DateTime, default=func.now(), nullable=False)

    # Relaciones
    project = relationship("Project", back_populates="required_profiles", foreign_keys=[project_id])

    def __repr__(self):
        return f"<RequiredProfile(id={self.id}, project_id={self.project_id})>"
