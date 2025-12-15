# app/schemas/profile.py

from pydantic import BaseModel
from typing import Optional

# Base: campos comunes entre entrada y salida
class ProfileBase(BaseModel):
    hardSkills: str
    softSkills: str
    languages: str

# Schema para crear un perfil (lo que envía el frontend)
class ProfileCreate(ProfileBase):
    pass

# Schema para leer un perfil (lo que devuelves al frontend)
class ProfileRead(ProfileBase):
    id: int

    class Config:
        orm_mode = True

# Schema para actualizar un perfil
class ProfileUpdate(BaseModel):
    hardSkills: Optional[str] = None
    softSkills: Optional[str] = None
    languages: Optional[str] = None