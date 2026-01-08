#!/usr/bin/env python
"""
Script para popular la base de datos con datos de prueba.
Ejecutar desde la carpeta backend: python populate_db.py
"""

import sys
import os

# Añadir el directorio backend al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.db.database import SessionLocal, Base, engine
from app.models.employee import Employee
from app.models.profile import Profile
from app.models.project import Project
from app.models.employee_project import EmployeeProject
from app.services.fixtures.seed_data import EMPLOYEES_DATA, PROJECTS_DATA
from datetime import datetime

def populate_database():
    """Populate the database with seed data."""
    
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    # Get database session
    db = SessionLocal()
    
    try:
        # Clear existing data
        db.query(EmployeeProject).delete()
        db.query(Employee).delete()
        db.query(Project).delete()
        db.query(Profile).delete()
        db.commit()
        print("✓ Cleared existing data")
        
        # Create profiles and employees
        for emp_data in EMPLOYEES_DATA:
            # Create profile
            profile = Profile(
                hard_skills=emp_data.get("hard_skills", ""),
                soft_skills=emp_data.get("soft_skills", ""),
                languages=emp_data.get("languages", "")
            )
            db.add(profile)
            db.flush()
            
            # Create employee
            employee = Employee(
                name=emp_data["name"],
                email=emp_data["email"],
                department=emp_data.get("department", ""),
                profile_id=profile.id
            )
            db.add(employee)
        
        db.commit()
        print(f"✓ Created {len(EMPLOYEES_DATA)} employees with profiles")
        
        # Create projects
        for proj_data in PROJECTS_DATA:
            project = Project(
                name=proj_data["name"],
                description=proj_data.get("description", ""),
                status=proj_data.get("status", "active"),
                start_date=datetime.strptime(proj_data["start_date"], "%Y-%m-%d").date() if proj_data.get("start_date") else None,
                end_date=datetime.strptime(proj_data["end_date"], "%Y-%m-%d").date() if proj_data.get("end_date") else None
            )
            db.add(project)
        
        db.commit()
        print(f"✓ Created {len(PROJECTS_DATA)} projects")
        
        # Create random employee-project assignments
        employees = db.query(Employee).all()
        projects = db.query(Project).all()
        
        assignment_count = 0
        for employee in employees:
            # Assign each employee to 1-3 random projects
            num_projects = min(3, len(projects))
            assigned_projects = []
            for _ in range(num_projects):
                project = projects[int(len(projects) * __import__('random').random())]
                if project not in assigned_projects:
                    assigned_projects.append(project)
                    assignment = EmployeeProject(
                        employee_id=employee.id,
                        project_id=project.id
                    )
                    db.add(assignment)
                    assignment_count += 1
        
        db.commit()
        print(f"✓ Created {assignment_count} employee-project assignments")
        print("\n✅ Database population completed successfully!")
        
    except Exception as e:
        db.rollback()
        print(f"❌ Error: {e}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    populate_database()
