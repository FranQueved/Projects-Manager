"""
Tabla Asociativa: Empleado-Proyecto.

Establece la relación N:M entre empleados y proyectos.
Un empleado puede trabajar en múltiples proyectos y un proyecto puede tener múltiples empleados.
"""

from sqlalchemy import Table, Column, Integer, ForeignKey, DateTime, func
from app.db.database import Base

employee_project = Table(
    "employee_project",
    Base.metadata,
    Column("employee_id", Integer, ForeignKey("employees.id", ondelete="CASCADE"), primary_key=True, index=True),
    Column("project_id", Integer, ForeignKey("projects.id", ondelete="CASCADE"), primary_key=True, index=True),
    Column("assigned_at", DateTime, default=func.now(), nullable=False),
)
