# 
# MÓDULO BACKEND/APP/ROUTERS/__INIT__.PY
# ======================================
# 
# CARPETA ROUTERS: Agrupa endpoints por funcionalidad/recurso
# 
# ¿QUÉ VA AQUÍ?
# 
# Cada archivo es un router que contiene endpoints relacionados:
# 
# routers/users.py:
#   POST   /api/users        → Crear usuario
#   GET    /api/users        → Listar usuarios
#   GET    /api/users/{id}   → Obtener usuario
#   PUT    /api/users/{id}   → Actualizar usuario
#   DELETE /api/users/{id}   → Eliminar usuario
# 
# routers/projects.py:
#   POST   /api/projects     → Crear proyecto
#   GET    /api/projects     → Listar proyectos
#   etc...
# 
# BENEFICIOS:
# - Organización: Código relacionado junto
# - Mantenibilidad: Fácil encontrar endpoints
# - Escalabilidad: Agregar nuevos routers es simple
# - Documentación: Se agrupa en Swagger por tags
# 
# CÓMO CREAR UN ROUTER:
# 
# from fastapi import APIRouter
# 
# router = APIRouter()
# 
# @router.get("/")
# def get_users():
#     return [{"id": 1, "nombre": "Juan"}]
# 
# Luego en main.py:
# from app.routers import users
# app.include_router(users.router, prefix="/api/users")
# 
