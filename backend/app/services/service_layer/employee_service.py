"""Employee service - CRUD operations for employees."""

from typing import List, Optional
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.employee import EmployeeCreate, EmployeeUpdate
from app.models.employee import Employee
from app.models.profile import Profile
from app.services.vectorial_services.embedding_service import EmbeddingService


class EmployeeService:
    """Employee CRUD service."""

    def __init__(self):
        self.db: Session = SessionLocal()
        self.embedding_service = EmbeddingService()

    def create_one(self, data: dict) -> Employee:
        """Create single employee with auto profile creation and embedding generation."""
        schema = EmployeeCreate(**data)
        
        # If profile_id is provided, use existing profile
        if schema.profile_id:
            profile = self.db.query(Profile).filter(Profile.id == schema.profile_id).first()
            if not profile:
                raise ValueError(f"Profile {schema.profile_id} does not exist")
            
            existing = self.db.query(Employee).filter(Employee.profile_id == schema.profile_id).first()
            if existing:
                raise ValueError(f"Profile {schema.profile_id} already assigned to employee {existing.id}")
        # Otherwise, create new profile from provided data
        elif schema.hard_skills or schema.soft_skills or schema.languages:
            profile = Profile(
                hard_skills=schema.hard_skills or "",
                soft_skills=schema.soft_skills or "",
                languages=schema.languages or ""
            )
            self.db.add(profile)
            self.db.flush()
        else:
            raise ValueError("Either profile_id or profile data (hard_skills, soft_skills, languages) must be provided")
        
        # Create employee with profile
        employee_data = {
            "name": schema.name,
            "office": schema.office,
            "profile_id": profile.id
        }
        employee = Employee(**employee_data)
        self.db.add(employee)
        self.db.commit()
        self.db.refresh(employee)
        
        self.embedding_service.create_embedding_for_employee(employee.id)
        
        return employee

    def create_many(self, data_list: List[dict]) -> List[Employee]:
        """Create multiple employees with auto profile creation and embedding generation."""
        created = []
        for data in data_list:
            schema = EmployeeCreate(**data)
            
            # If profile_id is provided, use existing profile
            if schema.profile_id:
                profile = self.db.query(Profile).filter(Profile.id == schema.profile_id).first()
                if not profile:
                    raise ValueError(f"Profile {schema.profile_id} does not exist")
                
                existing = self.db.query(Employee).filter(Employee.profile_id == schema.profile_id).first()
                if existing:
                    raise ValueError(f"Profile {schema.profile_id} already assigned to employee {existing.id}")
            # Otherwise, create new profile from provided data
            elif schema.hard_skills or schema.soft_skills or schema.languages:
                profile = Profile(
                    hard_skills=schema.hard_skills or "",
                    soft_skills=schema.soft_skills or "",
                    languages=schema.languages or ""
                )
                self.db.add(profile)
                self.db.flush()
            else:
                raise ValueError("Either profile_id or profile data (hard_skills, soft_skills, languages) must be provided")
            
            # Create employee with profile
            employee_data = {
                "name": schema.name,
                "office": schema.office,
                "profile_id": profile.id
            }
            employee = Employee(**employee_data)
            self.db.add(employee)
            created.append(employee)
        
        self.db.commit()
        for employee in created:
            self.db.refresh(employee)
            self.embedding_service.create_embedding_for_employee(employee.id)
        return created

    def get_by_id(self, employee_id: int) -> Optional[Employee]:
        """Get employee by ID."""
        return self.db.query(Employee).filter(Employee.id == employee_id).first()

    def get_all(self) -> List[Employee]:
        """Get all employees."""
        return self.db.query(Employee).all()

    def get_by_office(self, office: str) -> List[Employee]:
        """Get employees by office."""
        return self.db.query(Employee).filter(Employee.office == office).all()

    def get_by_name(self, name: str) -> List[Employee]:
        """Get employees by name (partial search)."""
        return self.db.query(Employee).filter(Employee.name.ilike(f"%{name}%")).all()

    def get_with_profile(self, employee_id: int) -> Optional[Employee]:
        """Get employee with loaded profile."""
        return self.db.query(Employee).filter(Employee.id == employee_id).first()

    def get_profile_of_employee(self, employee_id: int) -> Optional[Profile]:
        """Get profile associated with employee."""
        employee = self.get_by_id(employee_id)
        if employee:
            return employee.profile
        return None

    def close(self):
        """Close database session and embedding service."""
        self.db.close()
        self.embedding_service.close()

    def update_by_id(self, employee_id: int, data: dict) -> Optional[Employee]:
        """Update employee."""
        employee = self.get_by_id(employee_id)
        if not employee:
            return None

        schema = EmployeeUpdate(**data)
        update_data = schema.dict(exclude_unset=True)

        if "profile_id" in update_data:
            new_profile_id = update_data["profile_id"]
            profile = self.db.query(Profile).filter(Profile.id == new_profile_id).first()
            if not profile:
                raise ValueError(f"Profile {new_profile_id} does not exist")

            existing = self.db.query(Employee).filter(Employee.profile_id == new_profile_id).first()
            if existing and existing.id != employee_id:
                raise ValueError(f"Profile {new_profile_id} already assigned to another employee")

        for key, value in update_data.items():
            setattr(employee, key, value)
        self.db.commit()
        self.db.refresh(employee)
        return employee

    def delete_by_id(self, employee_id: int) -> bool:
        """Delete employee."""
        employee = self.get_by_id(employee_id)
        if employee:
            self.db.delete(employee)
            self.db.commit()
            return True
        return False

    def close(self):
        """Close database session."""
        self.db.close()
