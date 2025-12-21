"""
Modelo de Perfil Profesional Requerido.

Replica la estructura de Profile para reutilizar la definición con un nombre distinto.
"""

from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class RequiredProfile(Base):
    """
    Representa un perfil profesional requerido con habilidades y competencias.
    
    Atributos:
        id: Identificador único
        project_id: Proyecto al que pertenece (relación 1:N)
        hard_skills: Habilidades técnicas requeridas/poseer (ej: Python, SQL, Docker)
        soft_skills: Habilidades blandas (ej: Liderazgo, Comunicación)
        languages: Lenguajes de programación/idiomas dominados
        created_at: Timestamp de creación

    Relaciones:
        project: Proyecto que requiere este perfil (1:N)
    """
    
    __tablename__ = "required_profiles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True)
    hard_skills = Column(String, nullable=False)
    soft_skills = Column(String, nullable=False)
    languages = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    project = relationship("Project", back_populates="required_profiles", foreign_keys=[project_id])

    def __repr__(self):
        return f"<RequiredProfile(id={self.id}, project_id={self.project_id}, skills='{self.hard_skills[:30]}...')>"
