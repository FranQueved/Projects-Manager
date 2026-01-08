# 🏗️ Arquitectura del Sistema



```
┌─────────────────────────────────────────────────────────────┐
│                     FRONTEND (React)                        │
│  - Dashboard interactivo                                    │
│  - Gestión de empleados y proyectos                         │
│  - Sistema de recomendaciones visualizado                   │
└──────────────────┬──────────────────────────────────────────┘
                   │ HTTP/REST (Axios)
                   ▼
┌─────────────────────────────────────────────────────────────┐
│                   BACKEND (FastAPI)                         │
│  - API REST con 5 routers principales                       │
│  - Validación de datos (Pydantic)                           │
│  - Lógica de recomendaciones                                │
│  - Generación de embeddings                                 │
└──────────────────┬──────────────────────────────────────────┘
                   │ SQLAlchemy ORM
                   ▼
┌─────────────────────────────────────────────────────────────┐
│              BASE DE DATOS (PostgreSQL)                     │
│  - 6 tablas principales                                     │
│  - Extension pgvector para búsqueda semántica               │
│  - Indexes para optimización                                │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Flujo de Datos

### 1. Crear Empleado
```
Frontend (Form) 
    ↓
POST /api/employees 
    ↓
Backend: Crear Employee + Profile + Embedding
    ↓
PostgreSQL: Guardar en DB
    ↓
Response JSON al Frontend
```

### 2. Sistema de Recomendaciones
```
Usuario selecciona proyecto
    ↓
Frontend: Obtiene required_profiles del proyecto
    ↓
GET /api/recommendations/required-profile/{id}
    ↓
Backend:
  1. Obtiene embedding del required_profile
  2. Busca todos los embeddings de empleados
  3. Calcula similitud (cosine similarity)
  4. Ordena por puntuación
    ↓
Response: Lista de empleados ordenados por match
    ↓
Frontend: Muestra recomendaciones
```

---

## 📦 Componentes Principales

### Backend - Estructura de Directorios

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Aplicación FastAPI principal
│   │
│   ├── db/                      # Configuración BD
│   │   ├── database.py          # Conexión PostgreSQL
│   │   └── create_tables.py     # Inicialización de tablas
│   │
│   ├── models/                  # Modelos SQLAlchemy (ORM)
│   │   ├── employee.py
│   │   ├── profile.py
│   │   ├── project.py
│   │   ├── required_profile.py
│   │   ├── embedding.py
│   │   └── employee_project.py
│   │
│   ├── schemas/                 # Schemas Pydantic (validación)
│   │   ├── employee.py
│   │   ├── profile.py
│   │   └── project.py
│   │
│   ├── routers/                 # API Endpoints (FastAPI)
│   │   ├── employees.py         # CRUD empleados
│   │   ├── projects.py          # CRUD proyectos
│   │   ├── assignments.py       # Asignaciones E-P
│   │   ├── required_profiles.py # Perfiles requeridos
│   │   └── recommendations.py   # Sistema IA
│   │
│   └── services/                # Servicios
│       └── vectorial_services/
│           ├── embedding_service.py       # Generación embeddings
│           ├── embedding_comparation.py   # Comparación vectores
│           └── embeding_creator.py        # Carga modelo IA
│
├── requirements.txt             # Dependencias Python
├── populate_db.py               # Script para llenar BD
└── reset_db.py                  # Script para resetear BD
```

### Frontend - Estructura React

```
frontend/
├── src/
│   ├── App.jsx                  # Componente raíz
│   ├── index.jsx                # Entry point
│   │
│   ├── components/              # Componentes reutilizables
│   │   ├── Table.jsx
│   │   ├── Form.jsx
│   │   ├── Modal.jsx
│   │   ├── Button.jsx
│   │   ├── Card.jsx
│   │   ├── Alert.jsx
│   │   └── Loading.jsx
│   │
│   ├── pages/                   # Páginas
│   │   ├── Home.jsx             # Dashboard principal
│   │   ├── Employees.jsx        # Gestión empleados
│   │   ├── Projects.jsx         # Gestión proyectos
│   │   └── Dashboard.jsx        # Analytics
│   │
│   ├── services/                # Comunicación con API
│   │   ├── api.js               # Cliente Axios
│   │   └── dataService.js       # Métodos por entidad
│   │
│   ├── context/                 # State Management
│   │   └── AppContext.jsx       # Zustand store
│   │
│   ├── hooks/                   # Custom hooks
│   │   └── useFetch.js          # Fetch data
│   │
│   └── styles/                  # CSS
│       └── *.css
│
└── public/
    └── index.html
```

---

## 🔌 Routers y Endpoints

### 5 Routers Principales

#### 1. **Employees Router** (`/api/employees`)
```
GET    /api/employees              → Listar todos
GET    /api/employees/{id}         → Obtener por ID
POST   /api/employees              → Crear nuevo
PUT    /api/employees/{id}         → Actualizar
DELETE /api/employees/{id}         → Eliminar
```

#### 2. **Projects Router** (`/api/projects`)
```
GET    /api/projects               → Listar todos
GET    /api/projects/{id}          → Obtener por ID
POST   /api/projects               → Crear nuevo
PUT    /api/projects/{id}          → Actualizar
DELETE /api/projects/{id}          → Eliminar
```

#### 3. **Assignments Router** (`/api/assignments`)
```
POST   /api/assignments/assign/{emp_id}/{proj_id}
DELETE /api/assignments/unassign/{emp_id}/{proj_id}
GET    /api/assignments/project/{proj_id}
GET    /api/assignments/employee/{emp_id}
```

#### 4. **Required Profiles Router** (`/api/required-profiles`)
```
GET    /api/required-profiles/project/{proj_id}
GET    /api/required-profiles/{id}
POST   /api/required-profiles
PUT    /api/required-profiles/{id}
DELETE /api/required-profiles/{id}
```

#### 5. **Recommendations Router** (`/api/recommendations`)
```
GET    /api/recommendations/employees/{proj_id}
GET    /api/recommendations/required-profile/{req_prof_id}
```

---

## 💡 Características Clave

### 1. CORS (Cross-Origin Resource Sharing)
```python
# Permite comunicación entre frontend (3000) y backend (8000)
allow_origins = [
    "http://localhost:3000",
    "http://localhost:5173"
]
```

### 2. Validación Automática (Pydantic)
```python
# Todos los requests se validan automáticamente
class EmployeeCreate(BaseModel):
    name: str
    office: str
    hard_skills: str = ""
    soft_skills: str = ""
    languages: str = ""
```

### 3. Documentación Automática
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

---

## 🚀 Pipeline de Inicio

### Backend
```
1. main.py inicia FastAPI
2. Carga middlewares (CORS)
3. Registra routers (/api/*)
4. Inicia Uvicorn en puerto 8000
5. PostgreSQL conexión automática (SessionLocal)
```

### Frontend
```
1. index.jsx monta App en #root
2. AppContext (Zustand) inicializa estado
3. React Router configura rutas
4. Carga página Home/Dashboard
5. Axios interceptores listos para requests
```

---

## 🔐 Validación y Errores

### Flujo de Validación
```
Request HTTP
    ↓
FastAPI middleware (CORS, headers)
    ↓
Pydantic schema validation
    ↓
Endpoint handler
    ↓
SQLAlchemy ORM operations
    ↓
PostgreSQL execute
    ↓
Response JSON
```

### Códigos HTTP Retornados
| Código | Significado |
|--------|------------|
| `200` | OK - Éxito |
| `201` | Created - Recurso creado |
| `400` | Bad Request - Validación fallida |
| `404` | Not Found - Recurso no existe |
| `500` | Server Error - Error interno |

---

## 📊 Optimizaciones

### Base de Datos
- **Indexes** en campos frecuentemente buscados (name, client, finished)
- **Foreign Keys** con cascadas automáticas
- **pgvector** optimizado para búsqueda de vectores
- **Unique Constraints** en relaciones 1:1

### Backend
- **Connection Pooling**: SQLAlchemy maneja múltiples conexiones
- **Lazy Loading**: Relaciones cargadas bajo demanda
- **Caching**: Posibilidad de implementar Redis

### Frontend
- **Code Splitting**: React Router con lazy loading
- **Memoization**: Componentes optimizados con React.memo
- **HTTP Caching**: Axios con etags

---

## 🔄 Ciclo de Vida de una Solicitud

```
1. FRONTEND
   └─ Usuario hace acción (ej: crear empleado)
      └─ Dispara evento onChange en Form
         └─ AppContext actualiza estado local
            └─ Click en "Guardar"
               └─ employeeService.create(data)

2. HTTP REQUEST
   └─ Axios POST /api/employees
      └─ Headers: Content-Type application/json, CORS headers
         └─ Body: JSON con datos validados localmente

3. BACKEND
   └─ FastAPI recibe request
      └─ CORS middleware verifica origen
         └─ Router employees.py maneja POST
            └─ Pydantic valida schema EmployeeCreate
               └─ Crear Profile
                  └─ Crear Employee
                     └─ EmbeddingService crea vector
                        └─ SQLAlchemy commit()
                           └─ PostgreSQL INSERT

4. DATABASE
   └─ Inserta en profiles
      └─ Inserta en employees
         └─ Inserta en embeddings
            └─ pgvector indexa el vector
               └─ COMMIT

5. RESPONSE
   └─ FastAPI retorna EmployeeRead (JSON)
      └─ Axios receives status 200
         └─ Frontend recibe datos
            └─ AppContext actualiza estado
               └─ UI re-renderiza
                  └─ Usuario ve empleado nuevo
```

---

**Última actualización:** Enero 2026
