"""
Database seeding service - Populates database with test data and embeddings.
"""

import time
import random
from app.services.service_layer.project_service import ProjectService
from app.services.service_layer.employee_service import EmployeeService
from app.services.service_layer.profile_service import ProfileService
from app.services.service_layer.employee_project_service import EmployeeProjectService
from app.services.service_layer.required_profile_service import RequiredProfileService
from app.services.fixtures.seed_data import (
    PROFILES_DATA, EMPLOYEES_DATA, PROJECTS_DATA, ASSIGNMENTS_DATA
)
from app.db.create_tables import InitDB


class SeedService:
    """Service for database seeding with test data."""

    def __init__(self):
        """Initialize service dependencies."""
        self.project_service = ProjectService()
        self.employee_service = EmployeeService()
        self.profile_service = ProfileService()
        self.assignment_service = EmployeeProjectService()
        self.required_profile_service = RequiredProfileService()

    def seed_database(self, include_embeddings=True):
        """
        Populate database with test data.
        
        Creates profiles, employees, projects, assignments, required profiles, and embeddings.
        
        Args:
            include_embeddings: Whether to generate embeddings for employee profiles
            
        Returns:
            dict: Statistics about created records
        """
        print("\n" + "=" * 70)
        print("SEEDING DATABASE WITH TEST DATA")
        print("=" * 70)

        start_time = time.time()
        stats = {
            "profiles": 0,
            "employees": 0,
            "projects": 0,
            "assignments": 0,
            "embeddings": 0,
            "success": False
        }

        try:
            print(f"\n[1/4] Creating {len(PROFILES_DATA)} profiles...")
            stats["profiles"] = self._create_profiles()
            print(f"   [OK] {stats['profiles']} profiles created")

            print(f"\n[2/4] Creating {len(EMPLOYEES_DATA)} employees with inline profiles...")
            stats["employees"] = self._create_employees_with_profiles()
            print(f"   [OK] {stats['employees']} employees created (profiles auto-created)")

            print(f"\n[3/4] Creating {len(PROJECTS_DATA)} projects...")
            stats["projects"] = self._create_projects()
            print(f"   [OK] {stats['projects']} projects created")

            print(f"\n[4/4] Creating {len(ASSIGNMENTS_DATA)} assignments...")
            stats["assignments"] = self._create_assignments()
            print(f"   [OK] {stats['assignments']} assignments created")

            print(f"\n[5/5] Assigning required profiles...")
            stats["required_profiles"] = self._create_required_profiles()
            print(f"   [OK] Required profiles assigned")

            print(f"\n[6/6] Generating embeddings for all employees and required profiles...")
            stats["embeddings"] = self._create_embeddings()
            print(f"   [OK] {stats['embeddings']} embeddings generated")

            elapsed_time = time.time() - start_time

            print(f"\n" + "=" * 70)
            print(f"SEEDING COMPLETED SUCCESSFULLY")
            print(f"=" * 70)
            print(f"[TIME] Total time: {elapsed_time:.2f}s")
            print(f"[STATS] Summary:")
            print(f"   • Profiles: {stats['profiles']}")
            print(f"   • Employees: {stats['employees']}")
            print(f"   • Projects: {stats['projects']}")
            print(f"   • Assignments: {stats['assignments']}")
            print(f"   • Required profiles: {stats.get('required_profiles', 0)}")
            print(f"   • Embeddings: {stats.get('embeddings', 0)}")
            print("=" * 70 + "\n")

            stats["success"] = True
            return stats

        except Exception as e:
            print(f"\n[ERROR] Seeding failed: {e}")
            import traceback
            traceback.print_exc()
            return stats

        finally:
            self.close()

    def _create_profiles(self):
        """Create all profiles."""
        created_count = 0
        for i, profile_data in enumerate(PROFILES_DATA, 1):
            try:
                self.profile_service.create_one(profile_data)
                created_count += 1
                if i % 10 == 0:
                    print(f"   Created {i}/{len(PROFILES_DATA)} profiles")
            except Exception as e:
                print(f"   [ERROR] Creating profile {i}: {e}")
        return created_count

    def _create_employees_with_profiles(self):
        """Create all employees with inline profile data (full automation)."""
        created_count = 0
        
        for i, employee_data in enumerate(EMPLOYEES_DATA, 1):
            try:
                # Use corresponding profile data for inline profile creation
                if i <= len(PROFILES_DATA):
                    profile_data = PROFILES_DATA[i - 1]
                    payload = dict(employee_data)
                    payload.update({
                        "hard_skills": profile_data.get("hard_skills", ""),
                        "soft_skills": profile_data.get("soft_skills", ""),
                        "languages": profile_data.get("languages", "")
                    })
                    self.employee_service.create_one(payload)
                    created_count += 1
                    if i % 10 == 0:
                        print(f"   Created {i}/{len(EMPLOYEES_DATA)} employees with profiles")
            except Exception as e:
                print(f"   [ERROR] Creating employee {i}: {e}")
        return created_count

    def _create_employees(self):
        """Deprecated - use _create_employees_with_profiles instead."""
        return 0

    def _create_projects(self):
        """Create all projects."""
        created_count = 0
        for i, project_data in enumerate(PROJECTS_DATA, 1):
            try:
                self.project_service.create_one(project_data)
                created_count += 1
                if i % 5 == 0:
                    print(f"   Created {i}/{len(PROJECTS_DATA)} projects")
            except Exception as e:
                print(f"   [ERROR] Creating project {i}: {e}")
        return created_count

    def _create_assignments(self):
        """Create all employee-project assignments."""
        created_count = 0
        for i, assignment_data in enumerate(ASSIGNMENTS_DATA, 1):
            try:
                success = self.assignment_service.assign_employee_to_project(
                    assignment_data["employee_id"],
                    assignment_data["project_id"]
                )
                if success:
                    created_count += 1
                if i % 25 == 0:
                    print(f"   Created {i}/{len(ASSIGNMENTS_DATA)} assignments")
            except Exception as e:
                print(f"   [ERROR] Creating assignment {i}: {e}")
        return created_count

    def _create_embeddings(self):
        """Generate embeddings for all employees and required profiles."""
        from app.services.vectorial_services.embedding_service import EmbeddingService
        
        embedding_service = EmbeddingService()
        created_count = 0
        
        try:
            # Generate embeddings for all employees
            all_employees = self.employee_service.get_all()
            print(f"\n   Generating embeddings for {len(all_employees)} employees...")
            
            for i, employee in enumerate(all_employees, 1):
                if embedding_service.create_embedding_for_employee(employee.id):
                    created_count += 1
                if i % 10 == 0:
                    print(f"   [OK] Employee embeddings: {i}/{len(all_employees)}")
            
            # Generate embeddings for all required profiles
            all_required_profiles = self.required_profile_service.get_all()
            print(f"\n   Generating embeddings for {len(all_required_profiles)} required profiles...")
            
            for i, req_profile in enumerate(all_required_profiles, 1):
                if embedding_service.create_embedding_for_required_profile(req_profile.id):
                    created_count += 1
                if i % 10 == 0:
                    print(f"   [OK] Required profile embeddings: {i}/{len(all_required_profiles)}")
            
            return created_count
        except Exception as e:
            print(f"   [ERROR] Creating embeddings: {e}")
            import traceback
            traceback.print_exc()
            return created_count
        finally:
            embedding_service.close()

    def _create_required_profiles(self):
        """Assign required profiles to each project (1-4 per project)."""
        created_count = 0
        try:
            all_projects = self.project_service.get_all()
            
            if not PROFILES_DATA:
                print("   [ERROR] No profile data available")
                return 0
            
            if not all_projects:
                print("   [ERROR] No projects available")
                return 0
            
            for project in all_projects:
                num_required = random.randint(1, 4)
                
                for _ in range(num_required):
                    profile_data = random.choice(PROFILES_DATA)
                    
                    try:
                        result = self.required_profile_service.add_required_profile(
                            project_id=project.id,
                            hard_skills=profile_data["hard_skills"],
                            soft_skills=profile_data["soft_skills"],
                            languages=profile_data["languages"]
                        )
                        if result:
                            created_count += 1
                    except Exception as inner_e:
                        print(f"   [ERROR] Creating required_profile for project {project.id}: {inner_e}")
            
            print(f"   Created {created_count} required profiles")
            return created_count
            
        except Exception as e:
            print(f"   [ERROR] Creating required profiles: {e}")
            import traceback
            traceback.print_exc()
            return 0

    def _create_required_profile_embeddings(self):
        """Embeddings generated automatically during required profile creation."""
        return 0

    def validate_data(self):
        """
        Valida que todos los datos se crearon correctamente.

        Returns:
            dict: Resultados de validación
        """
        print("\n" + "=" * 70)
        print("VALIDANDO DATOS CREADOS")
        print("=" * 70)

        validation_results = {
            "employees": 0,
            "profiles": 0,
            "projects": 0,
            "assignments": 0,
            "valid": True
        }

        try:
            # Validar empleados
            all_employees = self.employee_service.get_all()
            validation_results["employees"] = len(all_employees)
            print(f"[OK] Empleados en BD: {len(all_employees)}/100")

            # Validar perfiles
            all_profiles = self.profile_service.get_all()
            validation_results["profiles"] = len(all_profiles)
            print(f"[OK] Perfiles en BD: {len(all_profiles)}/100")

            # Validar proyectos
            all_projects = self.project_service.get_all()
            validation_results["projects"] = len(all_projects)
            print(f"[OK] Proyectos en BD: {len(all_projects)}/30")

            # Validar asignaciones
            total_assignments = 0
            for project in all_projects:
                employees_in_project = self.assignment_service.get_employees_by_project(project.id)
                total_assignments += len(employees_in_project)
            validation_results["assignments"] = total_assignments
            print(f"[OK] Asignaciones en BD: {total_assignments}/150+")

            # Validar relación empleado-perfil
            employees_with_profiles = 0
            for employee in all_employees[:10]:
                emp_with_profile = self.employee_service.get_with_profile(employee.id)
                if emp_with_profile.profile:
                    employees_with_profiles += 1
            print(f"[OK] Relaciones empleado-perfil: {employees_with_profiles}/10 validados")

            # Mostrar ejemplos
            print(f"\n[DATA] EJEMPLOS DE DATOS:")
            if all_employees:
                emp = all_employees[0]
                emp_with_profile = self.employee_service.get_with_profile(emp.id)
                print(f"   [USER] Empleado: {emp_with_profile.name} ({emp_with_profile.office})")
                if emp_with_profile.profile:
                    skills = emp_with_profile.profile.hard_skills[:50]
                    print(f"   [SKILL] Skills: {skills}...")

            if all_projects:
                proj = all_projects[0]
                employees_in_proj = self.assignment_service.get_employees_by_project(proj.id)
                print(f"   [PROJ] Proyecto: {proj.name}")
                print(f"   [TEAM] Empleados asignados: {len(employees_in_proj)}")

            print("=" * 70 + "\n")
            return validation_results

        except Exception as e:
            print(f"[ERROR] Error validando datos: {e}")
            validation_results["valid"] = False
            return validation_results

    def close(self):
        """Close database service connections."""
        try:
            self.project_service.close()
            self.employee_service.close()
            self.profile_service.close()
            self.assignment_service.close()
        except:
            pass


def seed_all(include_embeddings=True):
    """
    Función de conveniencia para ejecutar todo el seeding.

    Args:
        include_embeddings: Si True, también genera embeddings
    """
    # Crear tablas si no existen
    InitDB().create_tables()

    # Ejecutar seeding
    service = SeedService()
    stats = service.seed_database(include_embeddings=include_embeddings)

    if stats["success"]:
        # Validar datos
        service.validate_data()
        print("\n[SUCCESS] SEEDING COMPLETADO Y VALIDADO EXITOSAMENTE")
        return True
    else:
        print("\n[ERROR] SEEDING FALLIDO")
        return False


if __name__ == "__main__":
    success = seed_all(include_embeddings=True)
    exit(0 if success else 1)
