# Mi Proyecto - Frontend React

Aplicación frontend desarrollada con React para el proyecto Mi Proyecto.

## 📁 Estructura del Proyecto

```
frontend/
├── public/               # Archivos estáticos HTML/imágenes
│   └── index.html        # Archivo HTML principal
├── src/
│   ├── components/       # Componentes reutilizables (botones, cards, etc)
│   ├── pages/            # Páginas principales (Home, Dashboard, etc)
│   ├── hooks/            # Custom hooks (lógica reutilizable)
│   ├── context/          # React Context para estado global
│   ├── services/         # Servicios API y utilidades
│   ├── App.jsx           # Componente principal con rutas
│   ├── index.jsx         # Punto de entrada
│   ├── App.css
│   └── index.css         # Estilos globales
├── package.json          # Dependencias y scripts
└── .env.example          # Variables de entorno ejemplo
```

## 🚀 Instalación

1. **Instalar dependencias:**
```bash
npm install
```

2. **Crear archivo `.env`:**
```bash
cp .env.example .env
```

3. **Configurar la URL del API en `.env`:**
```env
REACT_APP_API_URL=http://localhost:8000/api
```

## 🛠️ Desarrollo

**Iniciar servidor de desarrollo:**
```bash
npm start
```

La aplicación se abrirá automáticamente en `http://localhost:3000`

## 📦 Build para producción

```bash
npm run build
```

Genera una carpeta `build/` con la aplicación optimizada lista para deploying.

## 🧪 Testing

```bash
npm test
```

Ejecuta todos los tests unitarios.

## 📚 Dependencias principales

| Librería | Propósito |
|----------|-----------|
| **react** | Librería de UI y componentes |
| **react-dom** | Renderización en el DOM |
| **react-router-dom** | Enrutamiento entre páginas |
| **axios** | Cliente HTTP para peticiones al API |
| **zustand** | Gestión de estado (opcional) |

## 🔌 Módulos clave

### services/api.js
Cliente HTTP centralizado que:
- Configura la URL base del API
- Agrega automáticamente tokens de autenticación
- Maneja errores comunes

### context/AppContext.jsx
Contexto global que proporciona:
- Información del usuario autenticado
- Estados de carga y error globales

### hooks/useFetch.js
Hook reutilizable para fetching de datos:
- Automáticamente maneja loading, error y data
- Se ejecuta una sola vez al montar el componente

## 🌍 Variables de Entorno

```env
# URL del API backend
REACT_APP_API_URL=http://localhost:8000/api
```

## 📖 Cómo usar los módulos

### Hacer una petición al API
```javascript
import api from '../services/api';

// GET
const usuarios = await api.get('/usuarios');

// POST
await api.post('/usuarios', { nombre: 'Juan' });

// PUT
await api.put('/usuarios/1', { nombre: 'Juan Pérez' });

// DELETE
await api.delete('/usuarios/1');
```

### Usar el contexto global
```javascript
import { useAppContext } from '../context/AppContext';

function MiComponente() {
  const { user, loading, setUser } = useAppContext();
  // Usar el estado global aquí
}
```

### Usar el hook de fetch
```javascript
import { useFetch } from '../hooks/useFetch';

function ListaUsuarios() {
  const { data: usuarios, loading, error } = useFetch('/usuarios');
  
  if (loading) return <p>Cargando...</p>;
  if (error) return <p>Error: {error}</p>;
  return <ul>{usuarios.map(u => <li>{u.nombre}</li>)}</ul>;
}
```

## 🎨 Estructura de carpetas

- **components/**: Componentes pequeños y reutilizables
  - Button.jsx, Card.jsx, Modal.jsx, etc.
  
- **pages/**: Componentes grandes que representan páginas
  - Home.jsx, Dashboard.jsx, Login.jsx, etc.
  
- **hooks/**: Lógica reutilizable
  - useFetch.js, useAuth.js, useLocalStorage.js, etc.
  
- **context/**: Estado global compartido
  - AppContext.jsx, AuthContext.jsx, etc.
  
- **services/**: Lógica de negocio y utilidades
  - api.js, authService.js, storageService.js, etc.

