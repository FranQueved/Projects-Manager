"""
Profile Model - Represents professional skills and competencies.
"""

from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.db.database import Base


class Profile(Base):
    """Professional profile with technical and soft skills."""
    
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    hard_skills = Column(String, nullable=False)
    soft_skills = Column(String, nullable=False)
    languages = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    employee = relationship(
        "Employee",
        back_populates="profile",
        uselist=False,
        foreign_keys="Employee.profile_id"
    )

    def __repr__(self):
        return f"<Profile(id={self.id}, skills='{self.hard_skills[:30]}...')>"