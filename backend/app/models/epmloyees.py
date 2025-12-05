from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Trabajador(Base):
    __tablename__ = "employees"

    id_t = Column(Integer, primary_key=True, index=True , autoincrement=True) 
    name = Column(String, nullable=False)
    hard_skills = Column(String)
    oficce = Column(String)