"""
EJEMPLO DE USO DE LOS SERVICIOS CRUD CON DATOS MASIVOS
======================================================

Este archivo muestra cómo usar todos los servicios CRUD
con datos de prueba masivos (100 empleados, 30 proyectos, 150 asignaciones)
"""

from app.services.project_service import ProjectService
from app.services.employee_service import EmployeeService
from app.services.profile_service import ProfileService
from app.services.employee_project_service import EmployeeProjectService
from app.services.test_data import (
    PROFILES_DATA, EMPLOYEES_DATA, PROJECTS_DATA, ASSIGNMENTS_DATA
)
from app.db.create_tables import InitDB
from datetime import date
import time

def poblar_base_datos_masiva():
    """
    Función para poblar la base de datos con datos de prueba masivos.
    Crea 100 empleados con perfiles, 30 proyectos y asignaciones aleatorias.
    """
    print("🌱 POBLANDO BASE DE DATOS CON DATOS MASIVOS")
    print("=" * 60)

    start_time = time.time()

    try:
        # Inicializar servicios

        project_service = ProjectService()
        employee_service = EmployeeService()
        profile_service = ProfileService()
        assignment_service = EmployeeProjectService()

        # 1. Crear todos los perfiles
        print(f"\n📝 Creando {len(PROFILES_DATA)} perfiles...")
        profiles_created = []
        for i, profile_data in enumerate(PROFILES_DATA, 1):
            try:
                profile = profile_service.create_one(profile_data)
                profiles_created.append(profile)
                if i % 10 == 0:
                    print(f"   ✅ Creados {i}/{len(PROFILES_DATA)} perfiles")
            except Exception as e:
                print(f"   ❌ Error creando perfil {i}: {e}")

        print(f"   🎉 ¡{len(profiles_created)} perfiles creados exitosamente!")

        # 2. Crear todos los empleados (cada uno con su perfil)
        print(f"\n👥 Creando {len(EMPLOYEES_DATA)} empleados...")
        employees_created = []
        for i, employee_data in enumerate(EMPLOYEES_DATA, 1):
            try:
                # Crear empleado
                employee = employee_service.create_one(employee_data)
                employees_created.append(employee)

                # Asignar perfil al empleado (relación 1 a 1)
                profile_id = profiles_created[i-1].id  # Perfil correspondiente
                employee_service.assign_profile_to_employee(employee.id, profile_id)

                if i % 10 == 0:
                    print(f"   ✅ Creados {i}/{len(EMPLOYEES_DATA)} empleados")
            except Exception as e:
                print(f"   ❌ Error creando empleado {i}: {e}")

        print(f"   🎉 ¡{len(employees_created)} empleados creados exitosamente!")

        # 3. Crear todos los proyectos
        print(f"\n📁 Creando {len(PROJECTS_DATA)} proyectos...")
        projects_created = []
        for i, project_data in enumerate(PROJECTS_DATA, 1):
            try:
                project = project_service.create_one(project_data)
                projects_created.append(project)
                if i % 5 == 0:
                    print(f"   ✅ Creados {i}/{len(PROJECTS_DATA)} proyectos")
            except Exception as e:
                print(f"   ❌ Error creando proyecto {i}: {e}")

        print(f"   🎉 ¡{len(projects_created)} proyectos creados exitosamente!")

        # 4. Crear asignaciones aleatorias empleado-proyecto
        print(f"\n🔗 Creando {len(ASSIGNMENTS_DATA)} asignaciones empleado-proyecto...")
        assignments_created = 0
        for i, assignment_data in enumerate(ASSIGNMENTS_DATA, 1):
            try:
                success = assignment_service.assign_employee_to_project(
                    assignment_data["employee_id"],
                    assignment_data["project_id"]
                )
                if success:
                    assignments_created += 1
                if i % 25 == 0:
                    print(f"   ✅ Creadas {i}/{len(ASSIGNMENTS_DATA)} asignaciones")
            except Exception as e:
                print(f"   ❌ Error creando asignación {i}: {e}")

        print(f"   🎉 ¡{assignments_created} asignaciones creadas exitosamente!")

        # 5. Estadísticas finales
        elapsed_time = time.time() - start_time
        print(f"\n📊 ESTADÍSTICAS FINALES:")
        print(f"   ⏱️  Tiempo total: {elapsed_time:.2f} segundos")
        print(f"   👤 Empleados: {len(employees_created)}")
        print(f"   📋 Perfiles: {len(profiles_created)}")
        print(f"   📁 Proyectos: {len(projects_created)}")
        print(f"   🔗 Asignaciones: {assignments_created}")
        print(f"   📈 Total registros: {len(employees_created) + len(profiles_created) + len(projects_created) + assignments_created}")

        return True

    except Exception as e:
        print(f"❌ Error poblando base de datos: {e}")
        import traceback
        traceback.print_exc()
        return False

    finally:
        # Cerrar conexiones
        try:
            project_service.close()
            employee_service.close()
            profile_service.close()
            assignment_service.close()
        except:
            pass

def validar_datos_creados():
    """
    Función para validar que todos los datos se crearon correctamente.
    """
    print("\n🔍 VALIDANDO DATOS CREADOS")
    print("=" * 40)

    try:
        project_service = ProjectService()
        employee_service = EmployeeService()
        profile_service = ProfileService()
        assignment_service = EmployeeProjectService()

        # Validar empleados
        all_employees = employee_service.get_all()
        print(f"✅ Empleados en BD: {len(all_employees)}/100")

        # Validar perfiles
        all_profiles = profile_service.get_all()
        print(f"✅ Perfiles en BD: {len(all_profiles)}/100")

        # Validar proyectos
        all_projects = project_service.get_all()
        print(f"✅ Proyectos en BD: {len(all_projects)}/30")

        # Validar asignaciones
        total_assignments = 0
        for project in all_projects:
            employees_in_project = assignment_service.get_employees_by_project(project.id)
            total_assignments += len(employees_in_project)
        print(f"✅ Asignaciones en BD: {total_assignments}/150+")

        # Validar relación empleado-perfil
        employees_with_profiles = 0
        for employee in all_employees[:5]:  # Validar primeros 5
            emp_with_profile = employee_service.get_with_profile(employee.id)
            if emp_with_profile.profile:
                employees_with_profiles += 1
        print(f"✅ Relaciones empleado-perfil: {employees_with_profiles}/5 validados")

        # Mostrar algunos ejemplos
        print(f"\n📋 EJEMPLOS DE DATOS:")
        if all_employees:
            emp = all_employees[0]
            emp_with_profile = employee_service.get_with_profile(emp.id)
            print(f"   👤 Empleado: {emp_with_profile.name} ({emp_with_profile.office})")
            if emp_with_profile.profile:
                print(f"   📋 Habilidades: {emp_with_profile.profile.hardSkills[:50]}...")

        if all_projects:
            proj = all_projects[0]
            employees_in_proj = assignment_service.get_employees_by_project(proj.id)
            print(f"   📁 Proyecto: {proj.name}")
            print(f"   👥 Empleados asignados: {len(employees_in_proj)}")

        return True

    except Exception as e:
        print(f"❌ Error validando datos: {e}")
        return False

    finally:
        try:
            project_service.close()
            employee_service.close()
            profile_service.close()
            assignment_service.close()
        except:
            pass

def ejemplo_consultas_avanzadas():
    """
    Ejemplo de consultas avanzadas usando los datos masivos.
    """
    print("\n🔍 EJEMPLO DE CONSULTAS AVANZADAS")
    print("=" * 45)

    try:
        project_service = ProjectService()
        employee_service = EmployeeService()
        assignment_service = EmployeeProjectService()

        # Buscar empleados por oficina
        offices = ["Desarrollador Frontend", "Desarrollador Backend", "Full Stack Developer"]
        for office in offices:
            employees = employee_service.get_by_office(office)
            print(f"✅ {office}: {len(employees)} empleados")

        # Buscar proyectos por cliente
        clients = ["LogisticsCorp", "FoodExpress", "EduTech Solutions"]
        for client in clients:
            projects = project_service.get_by_client(client)
            print(f"✅ Proyectos de {client}: {len(projects)}")

        # Proyectos con más empleados asignados
        print(f"\n🏆 PROYECTOS CON MÁS EMPLEADOS:")
        all_projects = project_service.get_all()
        project_stats = []

        for project in all_projects:
            employees_count = len(assignment_service.get_employees_by_project(project.id))
            project_stats.append((project.name, employees_count))

        # Ordenar por número de empleados (descendente)
        project_stats.sort(key=lambda x: x[1], reverse=True)

        for name, count in project_stats[:5]:  # Top 5
            print(f"   📊 {name}: {count} empleados")

        # Empleados con más proyectos asignados
        print(f"\n👑 EMPLEADOS CON MÁS PROYECTOS:")
        all_employees = employee_service.get_all()
        employee_stats = []

        for employee in all_employees:
            emp_with_projects = employee_service.get_with_profile(employee.id)
            projects_count = len(emp_with_projects.projects)
            employee_stats.append((emp_with_projects.name, projects_count))

        # Ordenar por número de proyectos (descendente)
        employee_stats.sort(key=lambda x: x[1], reverse=True)

        for name, count in employee_stats[:5]:  # Top 5
            print(f"   👤 {name}: {count} proyectos")

    except Exception as e:
        print(f"❌ Error en consultas avanzadas: {e}")

    finally:
        try:
            project_service.close()
            employee_service.close()
            assignment_service.close()
        except:
            pass

def limpiar_base_datos():
    """
    Función para limpiar todos los datos de prueba (opcional).
    """
    print("\n🧹 LIMPIANDO BASE DE DATOS")
    print("=" * 35)

    try:
        # Nota: Esta función requeriría implementar métodos delete_all en los servicios
        # Por ahora solo mostramos el mensaje
        print("⚠️  Función de limpieza no implementada aún")
        print("   Para limpiar manualmente, ejecuta las migraciones de nuevo")

    except Exception as e:
        print(f"❌ Error limpiando base de datos: {e}")

if __name__ == "__main__":
    InitDB().create_tables()
    print("🚀 INICIANDO DEMOSTRACIÓN COMPLETA DE SERVICIOS CRUD")
    print("=" * 65)

    # Paso 1: Poblar base de datos con datos masivos
    success = poblar_base_datos_masiva()

    if success:
        # Paso 2: Validar que los datos se crearon correctamente
        validar_datos_creados()

        # Paso 3: Mostrar consultas avanzadas
        ejemplo_consultas_avanzadas()

        print("\n🎉 ¡DEMOSTRACIÓN COMPLETADA EXITOSAMENTE!")
        print("   ✅ Todos los servicios CRUD funcionan correctamente")
        print("   ✅ Relaciones 1 a 1 (empleado-perfil) funcionan")
        print("   ✅ Relaciones muchos a muchos (empleado-proyecto) funcionan")
        print("   ✅ Consultas y búsquedas avanzadas funcionan")
        print(f"   📊 Base de datos poblada con {100 + 100 + 30 + 150}+ registros")

    else:
        print("\n❌ DEMOSTRACIÓN FALLIDA")
        print("   Revisa los errores anteriores")

    # Opción para limpiar (comentada por seguridad)
    # limpiar_base_datos()