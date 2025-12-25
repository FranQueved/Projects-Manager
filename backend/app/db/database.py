"""Database configuration and connection setup."""

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:123456789@db.ufvfmeptmrukthgvdjwd.supabase.co:5432/postgres"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    future=True
)


@event.listens_for(engine, "connect")
def enable_pgvector(dbapi_conn, connection_record):
    """Enable pgvector extension for vector operations."""
    with dbapi_conn.cursor() as cursor:
        cursor.execute("CREATE EXTENSION IF NOT EXISTS vector")
        dbapi_conn.commit()


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

