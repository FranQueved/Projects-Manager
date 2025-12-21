"""
Modelo de Empleado.

Representa un empleado con su información de contacto, oficina y relación con un perfil profesional.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.db.database import Base


class Employee(Base):
    """
    Representa un empleado del sistema.
    
    Atributos:
        id: Identificador único
        name: Nombre completo del empleado
        office: Ubicación/oficina del empleado
        profile_id: Referencia al perfil profesional (relación 1:1)
        created_at: Timestamp de creación
    
    Relaciones:
        profile: Perfil profesional del empleado (1:1)
        projects: Proyectos en los que trabaja (N:M)
    """
    
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    office = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    # Relación 1:1 con Profile
    profile_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), unique=True, nullable=False)
    profile = relationship(
        "Profile",
        back_populates="employee",
        uselist=False,
        foreign_keys=[profile_id]
    )

    # Relación N:M con Projects
    projects = relationship(
        "Project",
        secondary="employee_project",
        back_populates="employees"
    )

    def __repr__(self):
        return f"<Employee(id={self.id}, name='{self.name}', office='{self.office}')>"

    def __str__(self):
        return f"{self.name} ({self.office})"
