"""Project request/response schemas."""

from pydantic import BaseModel
from datetime import date


class ProjectBase(BaseModel):
    """Base project schema."""
    name: str
    description: str
    client: str = "Internal"
    start_date: date
    end_date: date | None = None
    finished: bool = False
    budget: int
    presential: bool = False


class ProjectCreate(ProjectBase):
    """Schema for creating project."""
    pass


class ProjectRead(ProjectBase):
    """Schema for reading project."""
    id: int

    class Config:
        from_attributes = True


class ProjectUpdate(ProjectBase):
    """Schema for updating project."""
    pass