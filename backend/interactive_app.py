"""Interactive Application - Manage Projects, Employees, and Assignments."""

import os
import sys
from app.db.create_tables import InitDB
from app.services.service_layer.project_service import ProjectService
from app.services.service_layer.employee_service import EmployeeService
from app.services.service_layer.required_profile_service import RequiredProfileService
from app.services.service_layer.employee_project_service import EmployeeProjectService
from sqlalchemy import text
from app.db.database import SessionLocal


class InteractiveApp:
    """Interactive project management application."""

    def __init__(self):
        """Initialize services."""
        self.project_service = ProjectService()
        self.employee_service = EmployeeService()
        self.required_profile_service = RequiredProfileService()
        self.assignment_service = EmployeeProjectService()
        self.db = SessionLocal()

    def clear_screen(self):
        """Clear terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self, title: str):
        """Print formatted header."""
        print("\n" + "=" * 70)
        print(f"  {title.center(66)}")
        print("=" * 70)

    def print_menu(self):
        """Display main menu."""
        self.clear_screen()
        self.print_header("PROJECT MANAGER - INTERACTIVE APPLICATION")
        print("""
  [1] Create Project
  [2] Add Required Profile to Project
  [3] Create Employee (with automatic profile)
  [4] Assign Employee to Project
  [5] View All Projects
  [6] View All Employees
  [7] View Project Details
  [8] View Employee Details
  [9] View Database Statistics
  [0] Exit

""")

    def create_project(self):
        """Create a new project."""
        self.clear_screen()
        self.print_header("CREATE NEW PROJECT")
        
        try:
            name = input("\n  Project name: ").strip()
            if not name:
                print("  ✗ Project name cannot be empty")
                input("\n  Press Enter to continue...")
                return
            
            description = input("  Project description: ").strip()
            
            project = self.project_service.create_one({
                "name": name,
                "description": description
            })
            
            print(f"\n  ✓ Project created successfully!")
            print(f"    ID: {project.id}")
            print(f"    Name: {project.name}")
            print(f"    Description: {project.description}")
            
        except Exception as e:
            print(f"\n  ✗ Error creating project: {e}")
        
        input("\n  Press Enter to continue...")

    def add_required_profile(self):
        """Add required profile to a project."""
        self.clear_screen()
        self.print_header("ADD REQUIRED PROFILE TO PROJECT")
        
        try:
            # Show available projects
            projects = self.project_service.get_all()
            if not projects:
                print("\n  ✗ No projects found. Create a project first.")
                input("\n  Press Enter to continue...")
                return
            
            print("\n  Available Projects:")
            for p in projects:
                print(f"    [{p.id}] {p.name}")
            
            project_id = input("\n  Select project ID: ").strip()
            try:
                project_id = int(project_id)
            except ValueError:
                print("  ✗ Invalid project ID")
                input("\n  Press Enter to continue...")
                return
            
            project = self.project_service.get_by_id(project_id)
            if not project:
                print("  ✗ Project not found")
                input("\n  Press Enter to continue...")
                return
            
            # Get profile requirements
            print(f"\n  Adding required profile to: {project.name}")
            hard_skills = input("  Hard skills (e.g., Python, Django, PostgreSQL): ").strip()
            soft_skills = input("  Soft skills (e.g., Problem solving, Communication): ").strip()
            languages = input("  Languages (e.g., English, Spanish): ").strip()
            
            req_profile = self.required_profile_service.add_required_profile(
                project_id=project_id,
                hard_skills=hard_skills,
                soft_skills=soft_skills,
                languages=languages
            )
            
            print(f"\n  ✓ Required profile added successfully!")
            print(f"    ID: {req_profile.id}")
            print(f"    Hard skills: {req_profile.hard_skills}")
            print(f"    Soft skills: {req_profile.soft_skills}")
            print(f"    Languages: {req_profile.languages}")
            print(f"    (Embedding auto-generated)")
            
        except Exception as e:
            print(f"\n  ✗ Error adding required profile: {e}")
        
        input("\n  Press Enter to continue...")

    def create_employee(self):
        """Create a new employee with automatic profile."""
        self.clear_screen()
        self.print_header("CREATE NEW EMPLOYEE (with automatic profile)")
        
        try:
            name = input("\n  Employee name: ").strip()
            if not name:
                print("  ✗ Name cannot be empty")
                input("\n  Press Enter to continue...")
                return
            
            office = input("  Office location (e.g., Madrid, Barcelona): ").strip()
            
            print("\n  Profile information (will be created automatically):")
            hard_skills = input("  Hard skills (e.g., Python, Django, PostgreSQL): ").strip()
            soft_skills = input("  Soft skills (e.g., Problem solving, Communication): ").strip()
            languages = input("  Languages (e.g., English, Spanish): ").strip()
            
            if not hard_skills and not soft_skills and not languages:
                print("  ✗ At least one profile field is required")
                input("\n  Press Enter to continue...")
                return
            
            employee = self.employee_service.create_one({
                "name": name,
                "office": office,
                "hard_skills": hard_skills,
                "soft_skills": soft_skills,
                "languages": languages
            })
            
            print(f"\n  ✓ Employee created successfully!")
            print(f"    ID: {employee.id}")
            print(f"    Name: {employee.name}")
            print(f"    Office: {employee.office}")
            print(f"    Profile ID: {employee.profile_id}")
            print(f"    (Profile created automatically)")
            print(f"    (Embedding generated automatically)")
            
        except Exception as e:
            print(f"\n  ✗ Error creating employee: {e}")
        
        input("\n  Press Enter to continue...")

    def assign_employee(self):
        """Assign employee to project."""
        self.clear_screen()
        self.print_header("ASSIGN EMPLOYEE TO PROJECT")
        
        try:
            # Show available employees
            employees = self.employee_service.get_all()
            if not employees:
                print("\n  ✗ No employees found. Create an employee first.")
                input("\n  Press Enter to continue...")
                return
            
            print("\n  Available Employees:")
            for e in employees:
                print(f"    [{e.id}] {e.name} ({e.office})")
            
            employee_id = input("\n  Select employee ID: ").strip()
            try:
                employee_id = int(employee_id)
            except ValueError:
                print("  ✗ Invalid employee ID")
                input("\n  Press Enter to continue...")
                return
            
            employee = self.employee_service.get_by_id(employee_id)
            if not employee:
                print("  ✗ Employee not found")
                input("\n  Press Enter to continue...")
                return
            
            # Show available projects
            projects = self.project_service.get_all()
            if not projects:
                print("\n  ✗ No projects found. Create a project first.")
                input("\n  Press Enter to continue...")
                return
            
            print(f"\n  Available Projects:")
            for p in projects:
                print(f"    [{p.id}] {p.name}")
            
            project_id = input("\n  Select project ID: ").strip()
            try:
                project_id = int(project_id)
            except ValueError:
                print("  ✗ Invalid project ID")
                input("\n  Press Enter to continue...")
                return
            
            project = self.project_service.get_by_id(project_id)
            if not project:
                print("  ✗ Project not found")
                input("\n  Press Enter to continue...")
                return
            
            # Assign
            success = self.assignment_service.assign_employee_to_project(
                employee_id=employee_id,
                project_id=project_id
            )
            
            if success:
                print(f"\n  ✓ Assignment successful!")
                print(f"    Employee: {employee.name}")
                print(f"    Project: {project.name}")
            else:
                print(f"\n  ✗ Assignment failed (may already exist)")
            
        except Exception as e:
            print(f"\n  ✗ Error assigning employee: {e}")
        
        input("\n  Press Enter to continue...")

    def view_projects(self):
        """View all projects."""
        self.clear_screen()
        self.print_header("ALL PROJECTS")
        
        try:
            projects = self.project_service.get_all()
            
            if not projects:
                print("\n  No projects found.")
            else:
                print(f"\n  Total projects: {len(projects)}\n")
                for i, p in enumerate(projects, 1):
                    print(f"  [{p.id}] {p.name}")
                    print(f"      Description: {p.description}")
                    print()
            
        except Exception as e:
            print(f"\n  ✗ Error loading projects: {e}")
        
        input("\n  Press Enter to continue...")

    def view_employees(self):
        """View all employees."""
        self.clear_screen()
        self.print_header("ALL EMPLOYEES")
        
        try:
            employees = self.employee_service.get_all()
            
            if not employees:
                print("\n  No employees found.")
            else:
                print(f"\n  Total employees: {len(employees)}\n")
                for e in employees:
                    profile_info = f"Profile ID: {e.profile_id}"
                    print(f"  [{e.id}] {e.name}")
                    print(f"      Office: {e.office}")
                    print(f"      {profile_info}")
                    print()
            
        except Exception as e:
            print(f"\n  ✗ Error loading employees: {e}")
        
        input("\n  Press Enter to continue...")

    def view_project_details(self):
        """View project with assignments and required profiles."""
        self.clear_screen()
        self.print_header("PROJECT DETAILS")
        
        try:
            projects = self.project_service.get_all()
            if not projects:
                print("\n  No projects found.")
                input("\n  Press Enter to continue...")
                return
            
            print("\n  Available Projects:")
            for p in projects:
                print(f"    [{p.id}] {p.name}")
            
            project_id = input("\n  Select project ID: ").strip()
            try:
                project_id = int(project_id)
            except ValueError:
                print("  ✗ Invalid project ID")
                input("\n  Press Enter to continue...")
                return
            
            project = self.project_service.get_by_id(project_id)
            if not project:
                print("  ✗ Project not found")
                input("\n  Press Enter to continue...")
                return
            
            print(f"\n  Project: {project.name}")
            print(f"  Description: {project.description}")
            
            # Assigned employees
            employees = self.assignment_service.get_employees_by_project(project_id)
            print(f"\n  Assigned Employees ({len(employees)}):")
            if employees:
                for e in employees:
                    print(f"    - {e.name} ({e.office})")
            else:
                print("    None")
            
            # Required profiles
            req_profiles = self.required_profile_service.get_required_profiles_for_project(project_id)
            print(f"\n  Required Profiles ({len(req_profiles)}):")
            if req_profiles:
                for rp in req_profiles:
                    print(f"    - Hard skills: {rp.hard_skills}")
                    print(f"      Soft skills: {rp.soft_skills}")
                    print(f"      Languages: {rp.languages}")
            else:
                print("    None")
            
        except Exception as e:
            print(f"\n  ✗ Error loading project details: {e}")
        
        input("\n  Press Enter to continue...")

    def view_employee_details(self):
        """View employee with profile and assignments."""
        self.clear_screen()
        self.print_header("EMPLOYEE DETAILS")
        
        try:
            employees = self.employee_service.get_all()
            if not employees:
                print("\n  No employees found.")
                input("\n  Press Enter to continue...")
                return
            
            print("\n  Available Employees:")
            for e in employees:
                print(f"    [{e.id}] {e.name}")
            
            employee_id = input("\n  Select employee ID: ").strip()
            try:
                employee_id = int(employee_id)
            except ValueError:
                print("  ✗ Invalid employee ID")
                input("\n  Press Enter to continue...")
                return
            
            employee = self.employee_service.get_by_id(employee_id)
            if not employee:
                print("  ✗ Employee not found")
                input("\n  Press Enter to continue...")
                return
            
            print(f"\n  Employee: {employee.name}")
            print(f"  Office: {employee.office}")
            
            # Profile information
            if employee.profile:
                profile = employee.profile
                print(f"\n  Profile (ID {profile.id}):")
                print(f"    Hard skills: {profile.hard_skills}")
                print(f"    Soft skills: {profile.soft_skills}")
                print(f"    Languages: {profile.languages}")
            
            # Projects assigned
            projects = self.assignment_service.get_projects_by_employee(employee_id)
            print(f"\n  Assigned Projects ({len(projects)}):")
            if projects:
                for p in projects:
                    print(f"    - {p.name}")
            else:
                print("    None")
            
        except Exception as e:
            print(f"\n  ✗ Error loading employee details: {e}")
        
        input("\n  Press Enter to continue...")

    def view_statistics(self):
        """View database statistics."""
        self.clear_screen()
        self.print_header("DATABASE STATISTICS")
        
        try:
            # Count records
            projects_count = self.db.execute(text("SELECT COUNT(*) FROM projects")).scalar()
            employees_count = self.db.execute(text("SELECT COUNT(*) FROM employees")).scalar()
            profiles_count = self.db.execute(text("SELECT COUNT(*) FROM profiles")).scalar()
            embeddings_count = self.db.execute(text("SELECT COUNT(*) FROM embeddings")).scalar()
            assignments_count = self.db.execute(
                text("SELECT COUNT(*) FROM employee_project")
            ).scalar()
            required_profiles_count = self.db.execute(
                text("SELECT COUNT(*) FROM required_profiles")
            ).scalar()
            
            print(f"""
  Database Records:
  
  Projects:               {projects_count}
  Employees:             {employees_count}
  Profiles:              {profiles_count}
  Required Profiles:     {required_profiles_count}
  Embeddings:            {embeddings_count}
  Assignments:           {assignments_count}
  
  Embeddings per type:
    - Employee profiles: {self.db.execute(text('SELECT COUNT(*) FROM embeddings WHERE profile_id IS NOT NULL')).scalar()}
    - Required profiles: {self.db.execute(text('SELECT COUNT(*) FROM embeddings WHERE required_profile_id IS NOT NULL')).scalar()}
""")
            
        except Exception as e:
            print(f"\n  ✗ Error loading statistics: {e}")
        
        input("\n  Press Enter to continue...")

    def run(self):
        """Run the application."""
        # Initialize database
        print("\nInitializing database...")
        InitDB().create_tables()
        print("✓ Database initialized\n")
        
        while True:
            self.print_menu()
            choice = input("  Select option: ").strip()
            
            if choice == "1":
                self.create_project()
            elif choice == "2":
                self.add_required_profile()
            elif choice == "3":
                self.create_employee()
            elif choice == "4":
                self.assign_employee()
            elif choice == "5":
                self.view_projects()
            elif choice == "6":
                self.view_employees()
            elif choice == "7":
                self.view_project_details()
            elif choice == "8":
                self.view_employee_details()
            elif choice == "9":
                self.view_statistics()
            elif choice == "0":
                print("\n  Closing application...")
                self.close()
                break
            else:
                print("\n  ✗ Invalid option. Try again.")
                input("\n  Press Enter to continue...")

    def close(self):
        """Close services."""
        try:
            self.project_service.close()
            self.employee_service.close()
            self.required_profile_service.close()
            self.assignment_service.close()
            self.db.close()
        except:
            pass


if __name__ == "__main__":
    app = InteractiveApp()
    app.run()
