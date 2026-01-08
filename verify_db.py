import requests
import json

print('='*60)
print('VERIFICACIÓN DE DATOS EN LA BASE DE DATOS')
print('='*60)

try:
    # Proyectos
    print('\n[PROYECTOS]')
    response = requests.get('http://localhost:8000/api/projects')
    if response.status_code == 200:
        projects = response.json()
        print(f'Total: {len(projects)} proyectos')
        for p in projects[:3]:
            emp_count = len(p.get('employees', []))
            print(f'  ID {p["id"]}: {p["name"]} | Cliente: {p["client"]} | Empleados: {emp_count}')
    else:
        print(f'Error: {response.status_code}')

    # Empleados
    print('\n[EMPLEADOS]')
    response = requests.get('http://localhost:8000/api/employees')
    if response.status_code == 200:
        employees = response.json()
        print(f'Total: {len(employees)} empleados')
        for e in employees[:3]:
            proj_count = len(e.get('projects', []))
            print(f'  ID {e["id"]}: {e["name"]} | Oficina: {e.get("office", "N/A")} | Proyectos: {proj_count}')
    else:
        print(f'Error: {response.status_code}')

    # Required Profiles
    print('\n[PERFILES REQUERIDOS]')
    response = requests.get('http://localhost:8000/api/required-profiles')
    if response.status_code == 200:
        profiles = response.json()
        print(f'Total: {len(profiles)} perfiles requeridos')
        for p in profiles[:3]:
            skills = p.get('hard_skills', '')[:25]
            print(f'  ID {p["id"]}: Proyecto {p["project_id"]} | Skills: {skills}...')
    else:
        print(f'Error: {response.status_code}')

    print('\n' + '='*60)
    print('✓ Base de datos verificada correctamente')
    print('='*60)

except Exception as e:
    print(f'Error de conexión: {e}')
    print('Asegúrate de que el backend está ejecutándose en http://localhost:8000')
