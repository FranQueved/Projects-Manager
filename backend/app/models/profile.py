from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from app.db.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    hardSkills = Column(String, nullable=False)
    softSkills = Column(String, nullable=False)
    languages = Column(String, nullable=False)
    embedding = Column(ARRAY(Float), nullable=True)  # Embedding del perfil para búsquedas vectoriales

    # Relación con Employee (uno a uno)
    employee = relationship("Employee", back_populates="profile", uselist=False)
    
    # Relación con proyectos que lo requieren (1:N)
    required_by_projects = relationship(
        "RequiredProfile",
        back_populates="profile"
    )