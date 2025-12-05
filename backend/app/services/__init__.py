# 
# MÓDULO BACKEND/APP/SERVICES/__INIT__.PY
# =======================================
# 
# CARPETA SERVICES: Contiene la LÓGICA DE NEGOCIO
# 
# ¿QUÉ VA AQUÍ?
# 
# Services son funciones/clases que contienen la lógica de negocio.
# Aquí NO va validación HTTP ni manejo de errores de API.
# Aquí va la lógica pura de negocios.
# 
# EJEMPLO - services/user_service.py:
# 
# def crear_usuario(nombre, email):
#     # Validar que el email no exista ya
#     # Crear el usuario en BD
#     # Enviar email de confirmación
#     # Retornar usuario creado
#     pass
# 
# def obtener_usuario_por_email(email):
#     # Buscar en BD
#     # Retornar usuario o None
#     pass
# 
# SEPARACIÓN DE RESPONSABILIDADES:
# 
# routers/users.py (Capa API):
#   - Recibe request HTTP
#   - Llama a user_service
#   - Retorna response HTTP
# 
# services/user_service.py (Capa Negocio):
#   - Implementa lógica pura
#   - No conoce HTTP
#   - Reutilizable en otros contextos
# 
# VENTAJAS:
# - Testeable: Puedes testear sin HTTP
# - Reutilizable: Mismo service en CLI, API, etc
# - Mantenible: Cambios en lógica solo aquí
# 
