# 
# MÓDULO BACKEND/APP/DB/__INIT__.PY
# ==================================
# 
# Exporta componentes de base de datos para imports simplificados
# 

from app.db.database import SessionLocal, engine, Base
from app.db.create_tables import InitDB

__all__ = [
    'SessionLocal',
    'engine',
    'Base',
    'InitDB',
]
# 
# @router.get("/users")
# def get_users(db: Session = Depends(get_db)):
#     # db es una sesión de BD inyectada automáticamente
#     users = db.query(User).all()
#     return users
# 
# FastAPI automáticamente:
# 1. Llama get_db()
# 2. Pasa la sesión al endpoint
# 3. Cierra la sesión después
# 
# OPERACIONES COMUNES:
# 
# # CREATE
# db.add(nuevo_usuario)
# db.commit()
# 
# # READ
# usuario = db.query(User).filter(User.id == 1).first()
# usuarios = db.query(User).all()
# 
# # UPDATE
# usuario.nombre = "Nuevo nombre"
# db.commit()
# 
# # DELETE
# db.delete(usuario)
# db.commit()
# 
