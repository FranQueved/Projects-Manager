# app/schemas/project.py

from pydantic import BaseModel
from datetime import date

# Base: campos comunes entre entrada y salida
class ProjectBase(BaseModel):
    name: str
    description: str
    client: str = "Internal"
    start_date: date
    end_date: date | None = None
    finished: bool = False
    budget: int
    presential: bool = False

# Schema para crear un proyecto (lo que envía el frontend)
class ProjectCreate(ProjectBase):
    pass

# Schema para leer un proyecto (lo que devuelves al frontend)
class ProjectRead(ProjectBase):
    id: int

    class Config:
        orm_mode = True
