from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    hardSkills = Column(String, nullable=False)
    softSkills = Column(String, nullable=False)
    languages = Column(String, nullable=False)

    # Relación con Employee (uno a uno)
    employee = relationship("Employee", back_populates="profile", uselist=False)