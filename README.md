# 🚀 Project Manager - Sistema Integral de Gestión

![Status](https://img.shields.io/badge/status-✅%20Completado-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![React](https://img.shields.io/badge/React-18.2-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.122-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue)

Sistema fullstack de gestión de proyectos y empleados con asignaciones inteligentes, construido con **FastAPI** en el backend y **React 18** en el frontend.

## ✨ Características

### 🎯 Gestión Central
- **Empleados**: Crear, editar, listar y eliminar empleados con perfiles
- **Proyectos**: Gestión completa de proyectos con presupuesto, fechas y clientes
- **Asignaciones**: Asignar empleados a proyectos de forma rápida
- **Dashboard**: Estadísticas en tiempo real

### 🎨 Interfaz Moderna
- UI responsiva y limpia
- Componentes reutilizables
- Modales para acciones
- Tablas interactivas
- Alerts para feedback

### 🔧 Tecnología
- **Backend**: FastAPI con SQLAlchemy ORM
- **Frontend**: React 18 con Context API
- **Base de Datos**: PostgreSQL con pgvector
- **HTTP**: Axios para comunicación API
- **Enrutamiento**: React Router v6

---

## 📊 Estructura del Proyecto

```
Project-Manager/
├── backend/                 # API FastAPI
│   ├── app/
│   │   ├── db/             # Configuración base de datos
│   │   ├── models/         # Modelos SQLAlchemy
│   │   ├── schemas/        # Esquemas Pydantic
│   │   ├── services/       # Lógica de negocio
│   │   ├── routers/        # Endpoints API ✨
│   │   └── main.py         # App principal
│   ├── requirements.txt
│   ├── .env.example
│   ├── ARCHITECTURE.md
│   └── README.md
│
├── frontend/                # App React
│   ├── src/
│   │   ├── components/     # Componentes reutilizables ✨
│   │   ├── pages/          # Páginas principales ✨
│   │   ├── services/       # Servicios API ✨
│   │   ├── context/        # Estado global ✨
│   │   ├── styles/         # Estilos CSS ✨
│   │   ├── App.jsx         # Componente raíz ✨
│   │   └── index.jsx
│   ├── package.json
│   ├── .env
│   └── README.md
│
├── QUICKSTART.md           # ⚡ Inicio en 2 minutos
├── SETUP.md                # 📖 Guía de instalación
├── IMPLEMENTACION.md       # 📋 Resumen técnico
├── NOTAS_TECNICAS.md       # 🔧 Decisiones arquitectónicas
└── README.md               # Este archivo
```

---

## 🚀 Inicio Rápido

### Requisitos
- Python 3.8+
- Node.js 14+
- PostgreSQL 12+

### Opción 1: Los Impatientes (2 minutos)

**Terminal 1 - Backend:**
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm start
```

Luego accede a: **http://localhost:3000**

### Opción 2: Instalación Completa

Ver [SETUP.md](SETUP.md) para instalación paso a paso con configuración de base de datos.

---

## 📚 API Endpoints

### 👥 Empleados
```
GET    /api/employees              - Listar todos
POST   /api/employees              - Crear uno
GET    /api/employees/{id}         - Obtener uno
PUT    /api/employees/{id}         - Actualizar
DELETE /api/employees/{id}         - Eliminar
```

### 📋 Proyectos
```
GET    /api/projects               - Listar todos
POST   /api/projects               - Crear uno
GET    /api/projects/{id}          - Obtener uno
PUT    /api/projects/{id}          - Actualizar
DELETE /api/projects/{id}          - Eliminar
```

### 🔗 Asignaciones
```
POST   /api/assignments/assign/{emp}/{proj}      - Asignar empleado
DELETE /api/assignments/unassign/{emp}/{proj}    - Desasignar
GET    /api/assignments/project/{id}             - Empleados por proyecto
GET    /api/assignments/employee/{id}            - Proyectos por empleado
```

---

## 🎮 Interfaz de Usuario

### 🏠 Home
Landing page con características principales y links de navegación.

### 📊 Dashboard
- Estadísticas: Total de empleados, proyectos, completados
- Presupuesto total
- Últimos empleados
- Proyectos activos

### 👥 Empleados
- Tabla con todos los empleados
- Modal para crear/editar
- Campos: Nombre, Oficina, Habilidades técnicas/blandas, Idiomas
- Acciones: Editar, Eliminar

### 📋 Proyectos
- Tabla con todos los proyectos
- Modal para crear/editar
- Campos: Nombre, Descripción, Cliente, Fechas, Presupuesto
- Checkboxes: Presencial, Completado
- Acciones: Editar, Eliminar

---

## 🏗️ Arquitectura

### Backend
```
FastAPI Application
  │
  ├─ Routers (14 endpoints)
  │   ├─ employees.py (5 endpoints)
  │   ├─ projects.py (5 endpoints)
  │   └─ assignments.py (4 endpoints)
  │
  ├─ Models (SQLAlchemy ORM)
  │   ├─ Employee
  │   ├─ Project
  │   ├─ Profile
  │   └─ EmployeeProject (M-N)
  │
  ├─ Schemas (Pydantic)
  │   ├─ EmployeeCreate/Read
  │   ├─ ProjectCreate/Read
  │   └─ ProfileRead
  │
  └─ Services
      └─ Lógica de negocio
```

### Frontend
```
React Application
  │
  ├─ Pages (4)
  │   ├─ Home
  │   ├─ Dashboard
  │   ├─ Employees
  │   └─ Projects
  │
  ├─ Components (7)
  │   ├─ Button, Card, Modal
  │   ├─ Form, Table, Loading
  │   └─ Alert
  │
  ├─ Context (AppContext)
  │   └─ Estado global de app
  │
  ├─ Services (dataService)
  │   ├─ employeeService
  │   ├─ projectService
  │   └─ assignmentService
  │
  └─ Styles (11 CSS files)
      └─ Estilos modulares
```

---

## 🔄 Flujo de Datos

```
Frontend (React)
    ↓
User Action
    ↓
Component Handler
    ↓
AppContext / useAppContext
    ↓
dataService
    ↓
Axios HTTP Request
    ↓
Backend (FastAPI)
    ↓
Router Handler
    ↓
SQLAlchemy ORM
    ↓
PostgreSQL Database
    ↓
Response JSON
    ↓
Frontend Update State
    ↓
Re-render Component
```

---

## 🔐 Seguridad

✅ Validación de datos con Pydantic  
✅ SQL Injection prevenido (SQLAlchemy ORM)  
✅ CORS configurado para localhost:3000  
⚠️ Sin autenticación (agregar en siguiente fase)  
⚠️ Sin autorización (agregar en siguiente fase)  

**Para Producción:**
- Implementar JWT authentication
- Usar HTTPS
- Variables de entorno seguros
- Rate limiting
- Validación de entrada más estricta

---

## 📝 Documentación Completa

| Documento | Descripción |
|-----------|-----------|
| [QUICKSTART.md](QUICKSTART.md) | Inicio en 2 minutos |
| [SETUP.md](SETUP.md) | Instalación paso a paso |
| [IMPLEMENTACION.md](IMPLEMENTACION.md) | Resumen de implementación |
| [NOTAS_TECNICAS.md](NOTAS_TECNICAS.md) | Decisiones arquitectónicas |
| [Backend README](backend/README.md) | Guía del backend |
| [Frontend README](frontend/README.md) | Guía del frontend |
| [Architecture](backend/ARCHITECTURE.md) | Arquitectura del backend |

---

## 🛠️ Stack Tecnológico

### Backend
- **FastAPI 0.122** - Framework web asincrónico
- **SQLAlchemy 2.0** - ORM SQL
- **Pydantic 2.12** - Validación de datos
- **PostgreSQL** - Base de datos
- **pgvector 0.4** - Extensión vectorial
- **Uvicorn 0.38** - Servidor ASGI

### Frontend
- **React 18.2** - Librería UI
- **React Router 6.20** - Enrutamiento
- **Axios 1.6** - Cliente HTTP
- **CSS3** - Estilos

---

## 🚨 Solución de Problemas

### Backend
- **"Module not found"**: Activa el entorno virtual y ejecuta `pip install -r requirements.txt`
- **"Connection refused"**: Verifica que PostgreSQL esté corriendo
- **"CORS error"**: El backend debe estar en http://localhost:8000

### Frontend
- **"npm ERR"**: Elimina `node_modules` y ejecuta `npm install`
- **"Cannot GET"**: Verifica que el backend esté corriendo
- **"Blank page"**: Abre la consola (F12) para ver errores

---

## 📈 Próximas Fases

### Fase 2 - Seguridad
- [ ] Autenticación JWT
- [ ] Roles y permisos
- [ ] Hash de contraseñas

### Fase 3 - Inteligencia
- [ ] Búsqueda semántica con embeddings
- [ ] Matching automático empleado-proyecto
- [ ] Recomendaciones

### Fase 4 - UX Mejorada
- [ ] Tema oscuro/claro
- [ ] Internacionalización (i18n)
- [ ] Filtros avanzados
- [ ] Exportar a PDF/CSV

### Fase 5 - Funcionalidades
- [ ] Historial de cambios
- [ ] Notificaciones en tiempo real
- [ ] Comentarios y colaboración
- [ ] Calendario de proyectos

---

## 🤝 Contribución

Este proyecto es un ejemplo completo de fullstack development. Siéntete libre de:
- Agregar nuevas funcionalidades
- Mejorar la UI/UX
- Implementar más validaciones
- Agregar tests

---

## 📄 Licencia

Proyecto de ejemplo - Uso libre

---

## 👨‍💻 Autor

Implementación: 2026-01-05  
Status: ✅ Completado y funcional

---

## 📞 Soporte

Para problemas o preguntas:
1. Revisa la documentación en [SETUP.md](SETUP.md)
2. Consulta [NOTAS_TECNICAS.md](NOTAS_TECNICAS.md)
3. Verifica los logs de la consola

---

**¡Disfruta usando Project Manager!** 🎉

## 🔌 Comunicación Frontend-Backend

El frontend comunica con el backend a través de HTTP/AJAX:

```
Cliente (React)
    ↓
axios.get('/api/usuarios')
    ↓
Backend (FastAPI)
    ↓
@app.get("/api/usuarios")
def get_usuarios():
    return [...]
    ↓
JSON Response
    ↓
React re-renderiza
```

## 🌍 Variables de Entorno

### Frontend (.env)
```env
REACT_APP_API_URL=http://localhost:8000/api
```

### Backend (.env)
```env
DATABASE_URL=postgresql://user:password@localhost:5432/mi_proyecto
SECRET_KEY=tu_clave_secreta
DEBUG=True
```

## Checklist de Desarrollo

- [ ] Clonar proyecto
- [ ] Instalar dependencias frontend
- [ ] Instalar dependencias backend
- [ ] Configurar archivos .env
- [ ] Verificar que ambos servidores inician correctamente
- [ ] Comprobar conectividad frontend y backend
- [ ] Crear modelos y endpoints iniciales
- [ ] Crear componentes React principales

## 🚢 Deployment

### Frontend
```bash
npm run build
# Subir carpeta 'build/' a Vercel, Netlify, o servidor web
```

### Backend
```bash
# Usar Gunicorn + Uvicorn
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.main:app
```

## Estructura de Carpetas Explicada

### backend/app/routers/
Agrupa endpoints por funcionalidad:
- users.py: CRUD de usuarios
- projects.py: CRUD de proyectos
- auth.py: Autenticación

### backend/app/services/
Lógica de negocio reutilizable:
- user_service.py: Operaciones de usuario
- project_service.py: Operaciones de proyecto

### frontend/src/components/
Componentes pequeños y reutilizables:
- Button.jsx, Card.jsx, Modal.jsx

### frontend/src/pages/
Componentes grandes que representan páginas:
- Home.jsx, Dashboard.jsx, Login.jsx

### frontend/src/services/
Servicios y utilidades:
- api.js: Cliente HTTP centralizado
- storageService.js: LocalStorage

## Seguridad

- Usar HTTPS en producción
- Guardar tokens en httpOnly cookies
- Validar datos en backend
- Usar CORS adecuadamente
- Nunca guardar secretos en código

## Debugging

### Frontend
- Abre DevTools (F12)
- Ve a Network para ver peticiones API
- Ve a Console para ver errores JavaScript
- Ve a React DevTools (extensión)

### Backend
- Logs en terminal
- Usa `print()` o logging
- Swagger UI en /docs para testear endpoints
- Ver status HTTP en respuestas

## Soporte

Para más detalles:
- Lee el README específico de cada carpeta
- Revisa comentarios en los archivos principales
- Consulta documentación oficial de cada librería

