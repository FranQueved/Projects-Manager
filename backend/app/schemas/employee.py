"""Employee request/response schemas."""

from pydantic import BaseModel
from typing import Optional


class EmployeeBase(BaseModel):
    """Base employee schema."""
    name: str
    office: Optional[str] = None


class EmployeeCreate(EmployeeBase):
    """Schema for creating employee."""
    profile_id: int


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