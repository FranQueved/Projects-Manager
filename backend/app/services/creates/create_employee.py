"""Employee creation service - Validate and create employee records."""

from typing import List
from app.schemas.employee import EmployeeCreate
from app.models.employee import Employee
from app.models.profile import Profile
from app.db.database import SessionLocal


class EmployeeCreator:
    """Service for creating employees with profile validation."""

    def __init__(self):
        self.db = SessionLocal()

    def create_one(self, data: dict) -> Employee:
        """Create single employee with profile."""
        schema = EmployeeCreate(**data)
        profile = self.db.query(Profile).filter(Profile.id == schema.profile_id).first()
        
        if not profile:
            raise ValueError(f"Profile {schema.profile_id} does not exist")

        existing = self.db.query(Employee).filter(Employee.profile_id == schema.profile_id).first()
        if existing:
            raise ValueError(f"Profile {schema.profile_id} already assigned to employee {existing.id}")

        employee = Employee(**schema.dict())
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)
        return employee

    def create_many(self, data_list: List[dict]) -> List[Employee]:
        """Create multiple employees with profile validation."""
        created = []

        for data in data_list:
            schema = EmployeeCreate(**data)
            profile = self.db.query(Profile).filter(Profile.id == schema.profile_id).first()
            
            if not profile:
                raise ValueError(f"Profile {schema.profile_id} does not exist")

            existing = self.db.query(Employee).filter(Employee.profile_id == schema.profile_id).first()
            if existing:
                raise ValueError(f"Profile {schema.profile_id} already assigned to employee {existing.id}")

            employee = Employee(**schema.dict())
            self.db.add(employee)
            created.append(employee)

        self.db.commit()
        for employee in created:
            self.db.refresh(employee)

        return created

    def close(self):
        """Close database session."""
        self.db.close()