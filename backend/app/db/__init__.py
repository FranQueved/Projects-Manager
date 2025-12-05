# 
# MÓDULO BACKEND/APP/DB/__INIT__.PY
# ==================================
# 
# CARPETA DB: Configuración y conexión a base de datos
# 
# ¿QUÉ VA AQUÍ?
# 
# database.py:
#   - Configurar SQLAlchemy engine
#   - Crear sesión de BD
#   - Funciones para conectar/desconectar
#   
#   from sqlalchemy import create_engine
#   from sqlalchemy.orm import sessionmaker
#   
#   DATABASE_URL = "postgresql://user:pass@localhost/db"
#   engine = create_engine(DATABASE_URL)
#   SessionLocal = sessionmaker(bind=engine)
#   
#   def get_db():
#       db = SessionLocal()
#       yield db
#       db.close()
# 
# CÓMO SE USA EN LOS ROUTERS:
# 
# from fastapi import Depends
# from app.db import get_db
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
