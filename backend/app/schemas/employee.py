"""Employee request/response schemas."""

from pydantic import BaseModel
from typing import Optional


class EmployeeBase(BaseModel):
    """Base employee schema."""
    name: str
    office: Optional[str] = None


class EmployeeCreate(EmployeeBase):
    """Schema for creating employee with optional profile data."""
    profile_id: Optional[int] = None
    hard_skills: Optional[str] = None
    soft_skills: Optional[str] = None
    languages: Optional[str] = None


class EmployeeRead(EmployeeBase):
    """Schema for reading employee."""
    id: int
    profile_id: int

    class Config:
        from_attributes = True


class EmployeeUpdate(BaseModel):
    """Schema for updating employee."""
    name: Optional[str] = None
    office: Optional[str] = None
    profile_id: Optional[int] = None