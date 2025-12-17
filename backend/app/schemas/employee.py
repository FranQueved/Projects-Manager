# app/schemas/employee.py

from pydantic import BaseModel
from typing import Optional

# Base: campos comunes entre entrada y salida
class EmployeeBase(BaseModel):
    name: str
    office: Optional[str] = None

# Schema para crear un empleado (lo que envía el frontend)
class EmployeeCreate(EmployeeBase):
    pass

# Schema para leer un empleado (lo que devuelves al frontend)
class EmployeeRead(EmployeeBase):
    id: int
    profile_id: Optional[int] = None

    class Config:
        orm_mode = True

# Schema para actualizar un empleado
class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    office: Optional[str] = None