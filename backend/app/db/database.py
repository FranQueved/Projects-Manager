# app/db/database.py

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, declarative_base

# Cambia esto por tu conexión real
# Ejemplos:
# PostgreSQL: "postgresql://user:password@localhost:5432/mydb"
# SQLite:     "sqlite:///./test.db"
DATABASE_URL = "postgresql://postgres:123456789@db.ufvfmeptmrukthgvdjwd.supabase.co:5432/postgres"

# Engine: puerta principal hacia la base de datos
engine = create_engine(
    DATABASE_URL,
    echo=True,          # Muestra las consultas SQL en consola (útil para debug). Pon False en producción.
    future=True
)

# Registrar evento para habilitar la extensión pgvector en la conexión
@event.listens_for(engine, "connect")
def enable_pgvector(dbapi_conn, connection_record):
    """Habilita la extensión pgvector en PostgreSQL"""
    with dbapi_conn.cursor() as cursor:
        cursor.execute("CREATE EXTENSION IF NOT EXISTS vector")
        dbapi_conn.commit()

# SessionLocal: fábrica de sesiones (llaves temporales)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base: clase base para todos tus models
Base = declarative_base()

