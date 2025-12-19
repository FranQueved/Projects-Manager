# Mi Proyecto

Proyecto fullstack con React en el frontend y FastAPI en el backend.

## Estructura del Proyecto

```
mi-proyecto/
├── frontend/          # React - Interfaz de usuario
│   ├── public/
│   ├── src/
│   │   ├── components/    # Componentes reutilizables
│   │   ├── pages/         # Páginas principales
│   │   ├── hooks/         # Custom hooks
│   │   ├── context/       # Estado global
│   │   ├── services/      # Cliente API
│   │   ├── App.jsx
│   │   └── index.jsx
│   ├── package.json
│   └── README.md
│
└── backend/           # FastAPI - API RESTful
    ├── app/
    │   ├── main.py        # Punto de entrada
    │   ├── routers/       # Endpoints
    │   ├── models/        # Esquemas de datos
    │   ├── services/      # Lógica de negocio
    │   └── db/            # Base de datos
    ├── tests/
    ├── requirements.txt
    └── README.md
```

## Inicio Rápido

### Frontend (React)

```bash
cd frontend

# Instalar dependencias
npm install

# Crear archivo .env
cp .env.example .env

# Iniciar servidor de desarrollo
npm start
```

La app estará en: http://localhost:3000

### Backend (FastAPI)

```bash
cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
venv\Scripts\activate

# Activar entorno (Linux/Mac)
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Crear archivo .env
cp .env.example .env

# Iniciar servidor
uvicorn app.main:app --reload
```

El API estará en: http://localhost:8000
Documentación: http://localhost:8000/docs

## 🛠️ Tecnologías

### Frontend
- **React 18**: Librería de UI
- **React Router**: Enrutamiento
- **Axios**: Cliente HTTP
- **CSS3**: Estilos
- **React Scripts**: Build tools

### Backend
- **FastAPI**: Framework web rápido
- **Uvicorn**: Servidor ASGI
- **Pydantic**: Validación de datos
- **SQLAlchemy**: ORM
- **PostgreSQL**: Base de datos (opcional)

## Documentación Detallada

- **[Frontend README](./frontend/README.md)** - Guía completa del frontend
- **[Backend README](./backend/README.md)** - Guía completa del backend

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

