from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base
from pgvector.sqlalchemy import Vector
from app.db.database import Base

# Tabla para almacenar embeddings usando pgvector
# Los embeddings son vectores de 384 dimensiones (all-MiniLM-L6-v2)
embeding_table: Table = Table(
    "embeding_table",
    Base.metadata,
    Column("id_project", Integer, ForeignKey("projects.id"), nullable=True),
    Column("id_employee", Integer, ForeignKey("employees.id"), nullable=True, unique=True),
    Column("vector", Vector(384), nullable=False),  # Almacena embeddings con pgvector (384 dimensiones)
)








