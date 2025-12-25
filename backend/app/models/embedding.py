"""
Embedding Model - Stores vectorial embeddings for semantic search using pgvector.
"""

from sqlalchemy import Column, Integer, ForeignKey, DateTime, func, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from app.db.database import Base


class Embedding(Base):
    """Vectorial embeddings for semantic search (384-dim, all-MiniLM-L6-v2)."""
    
    __tablename__ = "embeddings"

    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id", ondelete="CASCADE"), nullable=True, index=True)
    required_profile_id = Column(Integer, ForeignKey("required_profiles.id", ondelete="CASCADE"), nullable=True, index=True)
    vector = Column(Vector(384), nullable=False, index=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)

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
        return f"<Embedding(id={self.id}, profile_id={self.profile_id}, req_profile_id={self.required_profile_id})>"
