"""
Modelo de Proyecto.

Representa un proyecto con sus detalles, equipo asignado y perfiles requeridos.
"""

from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, func
from sqlalchemy.orm import relationship
from app.db.database import Base


class Project(Base):
    """
    Representa un proyecto del sistema.
    
    Atributos:
        id: Identificador único
        name: Nombre del proyecto
        description: Descripción del proyecto
        client: Cliente o empresa para el cual se desarrolla
        start_date: Fecha de inicio
        end_date: Fecha de finalización (nullable)
        finished: Estado de finalización
        budget: Presupuesto del proyecto
        presential: Si requiere trabajo presencial
        created_at: Timestamp de creación
    
    Relaciones:
        employees: Empleados asignados al proyecto (N:M)
        required_profiles: Perfiles requeridos para el proyecto (1:N)
    """
    
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    description = Column(String, nullable=False)
    client = Column(String(255), nullable=False, default="Internal", index=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    finished = Column(Boolean, default=False, index=True)
    budget = Column(Integer, nullable=False)
    presential = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    # Relación N:M con Employees (mediante tabla employee_project)
    employees = relationship(
        "Employee",
        secondary="employee_project",
        back_populates="projects"
    )
    
    # Relación 1:N con RequiredProfiles
    required_profiles = relationship(
        "RequiredProfile",
        back_populates="project",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Project(id={self.id}, name='{self.name}', client='{self.client}')>"

    def __str__(self):
        return f"{self.name} ({self.client}) - {self.start_date} a {self.end_date}"
