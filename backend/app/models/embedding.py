"""
Modelo para almacenar embeddings vectoriales de entidades del sistema.

Permite búsquedas semánticas rápidas usando pgvector en PostgreSQL.
Los embeddings se generan con Sentence Transformers (384 dimensiones).
"""

from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from app.db.database import Base


class Embedding(Base):
    """
    Almacena embeddings vectoriales para empleados, perfiles requeridos y proyectos.
    
    Atributos:
        id: Identificador único
        profile_id: ID del perfil (relación N:1, nullable)
        required_profile_id: ID del perfil requerido (relación N:1, nullable)
        vector: Vector de embedding (384 dimensiones, pgvector)
        created_at: Timestamp de creación
    """
    
    __tablename__ = "embeddings"

    id = Column(Integer, primary_key=True, index=True)
    
    # Relaciones foráneas (solo una es requerida por embedding)
    profile_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=True, index=True)
    required_profile_id = Column(Integer, ForeignKey("required_profiles.id", ondelete="CASCADE"), nullable=True, index=True)
    
    # Vector embedding (384 dimensiones - all-MiniLM-L6-v2)
    vector = Column(Vector(384), nullable=False, index=True)
    
    # Metadata
    created_at = Column(DateTime, default=func.now(), nullable=False)
    
    # Relaciones
    profile = relationship("Profile", backref="embeddings")
    required_profile = relationship("RequiredProfile", backref="embeddings")

    __table_args__ = (
        CheckConstraint(
            "(profile_id IS NOT NULL AND required_profile_id IS NULL) OR "
            "(profile_id IS NULL AND required_profile_id IS NOT NULL)",
            name="ck_embeddings_single_origin"
        ),
        UniqueConstraint("profile_id", name="uq_embeddings_profile"),
        UniqueConstraint("required_profile_id", name="uq_embeddings_required_profile")
    )

    
    def __repr__(self):
        return f"<Embedding(id={self.id}, profile_id={self.profile_id}, required_profile_id={self.required_profile_id})>"
