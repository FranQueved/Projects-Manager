"""
Employee-Project Association - Many-to-many relationship table.
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
