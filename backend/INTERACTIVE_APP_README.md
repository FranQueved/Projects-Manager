"""Interactive Project Manager Application

## Descripción

Aplicación interactiva por terminal para gestionar:
- Proyectos
- Empleados (con perfiles automáticos)
- Perfiles requeridos para proyectos
- Asignaciones de empleados a proyectos

TODO se guarda automáticamente en la base de datos PostgreSQL.

## Características

✅ Crear proyectos
✅ Agregar perfiles requeridos a proyectos
✅ Crear empleados (con perfiles automáticos)
✅ Asignar empleados a proyectos
✅ Ver detalles de proyectos y empleados
✅ Ver estadísticas de base de datos
✅ Embeddings generados automáticamente

## Instalación

### 1. Dependencias

```bash
pip install -r requirements.txt
```

### 2. Base de datos

```bash
# Asegurate de que PostgreSQL está corriendo
# La aplicación crea las tablas automáticamente
```

### 3. Variables de entorno

```bash
# Configurar en .env o en las variables de entorno:
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/projects_manager
```

## Uso

### Ejecutar la aplicación:

```bash
python interactive_app.py
```

O desde la raíz del proyecto:

```bash
python backend/interactive_app.py
```

### Menú Principal

```
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
```

## Flujo de trabajo recomendado

### 1️⃣ Crear proyectos
- Opción [1]
- Ingresa nombre y descripción

### 2️⃣ Agregar perfiles requeridos
- Opción [2]
- Selecciona proyecto
- Ingresa skills, soft skills, idiomas
- ✓ Embedding generado automáticamente

### 3️⃣ Crear empleados
- Opción [3]
- Ingresa nombre, oficina, skills
- ✓ Perfil creado automáticamente
- ✓ Embedding generado automáticamente

### 4️⃣ Asignar empleados a proyectos
- Opción [4]
- Selecciona empleado
- Selecciona proyecto
- ✓ Asignación guardada en BD

### 5️⃣ Ver detalles
- Opción [7] para proyectos
- Opción [8] para empleados
- Ve toda la información conectada

## Automatización

### Creación de Empleados

```
Input:
{
    "name": "Juan García",
    "office": "Madrid",
    "hard_skills": "Python, Django",
    "soft_skills": "Problem solving",
    "languages": "English"
}

Automático:
✓ Perfil creado
✓ Empleado creado
✓ Embedding generado (384 dimensiones)
✓ Guardado en BD
```

### Creación de Perfiles Requeridos

```
Input:
{
    "project_id": 1,
    "hard_skills": "Python, Machine Learning",
    "soft_skills": "Innovation",
    "languages": "English"
}

Automático:
✓ Perfil requerido creado
✓ Embedding generado (384 dimensiones)
✓ Guardado en BD
```

## Base de Datos

### Tablas principales:

```
profiles
├─ id
├─ hard_skills
├─ soft_skills
└─ languages

employees
├─ id
├─ name
├─ office
└─ profile_id (FK)

projects
├─ id
├─ name
└─ description

required_profiles
├─ id
├─ project_id (FK)
├─ hard_skills
├─ soft_skills
└─ languages

employee_project (M-to-N)
├─ employee_id (FK)
└─ project_id (FK)

embeddings
├─ id
├─ profile_id (FK)
├─ required_profile_id (FK)
├─ vector (384 dimensiones)
└─ created_at
```

## Estadísticas

La opción [9] muestra:
- Total de proyectos
- Total de empleados
- Total de perfiles
- Total de perfiles requeridos
- Total de embeddings
- Total de asignaciones
- Desglose de embeddings (empleados vs. perfiles requeridos)

## Ejemplo de sesión

```
== PROJECT MANAGER - INTERACTIVE APPLICATION ==

[1] Create Project
> Nombre: AI Platform
> Descripción: Machine learning platform
✓ Proyecto creado: ID 1

[3] Create Employee
> Nombre: Juan García
> Oficina: Madrid
> Hard skills: Python, TensorFlow
> Soft skills: Machine Learning, Problem solving
> Idiomas: English, Spanish
✓ Empleado creado: ID 1
✓ Perfil creado automáticamente: ID 1
✓ Embedding generado automáticamente

[2] Add Required Profile to Project
> Proyecto: AI Platform (ID 1)
> Hard skills: Python, PyTorch
> Soft skills: Innovation, Analysis
> Idiomas: English
✓ Perfil requerido agregado: ID 1
✓ Embedding generado automáticamente

[4] Assign Employee to Project
> Empleado: Juan García (ID 1)
> Proyecto: AI Platform (ID 1)
✓ Asignación completada

[7] View Project Details
> AI Platform
> Empleados asignados: 1 (Juan García)
> Perfiles requeridos: 1

[9] View Database Statistics
> Proyectos: 1
> Empleados: 1
> Perfiles: 1
> Embeddings: 2 (1 empleado + 1 requerido)
> Asignaciones: 1
```

## Troubleshooting

### Error: "No projects found"
- Crea un proyecto primero (opción 1)

### Error: "No employees found"
- Crea un empleado primero (opción 3)

### Error: "Database connection failed"
- Verifica que PostgreSQL está corriendo
- Verifica la DATABASE_URL en variables de entorno

### Error al asignar empleado a proyecto
- Asegúrate de que ambos existen
- Puede que ya esté asignado

## Notas

- Todos los cambios se guardan **inmediatamente** en la BD
- Los embeddings se generan automáticamente (Sentence Transformers 384-dim)
- No necesitas hacer nada especial para embeddings - todo es automático
- La aplicación es completamente interactiva y amigable

## Próximos pasos

Después de crear datos, puedes:
- Usar la API REST en FastAPI para consultas
- Ejecutar búsquedas de similaridad vectorial
- Exportar datos a reportes
- Integrar con otros servicios
"""
