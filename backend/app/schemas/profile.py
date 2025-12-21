"""Profile request/response schemas."""

from pydantic import BaseModel
from typing import Optional


class ProfileBase(BaseModel):
    """Base profile schema."""
    hard_skills: str
    soft_skills: str
    languages: str


class ProfileCreate(ProfileBase):
    """Schema for creating profile."""
    pass


class ProfileRead(ProfileBase):
    """Schema for reading profile."""
    id: int

    class Config:
        from_attributes = True


class ProfileUpdate(BaseModel):
    """Schema for updating profile."""
    hard_skills: Optional[str] = None
    soft_skills: Optional[str] = None
    languages: Optional[str] = None