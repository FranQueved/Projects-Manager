"""Embedding service - Generate and manage profile vectors with pgvector."""

from typing import Optional, List
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services.vectorial_services.embeding_creator import string_a_embedding
from app.models.required_profile import RequiredProfile


class EmbeddingService:
    """Service for managing employee profile embeddings using pgvector."""

    def __init__(self):
        self.db: Session = SessionLocal()

    def generate_embedding(self, text: str) -> Optional[List[float]]:
        """Generate 384-dimensional embedding from text."""
        try:
            embedding = string_a_embedding(text)
            return embedding.tolist()
        except Exception as e:
            print(f"   Error generating embedding: {e}")
            return None

    def create_embedding_for_employee(self, employee_id: int) -> bool:
        """Create embedding for employee profile and store in pgvector."""
        try:
            from app.models.employee import Employee
            employee = self.db.query(Employee).filter(Employee.id == employee_id).first()
            if not employee or not employee.profile:
                print(f"   Employee or profile not found: {employee_id}")
                return False

            profile_str = " ".join(filter(None, [
                employee.profile.hard_skills,
                employee.profile.soft_skills,
                employee.profile.languages,
            ]))
            
            if not profile_str:
                print(f"   Empty profile for employee {employee_id}")
                return False

            embedding = string_a_embedding(profile_str)
            if embedding is None:
                print(f"   Failed to generate embedding for employee {employee_id}")
                return False

            sql_delete = text("""DELETE FROM embeddings WHERE profile_id = :profile_id""")
            self.db.execute(sql_delete, {"profile_id": employee.profile.id})

            vector_str = "[" + ",".join(str(x) for x in embedding) + "]"
            sql_insert = text("""
                INSERT INTO embeddings (profile_id, vector, created_at)
                VALUES (:profile_id, CAST(:vector_str AS vector), NOW())
            """)

            self.db.execute(sql_insert, {"profile_id": employee.profile.id, "vector_str": vector_str})
            self.db.commit()
            return True

        except Exception as e:
            print(f"   Error generating embedding for employee {employee_id}: {e}")
            self.db.rollback()
            return False

    def create_embedding_for_required_profile(self, required_profile_id: int) -> bool:
        """Create embedding for required profile and store in pgvector."""
        try:
            required_profile = self.db.query(RequiredProfile).filter(
                RequiredProfile.id == required_profile_id
            ).first()
            if not required_profile or not required_profile.project_id:
                print(f"   Required profile not found: {required_profile_id}")
                return False

            profile_text = " ".join(
                filter(None, [
                    required_profile.hard_skills,
                    required_profile.soft_skills,
                    required_profile.languages,
                ])
            )

            embedding = string_a_embedding(profile_text)
            if embedding is None:
                print(f"   Failed to generate embedding for required profile {required_profile_id}")
                return False

            sql_delete = text(
                "DELETE FROM embeddings WHERE required_profile_id = :required_profile_id"
            )
            self.db.execute(sql_delete, {"required_profile_id": required_profile_id})

            vector_str = "[" + ",".join(str(x) for x in embedding) + "]"
            sql_insert = text("""
                INSERT INTO embeddings (required_profile_id, vector, created_at)
                VALUES (:required_profile_id, CAST(:vector_str AS vector), NOW())
            """)

            self.db.execute(sql_insert, {
                "required_profile_id": required_profile_id,
                "vector_str": vector_str
            })
            self.db.commit()
            return True
        except Exception as e:
            print(f"   Error generating embedding for required profile {required_profile_id}: {e}")
            self.db.rollback()
            return False

    def close(self):
        """Close database session."""
        self.db.close()
