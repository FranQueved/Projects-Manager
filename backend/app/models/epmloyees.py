from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    office = Column(String)

    profile_id = Column(Integer, ForeignKey("profiles.id"), unique=True)
    profile = relationship("Profile", back_populates="employee", uselist=False)

    projects = relationship(
        "Project",
        secondary="employee_project",
        back_populates="employees"
    )
