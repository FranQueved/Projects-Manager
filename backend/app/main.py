"""
MÓDULO BACKEND/APP/MAIN.PY - PUNTO DE ENTRADA DEL API
======================================================

Este es el archivo principal del backend. Aquí es donde:

1. SE CREA LA APLICACIÓN FASTAPI:
   - Creas la instancia de FastAPI que será el API
   - Configuras middlewares (CORS, autenticación, logging, etc)
   
2. SE DEFINEN LAS RUTAS PRINCIPALES:
   - El endpoint raíz "/"
   - El endpoint de health check "/health"
   - Se importan y registran todos los routers (usuarios, proyectos, etc)
   
3. SE EJECUTA EL SERVIDOR:
   - Con: python app/main.py
   - Se inicia Uvicorn que escucha en http://localhost:8000

DOCUMENTACIÓN AUTOMÁTICA:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

¿QUÉ SON LOS ROUTERS?
Son módulos que agrupan endpoints relacionados:
- routers/users.py: Endpoints de usuarios
- routers/projects.py: Endpoints de proyectos
Se registran en main.py con app.include_router()

FLUJO GENERAL:
Cliente → petición HTTP → FastAPI → Router correspondiente → 
→ Service (lógica de negocio) → Base de datos → respuesta JSON
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Crear la aplicación FastAPI
app = FastAPI(
    title="Mi Proyecto API",
    version="0.1.0",
    description="API para Mi Proyecto con backend en FastAPI"
)

# ============================================
# CONFIGURAR CORS (Cross-Origin Resource Sharing)
# ============================================
# CORS permite que el frontend React (puerto 3000) acceda a este API (puerto 8000)
# Sin CORS, el navegador bloqueaía las peticiones por seguridad
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",      # Desarrollo React
        "http://localhost:5173",      # Desarrollo Vite
        # Agregar dominios de producción aquí
    ],
    allow_credentials=True,            # Permitir cookies/autenticación
    allow_methods=["*"],               # Permitir todos los métodos HTTP
    allow_headers=["*"],               # Permitir todos los headers
)

# ============================================
# RUTAS PRINCIPALES
# ============================================

@app.get("/")
def read_root():
    """
    ENDPOINT RAÍZ
    Retorna un saludo simple. Útil para verificar que el API está corriendo.
    """
    return {"message": "Bienvenido a Mi Proyecto API"}


@app.get("/health")
def health_check():
    """
    ENDPOINT DE HEALTH CHECK
    Los orquestadores (Docker, Kubernetes) usan este endpoint para verificar
    que la aplicación está viva y funcionando correctamente.
    
    Retorna: {"status": "ok"} si todo está bien
    """
    return {"status": "ok"}

# ============================================
# REGISTRAR ROUTERS (descomenta cuando crees los módulos)
# ============================================
# Los routers agrupan endpoints por funcionalidad
# from app.routers import users, projects
# app.include_router(users.router, prefix="/api/users", tags=["Usuarios"])
# app.include_router(projects.router, prefix="/api/projects", tags=["Proyectos"])

# ============================================
# EJECUTAR EL SERVIDOR
# ============================================
# Esto se ejecuta si corres este archivo directamente: python app/main.py
if __name__ == "__main__":
    import uvicorn
    # Iniciar servidor Uvicorn
    # host="0.0.0.0": Acepta conexiones de cualquier IP
    # port=8000: Puerto donde escucha
    # reload=True: Reinicia cuando hay cambios (solo desarrollo)
    uvicorn.run(app, host="0.0.0.0", port=8000)
