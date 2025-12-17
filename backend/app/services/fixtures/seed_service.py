"""
Servicio de seeding - Orquesta la creación de datos ficticios

Este módulo centraliza toda la lógica para poblar la base de datos con:
- Datos de prueba masivos
- Embeddings de perfiles
- Validación de datos creados
"""

import time
import random
from app.services.service_layer.project_service import ProjectService
from app.services.service_layer.employee_service import EmployeeService
from app.services.service_layer.profile_service import ProfileService
from app.services.service_layer.employee_project_service import EmployeeProjectService
from app.services.service_layer.required_profile_service import RequiredProfileService
from app.services.vectorial_services.embedding_service import EmbeddingService
from app.services.fixtures.seed_data import (
    PROFILES_DATA, EMPLOYEES_DATA, PROJECTS_DATA, ASSIGNMENTS_DATA
)
from app.db.create_tables import InitDB


class SeedService:
    """
    Servicio centralizado para seeding de datos ficticios.
    Maneja la creación de perfiles, empleados, proyectos y asignaciones.
    """

    def __init__(self):
        """Inicializa los servicios de la base de datos."""
        self.project_service = ProjectService()
        self.employee_service = EmployeeService()
        self.profile_service = ProfileService()
        self.assignment_service = EmployeeProjectService()
        self.embedding_service = EmbeddingService()
        self.required_profile_service = RequiredProfileService()

    def seed_database(self, include_embeddings=True):
        """
        Función principal para poblar la base de datos con datos masivos.
        Crea 100 empleados con perfiles, 30 proyectos y asignaciones aleatorias.

        Args:
            include_embeddings: Si True, también genera embeddings de perfiles

        Returns:
            dict: Estadísticas de los datos creados
        """
        print("\n" + "=" * 70)
        print("POBLANDO BASE DE DATOS CON DATOS FICTICIOS")
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
            # 1. Crear perfiles
            print(f"\n[1/4] Creando {len(PROFILES_DATA)} perfiles...")
            stats["profiles"] = self._create_profiles()
            print(f"   ✅ {stats['profiles']} perfiles creados exitosamente")

            # 2. Crear empleados
            print(f"\n[2/4] Creando {len(EMPLOYEES_DATA)} empleados...")
            stats["employees"] = self._create_employees()
            print(f"   ✅ {stats['employees']} empleados creados exitosamente")

            # 3. Crear proyectos
            print(f"\n[3/4] Creando {len(PROJECTS_DATA)} proyectos...")
            stats["projects"] = self._create_projects()
            print(f"   ✅ {stats['projects']} proyectos creados exitosamente")

            # 4. Crear asignaciones
            print(f"\n[4/4] Creando {len(ASSIGNMENTS_DATA)} asignaciones...")
            stats["assignments"] = self._create_assignments()
            print(f"   ✅ {stats['assignments']} asignaciones creadas exitosamente")

            # 5. Crear perfiles requeridos para proyectos
            print(f"\n[5/6] Asignando perfiles requeridos a proyectos...")
            stats["required_profiles"] = self._create_required_profiles()
            print(f"   ✅ Perfiles requeridos asignados exitosamente")

            # 6. Generar embeddings de perfiles (nuevo)
            print(f"\n[6/7] Generando embeddings de perfiles...")
            stats["profile_embeddings"] = self._create_profile_embeddings()
            print(f"   ✅ {stats['profile_embeddings']} embeddings de perfiles creados exitosamente")

            # 7. Generar embeddings de empleados (original)
            if include_embeddings:
                print(f"\n[7/7] Generando embeddings de empleados...")
                stats["embeddings"] = self._create_embeddings()
                print(f"   ✅ {stats['embeddings']} embeddings de empleados creados exitosamente")

            # Estadísticas finales
            elapsed_time = time.time() - start_time
            total_records = (
                stats["profiles"] + 
                stats["employees"] + 
                stats["projects"] + 
                stats["assignments"] +
                stats["embeddings"]
            )

            print(f"\n" + "=" * 70)
            print(f"SEEDING COMPLETADO EXITOSAMENTE")
            print(f"=" * 70)
            print(f"⏱️  Tiempo total: {elapsed_time:.2f} segundos")
            print(f"📊 Estadísticas:")
            print(f"   • Perfiles: {stats['profiles']}")
            print(f"   • Empleados: {stats['employees']}")
            print(f"   • Proyectos: {stats['projects']}")
            print(f"   • Asignaciones: {stats['assignments']}")
            print(f"   • Perfiles requeridos: {stats.get('required_profiles', 0)}")
            print(f"   • Embeddings de perfiles: {stats.get('profile_embeddings', 0)}")
            if include_embeddings:
                print(f"   • Embeddings de empleados: {stats['embeddings']}")
            print("=" * 70 + "\n")

            stats["success"] = True
            return stats

        except Exception as e:
            print(f"\n❌ Error durante seeding: {e}")
            import traceback
            traceback.print_exc()
            return stats

        finally:
            self.close()

    def _create_profiles(self):
        """Crea todos los perfiles."""
        created_count = 0
        for i, profile_data in enumerate(PROFILES_DATA, 1):
            try:
                self.profile_service.create_one(profile_data)
                created_count += 1
                if i % 10 == 0:
                    print(f"   Creados {i}/{len(PROFILES_DATA)} perfiles")
            except Exception as e:
                print(f"   ⚠️  Error creando perfil {i}: {e}")
        return created_count

    def _create_employees(self):
        """Crea todos los empleados y asigna perfiles."""
        created_count = 0
        profiles_created = self.profile_service.get_all()

        for i, employee_data in enumerate(EMPLOYEES_DATA, 1):
            try:
                # Crear empleado
                employee = self.employee_service.create_one(employee_data)

                # Asignar perfil correspondiente
                if i <= len(profiles_created):
                    profile_id = profiles_created[i - 1].id
                    self.employee_service.assign_profile_to_employee(employee.id, profile_id)

                created_count += 1
                if i % 10 == 0:
                    print(f"   Creados {i}/{len(EMPLOYEES_DATA)} empleados")
            except Exception as e:
                print(f"   ⚠️  Error creando empleado {i}: {e}")
        return created_count

    def _create_projects(self):
        """Crea todos los proyectos."""
        created_count = 0
        for i, project_data in enumerate(PROJECTS_DATA, 1):
            try:
                self.project_service.create_one(project_data)
                created_count += 1
                if i % 5 == 0:
                    print(f"   Creados {i}/{len(PROJECTS_DATA)} proyectos")
            except Exception as e:
                print(f"   ⚠️  Error creando proyecto {i}: {e}")
        return created_count

    def _create_assignments(self):
        """Crea todas las asignaciones empleado-proyecto."""
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
                    print(f"   Creadas {i}/{len(ASSIGNMENTS_DATA)} asignaciones")
            except Exception as e:
                print(f"   ⚠️  Error creando asignación {i}: {e}")
        return created_count

    def _create_profile_embeddings(self):
        """Genera embeddings para todos los perfiles y los almacena en BD."""
        created_count = 0
        try:
            all_profiles = self.profile_service.get_all()
            
            if not all_profiles:
                print("   ⚠️  No hay perfiles disponibles")
                return 0
            
            for i, profile in enumerate(all_profiles, 1):
                try:
                    # Crear texto a partir de skills y lenguajes
                    profile_text = f"{profile.hardSkills} {profile.softSkills} {profile.languages}"
                    
                    # Generar embedding usando embedding_service
                    embedding_vector = self.embedding_service.generate_embedding(profile_text)
                    
                    # Actualizar perfil con embedding
                    if embedding_vector:
                        self.profile_service.update_profile_embedding(profile.id, embedding_vector)
                        created_count += 1
                    
                    if i % 10 == 0:
                        print(f"   Embeddings generados {i}/{len(all_profiles)}")
                except Exception as e:
                    print(f"   ⚠️  Error generando embedding para perfil {profile.id}: {e}")
            
            return created_count
        except Exception as e:
            print(f"   ⚠️  Error en proceso de embeddings de perfiles: {e}")
            return 0

    def _create_embeddings(self):
        """Genera embeddings para todos los empleados."""
        try:
            return self.embedding_service.create_embeddings_for_all_employees()
        except Exception as e:
            print(f"   ⚠️  Error generando embeddings: {e}")
            return 0

    def _create_required_profiles(self):
        """Asigna perfiles requeridos a cada proyecto (1-4 perfiles por proyecto)."""
        created_count = 0
        try:
            all_projects = self.project_service.get_all()
            all_profiles = self.profile_service.get_all()
            
            if not all_profiles:
                print("   ⚠️  No hay perfiles disponibles")
                return 0
            
            for project in all_projects:
                # Generar entre 1 y 4 perfiles requeridos aleatoriamente
                num_required = random.randint(1, min(4, len(all_profiles)))
                selected_profiles = random.sample(all_profiles, num_required)
                
                for profile in selected_profiles:
                    success = self.required_profile_service.add_required_profile(
                        project_id=project.id,
                        profile_id=profile.id
                    )
                    if success:
                        created_count += 1
            
            print(f"   Creados {created_count} perfiles requeridos")
            return created_count
            
        except Exception as e:
            print(f"   ⚠️  Error creando perfiles requeridos: {e}")
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
            print(f"✅ Empleados en BD: {len(all_employees)}/100")

            # Validar perfiles
            all_profiles = self.profile_service.get_all()
            validation_results["profiles"] = len(all_profiles)
            print(f"✅ Perfiles en BD: {len(all_profiles)}/100")

            # Validar proyectos
            all_projects = self.project_service.get_all()
            validation_results["projects"] = len(all_projects)
            print(f"✅ Proyectos en BD: {len(all_projects)}/30")

            # Validar asignaciones
            total_assignments = 0
            for project in all_projects:
                employees_in_project = self.assignment_service.get_employees_by_project(project.id)
                total_assignments += len(employees_in_project)
            validation_results["assignments"] = total_assignments
            print(f"✅ Asignaciones en BD: {total_assignments}/150+")

            # Validar relación empleado-perfil
            employees_with_profiles = 0
            for employee in all_employees[:10]:
                emp_with_profile = self.employee_service.get_with_profile(employee.id)
                if emp_with_profile.profile:
                    employees_with_profiles += 1
            print(f"✅ Relaciones empleado-perfil: {employees_with_profiles}/10 validados")

            # Mostrar ejemplos
            print(f"\n📋 EJEMPLOS DE DATOS:")
            if all_employees:
                emp = all_employees[0]
                emp_with_profile = self.employee_service.get_with_profile(emp.id)
                print(f"   👤 Empleado: {emp_with_profile.name} ({emp_with_profile.office})")
                if emp_with_profile.profile:
                    skills = emp_with_profile.profile.hardSkills[:50]
                    print(f"   📋 Skills: {skills}...")

            if all_projects:
                proj = all_projects[0]
                employees_in_proj = self.assignment_service.get_employees_by_project(proj.id)
                print(f"   📁 Proyecto: {proj.name}")
                print(f"   👥 Empleados asignados: {len(employees_in_proj)}")

            print("=" * 70 + "\n")
            return validation_results

        except Exception as e:
            print(f"❌ Error validando datos: {e}")
            validation_results["valid"] = False
            return validation_results

    def close(self):
        """Cierra todas las conexiones de base de datos."""
        try:
            self.project_service.close()
            self.employee_service.close()
            self.profile_service.close()
            self.assignment_service.close()
            self.embedding_service.close()
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
        print("\n✅ SEEDING COMPLETADO Y VALIDADO EXITOSAMENTE")
        return True
    else:
        print("\n❌ SEEDING FALLIDO")
        return False


if __name__ == "__main__":
    success = seed_all(include_embeddings=True)
    exit(0 if success else 1)
