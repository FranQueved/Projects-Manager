from sqlalchemy import Column, Integer, String, Boolean, Date , ForeignKeyConstraint
from sqlalchemy.orm import relationship
from app.db.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    client = Column(String, nullable=False, default="Internal")
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    finished = Column(Boolean, default=False)
    budget = Column(Integer, nullable=False)
    presential = Column(Boolean, default=False)
    employees = relationship(
        "Employee",
        secondary="employee_project",
        back_populates="projects"
    )
