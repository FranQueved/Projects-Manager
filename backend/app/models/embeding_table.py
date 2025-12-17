from sqlalchemy import Table, Column, Integer, ForeignKey, DateTime, Float, UniqueConstraint
from sqlalchemy.dialects.postgresql import ARRAY
from datetime import datetime
from app.db.database import Base


embeding_table = Table(
    "embeding_table",
    Base.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("id_project", Integer, ForeignKey("projects.id"), nullable=True),
    Column("id_employee", Integer, ForeignKey("employees.id"), nullable=True, unique=True),
    Column("vector", ARRAY(Float), nullable=False),  # Almacena embeddings como array de floats (pgvector compatible)
    Column("created_at", DateTime, default=datetime.utcnow),
)








