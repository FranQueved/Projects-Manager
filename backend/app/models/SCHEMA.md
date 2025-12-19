# Esquema de Modelado de Datos

## Descripción General

Sistema de gestión de proyectos y asignación de empleados con búsqueda inteligente mediante embeddings vectoriales.

---

## Tablas y Modelos

### 1. **employees**
Almacena información de empleados.

| Campo | Tipo | Restricción | Descripción |
|-------|------|-------------|-------------|
| `id` | INT | PK, AUTO | Identificador único |
| `name` | VARCHAR(255) | NOT NULL, INDEX | Nombre completo del empleado |
| `office` | VARCHAR(255) | NULLABLE | Ubicación/oficina |
| `profile_id` | INT | FK → profiles, UNIQUE | Relación 1:1 con perfil |
| `created_at` | DATETIME | DEFAULT NOW() | Timestamp de creación |

**Relaciones:**
- [x] 1:1 con `profiles` (cada empleado tiene un perfil)
- [x] N:M con `projects` (vía tabla `employee_project`)

---

### 2. **profiles**
Almacena perfiles profesionales con competencias.

| Campo | Tipo | Restricción | Descripción |
|-------|------|-------------|-------------|
| `id` | INT | PK, AUTO | Identificador único |
| `hard_skills` | TEXT | NOT NULL | Habilidades técnicas (Python, SQL, Docker...) |
| `soft_skills` | TEXT | NOT NULL | Habilidades blandas (Liderazgo, Comunicación...) |
| `languages` | TEXT | NOT NULL | Idiomas dominados (Español, Inglés...) |
| `created_at` | DATETIME | DEFAULT NOW() | Timestamp de creación |

**Relaciones:**
- [x] 1:1 con `employees` (cada perfil pertenece a un empleado)
- [x] 1:N con `required_profiles` (un perfil puede ser requerido por múltiples proyectos)

---

### 3. **projects**
Almacena información de proyectos.

| Campo | Tipo | Restricción | Descripción |
|-------|------|-------------|-------------|
| `id` | INT | PK, AUTO | Identificador único |
| `name` | VARCHAR(255) | NOT NULL, INDEX | Nombre del proyecto |
| `description` | TEXT | NOT NULL | Descripción detallada |
| `client` | VARCHAR(255) | NOT NULL, INDEX, DEFAULT "Internal" | Cliente o empresa |
| `start_date` | DATE | NOT NULL | Fecha de inicio |
| `end_date` | DATE | NULLABLE | Fecha de finalización |
| `finished` | BOOLEAN | DEFAULT FALSE, INDEX | Estado de finalización |
| `budget` | INT | NOT NULL | Presupuesto en unidades monetarias |
| `presential` | BOOLEAN | DEFAULT FALSE | Requiere trabajo presencial |
| `created_at` | DATETIME | DEFAULT NOW() | Timestamp de creación |

**Relaciones:**
- [x] N:M con `employees` (vía tabla `employee_project`)
- [x] 1:N con `required_profiles` (cada proyecto puede requerir múltiples perfiles)

---

### 4. **required_profiles**
Relación N:M entre proyectos y perfiles requeridos.

| Campo | Tipo | Restricción | Descripción |
|-------|------|-------------|-------------|
| `id` | INT | PK, AUTO | Identificador único |
| `project_id` | INT | FK → projects, INDEX | Referencia al proyecto |
| `profile_id` | INT | FK → profiles, INDEX | Referencia al perfil requerido |
| `created_at` | DATETIME | DEFAULT NOW() | Timestamp de creación |

**Constraints:**
- [LOCK] UNIQUE(project_id, profile_id) - No duplicar combinaciones
- [DELETE] CASCADE ON DELETE - Al eliminar proyecto/perfil, se elimina el registro

**Relaciones:**
- [x] N:1 con `projects` (múltiples perfiles por proyecto)
- [x] N:1 con `profiles` (un perfil puede ser requerido por múltiples proyectos)

---

### 5. **employee_project**
Relación N:M entre empleados y proyectos.

| Campo | Tipo | Restricción | Descripción |
|-------|------|-------------|-------------|
| `employee_id` | INT | PK, FK → employees | Referencia al empleado |
| `project_id` | INT | PK, FK → projects | Referencia al proyecto |
| `assigned_at` | DATETIME | DEFAULT NOW() | Timestamp de asignación |

**Constraints:**
- [LOCK] PK COMPOSITE (employee_id, project_id)
- [DELETE] CASCADE ON DELETE - Al eliminar empleado/proyecto

**Relaciones:**
- [x] Tabla de unión N:M entre `employees` y `projects`

---

### 6. **embeddings**
Almacena embeddings vectoriales para búsqueda semántica.

| Campo | Tipo | Restricción | Descripción |
|-------|------|-------------|-------------|
| `id` | INT | PK, AUTO | Identificador único |
| `profile_id` | INT | FK → profiles, NULLABLE, INDEX | Embedding del perfil profesional |
| `required_profile_id` | INT | FK → required_profiles, NULLABLE, INDEX | Embedding del perfil requerido |
| `vector` | VECTOR(384) | NOT NULL, INDEX | Vector embedding pgvector (384 dims) |
| `created_at` | DATETIME | DEFAULT NOW() | Timestamp de creación |

**Notas:**
- Solo uno de `profile_id` o `required_profile_id` está lleno por registro
- Vector de 384 dimensiones generado con Sentence Transformers (all-MiniLM-L6-v2)
- Índice en `vector` para búsquedas rápidas de similitud

**Relaciones:**
- [x] N:1 con `profiles`
- [x] N:1 con `required_profiles`

---

## Diagrama de Relaciones

```
┌─────────────────────┐
│    EMPLOYEES        │
├─────────────────────┤
│ id (PK)             │
│ name                │
│ office              │◄────┐
│ profile_id (FK,U)   │─────┤ 1:1
│ created_at          │     │
└─────────────────────┘     │
                            │
                     ┌──────▼──────────┐
                     │   PROFILES      │
                     ├─────────────────┤
                     │ id (PK)         │
                     │ hard_skills     │
                     │ soft_skills     │
                     │ languages       │◄────────┐
                     │ created_at      │         │ 1:N
                     └─────────────────┘         │
                                         ┌───────▼──────────────┐
                                         │ REQUIRED_PROFILES    │
                                         ├──────────────────────┤
                                         │ id (PK)              │
                                         │ project_id (FK)      │─────┐
                                         │ profile_id (FK)      │     │
                                         │ created_at           │     │
                                         └──────────────────────┘     │
                                                                      │
┌────────────────────┐                                               │
│    PROJECTS        │◄──────────────────────────────────────────────┘
├────────────────────┤       1:N
│ id (PK)            │
│ name               │
│ description        │
│ client             │
│ start_date         │
│ end_date           │
│ finished           │
│ budget             │
│ presential         │
│ created_at         │
└────────┬───────────┘
         │ N:M
         │
    ┌────▼─────────────────────┐
    │  EMPLOYEE_PROJECT        │
    ├──────────────────────────┤
    │ employee_id (FK, PK)     │
    │ project_id (FK, PK)      │
    │ assigned_at              │
    └────┬─────────────────────┘
         │ N:M
         │
┌────────▼──────────────┐
│    EMPLOYEES          │
└───────────────────────┘

────────────────────────────────────────────────────────────

              ┌──────────────────────┐
              │    EMBEDDINGS        │
              ├──────────────────────┤
              │ id (PK)              │
              │ employee_id (FK)     │ ──► EMPLOYEES
              │ required_profile_id  │ ──► REQUIRED_PROFILES
              │ project_id (FK)      │ ──► PROJECTS
              │ vector (384 dims)    │
              │ created_at           │
              └──────────────────────┘
```

---

## Constraints y Validaciones

### Claves Primarias (PK)
- [x] `employees.id`
- [x] `profiles.id`
- [x] `projects.id`
- [x] `required_profiles.id`
- [x] `employee_project.(employee_id, project_id)` - Composite
- [x] `embeddings.id`

### Claves Foráneas (FK)
- [x] `employees.profile_id` → `profiles.id`
- [x] `required_profiles.project_id` → `projects.id`
- [x] `required_profiles.profile_id` → `profiles.id`
- [x] `employee_project.employee_id` → `employees.id`
- [x] `employee_project.project_id` → `projects.id`
- [x] `embeddings.employee_id` → `employees.id`
- [x] `embeddings.required_profile_id` → `required_profiles.id`
- [x] `embeddings.project_id` → `projects.id`

### Unique Constraints
- [x] `employees.profile_id` - Un empleado por perfil
- [x] `required_profiles.(project_id, profile_id)` - No duplicar requerimientos

### Índices para Búsquedas Rápidas
- [x] `employees.name`, `employees.profile_id`
- [x] `profiles.id`
- [x] `projects.name`, `projects.client`, `projects.finished`
- [x] `required_profiles.project_id`, `required_profiles.profile_id`
- [x] `embeddings.employee_id`, `embeddings.required_profile_id`, `embeddings.project_id`, `embeddings.vector`

---

## Cascadas y Eliminaciones

| Relación | ON DELETE |
|----------|-----------|
| `employees → profiles` | SET NULL |
| `required_profiles → projects` | CASCADE |
| `required_profiles → profiles` | CASCADE |
| `employee_project → employees` | CASCADE |
| `employee_project → projects` | CASCADE |
| `embeddings → employees` | CASCADE |
| `embeddings → required_profiles` | CASCADE |
| `embeddings → projects` | CASCADE |

---



## 🧮 Estadísticas de Prueba

| Métrica | Valor |
|---------|-------|
| Empleados | 100 |
| Perfiles | 100-110 |
| Proyectos | 30-50 |
| Asignaciones (media) | 4-5 por proyecto |
| Perfiles requeridos | 1-4 por proyecto |
| Embeddings generados | 300+ |
| Dimensiones de embedding | 384 (pgvector) |

---

## Seguridad y Validaciones

- [x] Todas las FK tienen índices para evitar scans full table
- [x] Cascadas configuradas correctamente para mantener integridad
- [x] UNIQUE constraints para evitar duplicados
- [x] Timestamps para auditoría
- [x] Valores NOT NULL donde es crítico
- [x] Límites de longitud en VARCHAR

---

## Notas de Implementación

1. **Embeddings**: Se generan usando Sentence Transformers (all-MiniLM-L6-v2)
2. **pgvector**: Requiere extensión PostgreSQL `pgvector`
3. **Timestamps**: Usar UTC siempre
4. **Soft Deletes**: No implementados, usar logical deletes si es necesario
5. **Auditoría**: Considerar agregar `updated_at` y `deleted_at` en el futuro

---

**Última actualización:** 19 de Diciembre, 2025  
**Versión del esquema:** 1.0
