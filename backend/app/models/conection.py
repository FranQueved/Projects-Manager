from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Conection(Base):
    __tablename__ = "conections"

    id_c = Column(Integer, primary_key=True, index=True , autoincrement=True) 
    type = Column(String, nullable=False)
    details = Column(String)