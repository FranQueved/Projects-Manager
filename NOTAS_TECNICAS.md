# 🔧 Notas Técnicas - Project Manager

## Decisiones de Arquitectura

### Backend

#### 1. Estructura de Routers
- Separamos los endpoints en 3 routers independientes:
  - `employees.py` - CRUD de empleados
  - `projects.py` - CRUD de proyectos
  - `assignments.py` - Relaciones empleado-proyecto
- Cada router es un módulo independiente e importable

#### 2. Manejo de Errores
- HTTPException para errores (404, 400, etc)
- Mensajes de error claros
- Respuestas JSON consistentes

#### 3. Validación
- Schemas Pydantic para request/response
- Validación automática de tipos
- Documentación automática en Swagger

### Frontend

#### 1. Estado Global con Context API
```javascript
// En lugar de props drilling, usamos Context para:
- Empleados
- Proyectos
- Estado de carga
- Errores
```

#### 2. Servicios Centralizados
```javascript
// dataService.js exporta:
- employeeService (getAll, getById, create, update, delete)
- projectService (CRUD)
- assignmentService (asignación/desasignación)
```

#### 3. Componentes Reutilizables
- Componentes pequeños y enfocados
- Props para personalización
- CSS modular por componente

#### 4. Páginas y Rutas
```
/ → Home (Landing)
/dashboard → Dashboard (Estadísticas)
/employees → Empleados (CRUD)
/projects → Proyectos (CRUD)
```

---

## Mejoras Futuras Sugeridas

### Fase 2 - Seguridad
- [ ] Autenticación JWT
- [ ] Roles y permisos
- [ ] Validación de tokens

### Fase 3 - Búsqueda Semántica
- [ ] Integrar Sentence Transformers
- [ ] Búsqueda de empleados por habilidades
- [ ] Matching automático empleado-proyecto

### Fase 4 - UI/UX
- [ ] Temas oscuro/claro
- [ ] Internacionalización (i18n)
- [ ] Mejor responsive en móvil
- [ ] Animaciones

### Fase 5 - Funcionalidades
- [ ] Historial de cambios
- [ ] Filtros avanzados
- [ ] Exportar datos (CSV, PDF)
- [ ] Notificaciones en tiempo real

### Fase 6 - Testing
- [ ] Tests unitarios backend (pytest)
- [ ] Tests componentes frontend (Jest)
- [ ] Tests de integración E2E (Cypress)

---

## Configuración de Desarrollo

### Variables de Entorno

**Backend (.env)**
```env
DATABASE_URL=postgresql://user:password@localhost:5432/project_manager
DEBUG=True
```

**Frontend (.env)**
```env
REACT_APP_API_URL=http://localhost:8000
```

### Configuración de CORS

Ubicación: `backend/app/main.py`

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Si necesitas agregar más orígenes, agrégalos a la lista `allow_origins`.

---

## Flujo de Datos

### Creación de Empleado

```
Frontend (Employees.jsx)
    ↓
handleSubmit → createEmployee()
    ↓
AppContext (createEmployee)
    ↓
dataService (employeeService.create)
    ↓
Axios → POST /api/employees
    ↓
Backend (routers/employees.py)
    ↓
create_employee() → Database
    ↓
Response JSON
    ↓
Frontend (Alert + setEmployees)
```

### Lectura de Empleados

```
Dashboard.jsx → useEffect
    ↓
loadEmployees() from AppContext
    ↓
employeeService.getAll()
    ↓
GET /api/employees
    ↓
Backend query → Database
    ↓
Response JSON (list)
    ↓
setEmployees(data)
    ↓
Render Table
```

---

## Troubleshooting Común

### Error: "Cannot connect to database"
**Solución:**
1. Verifica que PostgreSQL esté corriendo
2. Confirma DATABASE_URL en .env
3. Verifica credenciales de usuario

### Error: "No module named 'app'"
**Solución:**
1. Asegúrate de estar en carpeta backend/
2. Activa el entorno virtual
3. Ejecuta: `pip install -r requirements.txt`

### Error: "Module not found" en Frontend
**Solución:**
1. Elimina `node_modules`
2. Ejecuta `npm install`
3. Reinicia el servidor

### Error: "CORS policy: No 'Access-Control-Allow-Origin'"
**Solución:**
1. Verifica que el backend está corriendo
2. Verifica la URL en .env del frontend
3. Recarga la página (Ctrl+Shift+R)

---

## Performance

### Backend
- FastAPI es muy rápido por defecto
- Usa SQLAlchemy lazy loading para reducir queries
- PostgreSQL con índices en campos frecuentes

### Frontend
- React.memo para componentes costosos
- useCallback para evitar re-renders innecesarios
- Lazy loading de rutas (opcional)

---

## Seguridad Consideraciones

1. **CORS**: Configurado para localhost solo
2. **No hay autenticación**: Agregar en fase 2
3. **SQL Injection**: Prevenido por SQLAlchemy ORM
4. **HTTPS**: Usar en producción
5. **Validación**: Pydantic valida entrada

---

## Deployment (Próximamente)

Para producción, considera:

**Backend:**
- Usar Gunicorn/Uvicorn
- Railway, Render, o Heroku
- Variables de entorno seguros

**Frontend:**
- Build: `npm run build`
- Deploy: Vercel, Netlify, o hosting estático

---

## Links Útiles

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [React Router](https://reactrouter.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [PostgreSQL](https://www.postgresql.org/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)

---

Última actualización: 2026-01-05
