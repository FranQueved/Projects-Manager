"""
Modelo de relación N-M entre Proyectos y Perfiles Requeridos.
Define qué perfiles son necesarios para cada proyecto.
"""

from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.database import Base


class RequiredProfile(Base):
    __tablename__ = "required_profiles"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    profile_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=False)

    # Relaciones
    project = relationship("Project", back_populates="required_profiles")
    profile = relationship("Profile", back_populates="required_by_projects")

    # Constraint: No duplicar la misma combinación proyecto-perfil
    __table_args__ = (UniqueConstraint('project_id', 'profile_id', name='uq_project_profile'),)
