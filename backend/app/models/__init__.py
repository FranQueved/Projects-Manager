# 
# MÓDULO BACKEND/APP/MODELS/__INIT__.PY
# ======================================
# 
# CARPETA MODELS: Contiene definiciones de datos (esquemas y modelos)
# 
# ¿QUÉ VA AQUÍ?
# 
# 1. MODELOS PYDANTIC: Definen la estructura de datos que recibe/envía la API
#    - Validan que los datos sean correctos
#    - Documentación automática en Swagger
#    Ejemplo: usuario.py, proyecto.py
#    
#    Clase: CreateUserRequest
#    {
#        "nombre": "Juan",
#        "email": "juan@example.com"
#    }
# 
# 2. MODELOS ORM (SQLAlchemy): Representan tablas en la base de datos
#    - Definen la estructura de la BD
#    - Mapean columnas a atributos de Python
#    Ejemplo: models/user_model.py
#    
#    Tabla users:
#    - id (INT, PK)
#    - nombre (VARCHAR)
#    - email (VARCHAR)
# 
# DIFERENCIA IMPORTANTE:
# - Pydantic models: Para validación de datos en APIs
# - SQLAlchemy models: Para mapeo de BD
# 
# Aquí importas y exportas todos los modelos para usarlos en otros módulos
# 
