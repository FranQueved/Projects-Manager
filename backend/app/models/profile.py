"""
Modelo de Perfil Profesional.

Representa las competencias y habilidades de un empleado o requisito de proyecto.
"""

from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.db.database import Base


class Profile(Base):
    """
    Representa un perfil profesional con habilidades y competencias.
    
    Atributos:
        id: Identificador único
        hard_skills: Habilidades técnicas requeridas/poseer (ej: Python, SQL, Docker)
        soft_skills: Habilidades blandas (ej: Liderazgo, Comunicación)
        languages: Lenguajes de programación/idiomas dominados
        created_at: Timestamp de creación
    
    Relaciones:
        employee: Empleado que posee este perfil (1:1 obligatorio)
        required_by_projects: Proyectos que lo requieren (0:N)
    """
    
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    hard_skills = Column(String, nullable=False)
    soft_skills = Column(String, nullable=False)
    languages = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    # Relación 1:1 con Employee (un empleado puede tener un perfil)
    employee = relationship("Employee", back_populates="profile", uselist=False, foreign_keys="Employee.profile_id")
    

    def __repr__(self):
        return f"<Profile(id={self.id}, skills='{self.hard_skills[:30]}...')>"

    def __str__(self):
        return f"Hard: {self.hard_skills} | Soft: {self.soft_skills} | Languages: {self.languages}"