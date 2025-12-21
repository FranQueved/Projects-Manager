"""
Required Profile Model - Professional skills required for a project.
"""

from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class RequiredProfile(Base):
    """Professional profile required for project execution."""
    
    __tablename__ = "required_profiles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False, index=True)
    hard_skills = Column(String, nullable=False)
    soft_skills = Column(String, nullable=False)
    languages = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    project = relationship("Project", back_populates="required_profiles", foreign_keys=[project_id])

    def __repr__(self):
        return f"<RequiredProfile(id={self.id}, project_id={self.project_id}, skills='{self.hard_skills[:30]}...')>"
