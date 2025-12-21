"""Example usage of the interactive app - Demo script."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.db.create_tables import InitDB
from app.services.service_layer.project_service import ProjectService
from app.services.service_layer.employee_service import EmployeeService
from app.services.service_layer.required_profile_service import RequiredProfileService
from app.services.service_layer.employee_project_service import EmployeeProjectService
from sqlalchemy import text
from app.db.database import SessionLocal


def demo():
    """Run a demo of the application."""
    
    print("\n" + "=" * 70)
    print("INTERACTIVE APP DEMO - Creating test data")
    print("=" * 70)
    
    # Initialize
    print("\n[1] Initializing database...")
    InitDB().create_tables()
    print("    ✓ Database ready")
    
    # Initialize services
    project_service = ProjectService()
    employee_service = EmployeeService()
    required_service = RequiredProfileService()
    assignment_service = EmployeeProjectService()
    db = SessionLocal()
    
    # Create projects
    print("\n[2] Creating projects...")
    project1 = project_service.create_one({
        "name": "AI Platform",
        "description": "Machine learning platform for data analysis"
    })
    print(f"    ✓ Project created: {project1.name} (ID {project1.id})")
    
    project2 = project_service.create_one({
        "name": "Web Application",
        "description": "Modern web application"
    })
    print(f"    ✓ Project created: {project2.name} (ID {project2.id})")
    
    # Add required profiles
    print("\n[3] Adding required profiles to projects...")
    req_profile1 = required_service.add_required_profile(
        project_id=project1.id,
        hard_skills="Python, Machine Learning, TensorFlow, PyTorch",
        soft_skills="Data analysis, Problem solving, Innovation",
        languages="English, Spanish"
    )
    print(f"    ✓ Required profile added to {project1.name} (ID {req_profile1.id})")
    print(f"      (Embedding auto-generated)")
    
    req_profile2 = required_service.add_required_profile(
        project_id=project2.id,
        hard_skills="JavaScript, React, Node.js, PostgreSQL",
        soft_skills="UI/UX thinking, Problem solving, Creativity",
        languages="English, Spanish"
    )
    print(f"    ✓ Required profile added to {project2.name} (ID {req_profile2.id})")
    print(f"      (Embedding auto-generated)")
    
    # Create employees
    print("\n[4] Creating employees with automatic profiles...")
    employee1 = employee_service.create_one({
        "name": "Juan García",
        "office": "Madrid",
        "hard_skills": "Python, FastAPI, Django, PostgreSQL, Machine Learning",
        "soft_skills": "Problem solving, Communication, Leadership",
        "languages": "Spanish, English"
    })
    print(f"    ✓ Employee created: {employee1.name} (ID {employee1.id})")
    print(f"      Profile ID: {employee1.profile_id} (auto-created)")
    print(f"      (Embedding auto-generated)")
    
    employee2 = employee_service.create_one({
        "name": "Ana López",
        "office": "Barcelona",
        "hard_skills": "JavaScript, React, TypeScript, Node.js, CSS",
        "soft_skills": "UI Design, Creativity, Communication",
        "languages": "Spanish, English, French"
    })
    print(f"    ✓ Employee created: {employee2.name} (ID {employee2.id})")
    print(f"      Profile ID: {employee2.profile_id} (auto-created)")
    print(f"      (Embedding auto-generated)")
    
    employee3 = employee_service.create_one({
        "name": "Carlos Pérez",
        "office": "Valencia",
        "hard_skills": "Python, Scikit-learn, Pandas, NumPy, Statistics",
        "soft_skills": "Data analysis, Attention to detail, Problem solving",
        "languages": "Spanish, English"
    })
    print(f"    ✓ Employee created: {employee3.name} (ID {employee3.id})")
    print(f"      Profile ID: {employee3.profile_id} (auto-created)")
    print(f"      (Embedding auto-generated)")
    
    # Assign employees to projects
    print("\n[5] Assigning employees to projects...")
    assignment_service.assign_employee_to_project(employee1.id, project1.id)
    print(f"    ✓ {employee1.name} assigned to {project1.name}")
    
    assignment_service.assign_employee_to_project(employee3.id, project1.id)
    print(f"    ✓ {employee3.name} assigned to {project1.name}")
    
    assignment_service.assign_employee_to_project(employee2.id, project2.id)
    print(f"    ✓ {employee2.name} assigned to {project2.name}")
    
    # Show statistics
    print("\n[6] Database statistics...")
    projects_count = db.execute(text("SELECT COUNT(*) FROM projects")).scalar()
    employees_count = db.execute(text("SELECT COUNT(*) FROM employees")).scalar()
    profiles_count = db.execute(text("SELECT COUNT(*) FROM profiles")).scalar()
    embeddings_count = db.execute(text("SELECT COUNT(*) FROM embeddings")).scalar()
    assignments_count = db.execute(text("SELECT COUNT(*) FROM employee_project")).scalar()
    req_profiles_count = db.execute(text("SELECT COUNT(*) FROM required_profiles")).scalar()
    
    print(f"\n    Projects:           {projects_count}")
    print(f"    Employees:          {employees_count}")
    print(f"    Profiles:           {profiles_count}")
    print(f"    Required Profiles:  {req_profiles_count}")
    print(f"    Embeddings:         {embeddings_count}")
    print(f"    Assignments:        {assignments_count}")
    
    # Show detailed info
    print("\n[7] Project Details:")
    print(f"\n    {project1.name}:")
    employees_in_p1 = assignment_service.get_employees_by_project(project1.id)
    print(f"      Employees assigned: {len(employees_in_p1)}")
    for e in employees_in_p1:
        print(f"        - {e.name} ({e.office})")
    
    print(f"\n    {project2.name}:")
    employees_in_p2 = assignment_service.get_employees_by_project(project2.id)
    print(f"      Employees assigned: {len(employees_in_p2)}")
    for e in employees_in_p2:
        print(f"        - {e.name} ({e.office})")
    
    print("\n[8] Employee Details:")
    print(f"\n    {employee1.name}:")
    projects_emp1 = assignment_service.get_projects_by_employee(employee1.id)
    print(f"      Projects assigned: {len(projects_emp1)}")
    for p in projects_emp1:
        print(f"        - {p.name}")
    
    # Show embeddings info
    print("\n[9] Embeddings information:")
    emp_embeddings = db.execute(
        text("SELECT COUNT(*) FROM embeddings WHERE profile_id IS NOT NULL")
    ).scalar()
    req_embeddings = db.execute(
        text("SELECT COUNT(*) FROM embeddings WHERE required_profile_id IS NOT NULL")
    ).scalar()
    print(f"    Employee profile embeddings: {emp_embeddings}")
    print(f"    Required profile embeddings: {req_embeddings}")
    print(f"    Total: {embeddings_count}")
    print(f"    (All auto-generated - 384 dimensions each)")
    
    print("\n" + "=" * 70)
    print("DEMO COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    print("\nNow run: python interactive_app.py")
    print("To use the interactive menu\n")
    
    # Cleanup
    project_service.close()
    employee_service.close()
    required_service.close()
    assignment_service.close()
    db.close()


if __name__ == "__main__":
    demo()
