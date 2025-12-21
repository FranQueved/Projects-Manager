"""
Employee Model - Represents a company employee with profile and project assignments.
"""

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.db.database import Base


class Employee(Base):
    """Company employee with professional profile and project assignments."""
    
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    office = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    profile_id = Column(
        Integer,
        ForeignKey("profiles.id", ondelete="CASCADE"),
        unique=True,
        nullable=False
    )

    profile = relationship(
        "Profile",
        back_populates="employee",
        uselist=False,
        foreign_keys=[profile_id]
    )

    projects = relationship(
        "Project",
        secondary="employee_project",
        back_populates="employees"
    )

    def __repr__(self):
        return f"<Employee(id={self.id}, name='{self.name}', office='{self.office}')>"

    def __str__(self):
        return f"{self.name} ({self.office})"
