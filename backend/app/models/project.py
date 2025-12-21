"""
Project Model - Represents a company project with team and required skills.
"""

from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, func
from sqlalchemy.orm import relationship
from app.db.database import Base


class Project(Base):
    """Company project with team assignments and required profiles."""
    
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

    employees = relationship(
        "Employee",
        secondary="employee_project",
        back_populates="projects"
    )
    
    required_profiles = relationship(
        "RequiredProfile",
        back_populates="project",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Project(id={self.id}, name='{self.name}', client='{self.client}')>"
