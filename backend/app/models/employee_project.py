from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.database import Base

employee_project = Table(
    "employee_project",
    Base.metadata,
    Column("employee_id", Integer, ForeignKey("employees.id"), primary_key=True),
    Column("project_id", Integer, ForeignKey("projects.id"), primary_key=True),
)
