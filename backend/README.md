# Mi Proyecto - Backend FastAPI

API backend desarrollado con FastAPI para el proyecto Mi Proyecto.

## 📁 Estructura del Proyecto

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # Punto de entrada - define app y rutas principales
│   ├── routers/             # Endpoints agrupados por recurso (users, projects, etc)
│   ├── models/              # Modelos Pydantic y SQLAlchemy
│   ├── services/            # Lógica de negocio
│   └── db/                  # Configuración de base de datos
├── tests/                   # Tests unitarios e integración
├── requirements.txt         # Dependencias Python
├── .env.example             # Variables de entorno ejemplo
└── README.md
```

## 🚀 Instalación

### 1. Crear entorno virtual:
```bash
python -m venv venv
```

### 2. Activar entorno virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

### 4. Crear archivo `.env`:
```bash
cp .env.example .env
```

### 5. Configurar variables de entorno:
Edita `.env` con tus valores:
```env
DATABASE_URL=postgresql://user:password@localhost:5432/mi_proyecto
SECRET_KEY=tu_clave_secreta_aleatoria
DEBUG=True
```

## 🛠️ Desarrollo

### Opción 1: Ejecutar directamente
```bash
python app/main.py
```

### Opción 2: Usar Uvicorn (recomendado)
```bash
uvicorn app.main:app --reload
```

El API estará disponible en `http://localhost:8000`

### Documentación interactiva:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🧪 Testing

```bash
# Instalar pytest
pip install pytest pytest-asyncio

# Ejecutar tests
pytest tests/
```

## 📦 Dependencias principales

| Librería | Propósito |
|----------|-----------|
| **fastapi** | Framework web moderno |
| **uvicorn** | Servidor ASGI |
| **pydantic** | Validación de datos |
| **sqlalchemy** | ORM para base de datos |
| **psycopg2** | Driver PostgreSQL |
| **python-dotenv** | Cargar variables .env |

## 🔌 Módulos clave

### main.py
- Crear instancia FastAPI
- Configurar CORS
- Definir rutas principales (/health, /)
- Registrar routers

### routers/
- Endpoints organizados por recurso
- Validación de entrada con Pydantic
- Retorno de respuestas JSON

### services/
- Lógica de negocio pura
- Operaciones en BD
- Reglas de aplicación

**Servicios disponibles:**
- `create_proyect.py` - ProjectCreator: Crear proyectos individuales o múltiples
- `create_employee.py` - EmployeeCreator: Crear empleados individuales o múltiples
- `create_profile.py` - ProfileCreator: Crear perfiles individuales o múltiples
- `project_service.py` - ProjectService: CRUD completo de proyectos
- `employee_service.py` - EmployeeService: CRUD completo de empleados
- `profile_service.py` - ProfileService: CRUD completo de perfiles
- `employee_project_service.py` - EmployeeProjectService: Gestionar asignaciones empleado-proyecto
- `ejemplo_uso_servicios.py` - Ejemplos de uso de todos los servicios

### models/
- Modelos Pydantic para validación
- Modelos SQLAlchemy para BD

### db/
- Configuración de conexión
- Sesiones de BD
- Migraciones (si usa Alembic)

## 🔧 Servicios CRUD

### Patrón de Diseño
Todos los servicios siguen el mismo patrón que `create_proyect.py`:

1. **Constructor**: Abre sesión de base de datos
2. **create_one()**: Crea un registro individual
3. **create_many()**: Crea múltiples registros
4. **Métodos CRUD**: get_by_id, get_all, update_by_id, delete_by_id
5. **close()**: Cierra sesión de BD

### Ejemplo de Uso

```python
from app.services.project_service import ProjectService
from datetime import date

# Crear servicio
service = ProjectService()

# Crear un proyecto
project_data = {
    "name": "Nuevo Proyecto",
    "description": "Descripción del proyecto",
    "client": "Cliente ABC",
    "start_date": date.today(),
    "budget": 30000
}
project = service.create_one(project_data)

# Obtener proyecto
project = service.get_by_id(1)

# Actualizar proyecto
update_data = {"budget": 35000}
service.update_by_id(1, update_data)

# Eliminar proyecto
service.delete_by_id(1)

# Cerrar conexión
service.close()
```

### Servicios Disponibles

#### ProjectService
```python
from app.services.project_service import ProjectService

service = ProjectService()
# create_one(), create_many(), get_by_id(), get_all()
# get_by_client(), get_finished(), get_active()
# update_by_id(), delete_by_id(), delete_many()
```

#### EmployeeService
```python
from app.services.employee_service import EmployeeService

service = EmployeeService()
# create_one(), create_many(), get_by_id(), get_all()
# get_by_office(), get_by_name(), get_with_profile()
# update_by_id(), delete_by_id(), delete_many()
```

#### ProfileService
```python
from app.services.profile_service import ProfileService

service = ProfileService()
# create_one(), create_many(), get_by_id(), get_all()
# get_by_skill(), get_by_language()
# update_by_id(), delete_by_id(), delete_many()
```

#### EmployeeProjectService
```python
from app.services.employee_project_service import EmployeeProjectService

service = EmployeeProjectService()
# assign_employee_to_project(), remove_employee_from_project()
# get_employees_by_project(), get_projects_by_employee()
# assign_multiple_employees_to_project()
```

### Ejecutar Ejemplos
```bash
# Desde backend/
python app/services/ejemplo_uso_servicios.py
```

## 📚 Crear un nuevo router

### 1. Crear archivo `app/routers/ejemplo.py`:
```python
from fastapi import APIRouter, Depends
from app.db import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/")
def get_items(db: Session = Depends(get_db)):
    """Obtener todos los items"""
    return [{"id": 1, "nombre": "Item 1"}]

@router.post("/")
def create_item(nombre: str, db: Session = Depends(get_db)):
    """Crear nuevo item"""
    # Lógica aquí
    return {"id": 1, "nombre": nombre}
```

### 2. Registrar en `app/main.py`:
```python
from app.routers import ejemplo

app.include_router(
    ejemplo.router, 
    prefix="/api/items",
    tags=["Items"]
)
```

## 🌍 Variables de Entorno

```env
# Conexión a BD PostgreSQL
DATABASE_URL=postgresql://user:password@localhost:5432/mi_proyecto

# Clave para JWT
SECRET_KEY=tu_clave_secreta_aleatoria

# Modo debug
DEBUG=True
```

## 🔐 Autenticación (JWT)

Ejemplo básico:
```python
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer

security = HTTPBearer()

@router.get("/protected")
def get_protected(credentials = Depends(security)):
    # Verificar token JWT aquí
    return {"mensaje": "Acceso permitido"}
```

## 🐳 Docker (opcional)

```dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
```

```bash
# Build
docker build -t mi-proyecto-api .

# Run
docker run -p 8000:8000 mi-proyecto-api
```

## 📖 Recursos útiles

- [Documentación FastAPI](https://fastapi.tiangolo.com/)
- [Documentación SQLAlchemy](https://docs.sqlalchemy.org/)
- [Documentación Pydantic](https://docs.pydantic.dev/)
