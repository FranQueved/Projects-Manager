# 📚 Project Manager - Documentación

Documentación del sistema Project Manager.

---

## 📖 Documentos Principales

1. **[QUICK_START.md](./QUICK_START.md)** - Instalación rápida
2. **[ARCHITECTURE.md](./ARCHITECTURE.md)** - Arquitectura del sistema
3. **[FRONTEND.md](./FRONTEND.md)** - Componentes React
4. **[TROUBLESHOOTING.md](./TROUBLESHOOTING.md)** - Solución de problemas
5. **[INDEX.md](./INDEX.md)** - Navegación completa

---

## 🚀 Quick Start

### Instalación Rápida

```bash
# 1. Clonar repositorio
git clone <repository-url>
cd Projects-Manager

# 2. Backend
cd backend
python -m venv venv
# Windows: .\venv\Scripts\Activate.ps1
# macOS/Linux: source venv/bin/activate
pip install -r requirements.txt

# Crear .env
echo "DATABASE_URL=postgresql://postgres:password@localhost:5432/project_manager" > .env

# Iniciar servidor
uvicorn app.main:app --reload

# 3. Frontend (nueva terminal)
cd frontend
npm install
npm start
```

### Acceso

| Componente | URL |
|-----------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| Swagger UI | http://localhost:8000/docs |
| ReDoc | http://localhost:8000/redoc |

---

## 📊 Tecnologías

### Backend
- **FastAPI** 0.104+ - Framework web asincrónico
- **SQLAlchemy** 2.0+ - ORM para Python
- **PostgreSQL** 14+ con pgvector - Base de datos vectorial
- **Sentence Transformers** - Modelo IA para embeddings
- **PyTorch** - Framework deep learning

### Frontend
- **React** 18 - UI library
- **React Router** v6 - Routing
- **Axios** - HTTP client
- **Zustand** - State management
- **CSS Modules** - Estilos

### DevOps
- **Uvicorn** - ASGI server
- **npm** - Package manager Node
- **pytest** - Testing framework
- **Git** - Version control

---

## 📁 Estructura Completa

```
Projects-Manager/
├── backend/                     # API REST Python
│   ├── app/
│   │   ├── main.py             # Entry point FastAPI
│   │   ├── db/                 # Configuración base de datos
│   │   ├── models/             # SQLAlchemy ORM models
│   │   ├── routers/            # FastAPI routers (endpoints)
│   │   ├── schemas/            # Pydantic schemas
│   │   └── services/           # Servicios IA y embeddings
│   ├── requirements.txt
│   ├── populate_db.py
│   ├── reset_db.py
│   └── .env (crear)
│
├── frontend/                    # Aplicación React
│   ├── src/
│   │   ├── components/         # Componentes reutilizables
│   │   ├── pages/              # Páginas/rutas
│   │   ├── services/           # Servicios HTTP
│   │   ├── context/            # State management
│   │   ├── hooks/              # Custom hooks
│   │   ├── styles/             # CSS modular
│   │   └── App.jsx
│   ├── package.json
│   └── .env (crear)
│
└── docs/                        # Este directorio
    ├── README.md               # Este archivo
    ├── ARCHITECTURE.md
    ├── DATABASE.md
    ├── API_ENDPOINTS.md
    ├── SETUP.md
    ├── DEVELOPMENT.md
    ├── SECURITY.md
    ├── FRONTEND.md
    ├── TROUBLESHOOTING.md
    └── media/                  # Diagramas e imágenes
```



## 🆘 Solución de Problemas

**¿El backend no inicia?**
→ Ver [TROUBLESHOOTING.md - Backend](./TROUBLESHOOTING.md#-backend-pythonfastapi)

**¿No puedo conectar a base de datos?**
→ Ver [TROUBLESHOOTING.md - Database](./TROUBLESHOOTING.md#-base-de-datos)

**¿El frontend muestra errores?**
→ Ver [TROUBLESHOOTING.md - Frontend](./TROUBLESHOOTING.md#-frontend-react)



---

## 🔗 Enlaces Útiles

### Documentación Externa
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [React Docs](https://react.dev/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Axios Docs](https://axios-http.com/)

### Herramientas de Desarrollo
- [Swagger UI Local](http://localhost:8000/docs)
- [ReDoc Local](http://localhost:8000/redoc)
- [React DevTools](https://chrome.google.com/webstore/detail/react-developer-tools/)
- [pgAdmin](https://www.pgadmin.org/) - GUI para PostgreSQL




**¿Necesitas ayuda? Consulta [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) o contacta al equipo de desarrollo.**

---

**Última actualización:** Enero 2026 | **Versión:** 1.0.0



## 🛠️ Stack Tecnológico

### Backend
- **Framework**: FastAPI (Python 3.13)
- **BD**: PostgreSQL + pgvector
- **ORM**: SQLAlchemy
- **IA**: Sentence Transformers (embeddings)
- **Server**: Uvicorn

### Frontend
- **Framework**: React 18
- **Routing**: React Router v6
- **HTTP**: Axios
- **State**: Zustand
- **Styling**: CSS custom

---



