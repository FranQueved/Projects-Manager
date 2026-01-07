# Guía de Instalación y Ejecución - Project Manager

## ✅ Requisitos

- Python 3.8+
- Node.js 14+
- npm 6+
- PostgreSQL 12+ (con extensión pgvector)

## 🚀 Instalación y Configuración

### 1. Backend (FastAPI)

#### Paso 1: Crear entorno virtual

```bash
cd backend
python -m venv venv

# En Windows
venv\Scripts\activate

# En Linux/Mac
source venv/bin/activate
```

#### Paso 2: Instalar dependencias

```bash
pip install -r requirements.txt
```

#### Paso 3: Configurar base de datos

Actualiza el archivo `.env` o `app/db/database.py` con tus credenciales de PostgreSQL:

```python
DATABASE_URL = "postgresql://usuario:contraseña@localhost:5432/project_manager"
```

#### Paso 4: Inicializar base de datos

```bash
python -m app.db.create_tables
```

#### Paso 5: (Opcional) Cargar datos de ejemplo

```bash
python -m app.services.fixtures.populate_database
```

#### Paso 6: Ejecutar el servidor

```bash
python -m uvicorn app.main:app --reload
```

El API estará disponible en: `http://localhost:8000`
Documentación interactiva: `http://localhost:8000/docs`

### 2. Frontend (React)

#### Paso 1: Instalar dependencias

```bash
cd frontend
npm install
```

#### Paso 2: Configurar variables de entorno

El archivo `.env` ya está configurado con:
```
REACT_APP_API_URL=http://localhost:8000
```

Si necesitas cambiar la URL del API, actualiza este archivo.

#### Paso 3: Ejecutar el servidor de desarrollo

```bash
npm start
```

La aplicación se abrirá automáticamente en: `http://localhost:3000`

## 📋 Endpoints del API

### Empleados
- `GET /api/employees` - Listar todos los empleados
- `GET /api/employees/{id}` - Obtener un empleado específico
- `POST /api/employees` - Crear un nuevo empleado
- `PUT /api/employees/{id}` - Actualizar un empleado
- `DELETE /api/employees/{id}` - Eliminar un empleado

### Proyectos
- `GET /api/projects` - Listar todos los proyectos
- `GET /api/projects/{id}` - Obtener un proyecto específico
- `POST /api/projects` - Crear un nuevo proyecto
- `PUT /api/projects/{id}` - Actualizar un proyecto
- `DELETE /api/projects/{id}` - Eliminar un proyecto

### Asignaciones
- `POST /api/assignments/assign/{employee_id}/{project_id}` - Asignar empleado a proyecto
- `DELETE /api/assignments/unassign/{employee_id}/{project_id}` - Desasignar empleado de proyecto
- `GET /api/assignments/project/{project_id}` - Obtener empleados de un proyecto
- `GET /api/assignments/employee/{employee_id}` - Obtener proyectos de un empleado

## 🏗️ Estructura del Proyecto

```
Project-Manager/
├── backend/
│   ├── app/
│   │   ├── db/           # Configuración de base de datos
│   │   ├── models/       # Modelos SQLAlchemy
│   │   ├── schemas/      # Esquemas Pydantic
│   │   ├── services/     # Lógica de negocio
│   │   ├── routers/      # Endpoints API
│   │   └── main.py       # Aplicación FastAPI
│   ├── requirements.txt   # Dependencias Python
│   └── README.md         # Documentación backend
│
├── frontend/
│   ├── src/
│   │   ├── components/   # Componentes reutilizables
│   │   ├── pages/        # Páginas principales
│   │   ├── services/     # Servicios de API
│   │   ├── context/      # Estado global
│   │   ├── styles/       # Estilos CSS
│   │   ├── App.jsx       # Componente raíz
│   │   └── index.jsx     # Punto de entrada
│   ├── package.json      # Dependencias Node.js
│   ├── .env              # Variables de entorno
│   └── README.md         # Documentación frontend
│
└── README.md             # Este archivo
```

## 🎨 Características Principales

### Dashboard
- Estadísticas generales (total de empleados, proyectos, presupuesto)
- Últimos empleados registrados
- Proyectos activos recientes

### Gestión de Empleados
- Crear nuevos empleados
- Editar información del empleado
- Eliminar empleados
- Gestionar habilidades técnicas y blandas

### Gestión de Proyectos
- Crear nuevos proyectos
- Editar detalles del proyecto (nombre, descripción, presupuesto, fechas)
- Eliminar proyectos
- Marcar proyectos como completados

### Asignaciones
- Asignar empleados a proyectos
- Desasignar empleados de proyectos
- Ver empleados por proyecto
- Ver proyectos por empleado

## 🔧 Tecnologías

### Backend
- **FastAPI** - Framework web moderno
- **SQLAlchemy** - ORM para base de datos
- **Pydantic** - Validación de datos
- **PostgreSQL** - Base de datos relacional
- **pgvector** - Extensión para búsquedas vectoriales

### Frontend
- **React 18** - Librería de UI
- **React Router** - Enrutamiento
- **Axios** - Cliente HTTP
- **CSS3** - Estilos

## 🚨 Solución de Problemas

### Error de conexión a base de datos
- Verifica que PostgreSQL esté corriendo
- Confirma las credenciales en DATABASE_URL
- Asegúrate de que la extensión pgvector está instalada

### Error de CORS en frontend
- El backend está configurado para permitir conexiones desde localhost:3000
- Si cambias el puerto del frontend, actualiza la configuración de CORS en `backend/app/main.py`

### Módulos no encontrados (Python)
- Asegúrate de tener el entorno virtual activado
- Ejecuta: `pip install -r requirements.txt`

### Node modules no encontrados
- Elimina la carpeta `node_modules` y `package-lock.json`
- Ejecuta: `npm install`

## 📚 Documentación Adicional

- [Backend README](./backend/README.md)
- [Frontend README](./frontend/README.md)
- [Arquitectura del Backend](./backend/ARCHITECTURE.md)

## ✨ Próximos Pasos

1. Carga datos de ejemplo: `python -m app.services.fixtures.populate_database`
2. Accede al dashboard: `http://localhost:3000/dashboard`
3. Comienza a crear proyectos y asignar empleados

¡Listo para empezar! 🎉
