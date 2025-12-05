from sqlalchemy import Column, Integer, String , Boolean
from app.db.database import Base

class Proyect(Base):
    __tablename__ = "proyects"

    id_p = Column(Integer, primary_key=True, index=True , autoincrement=True) 
    name = Column(String, nullable=False)
    description = Column(String)
    client = Column(String, nullable=False)
    finished = Column(Boolean, default=False)
    budget = Column(Integer)
    presential = Column(Boolean, default=False)

