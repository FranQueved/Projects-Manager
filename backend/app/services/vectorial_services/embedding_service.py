"""Embedding service - Generate and manage profile vectors with pgvector."""

from typing import Optional, List
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services.vectorial_services.embeding_creator import string_a_embedding
from app.services.service_layer.profile_service import ProfileService
from app.services.service_layer.employee_service import EmployeeService
from app.models.required_profile import RequiredProfile
import numpy as np


class EmbeddingService:
    """Service for managing employee profile embeddings using pgvector."""

    def __init__(self):
        self.db: Session = SessionLocal()
        self.profile_service = ProfileService()
        self.employee_service = EmployeeService()

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
            employee = self.employee_service.get_by_id(employee_id)
            if not employee or not employee.profile:
                print(f"   Employee or profile not found: {employee_id}")
                return False

            profile_str = self.profile_service.toString(employee.profile.id)
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

    def create_embeddings_for_all_employees(self) -> int:
        """Generate embeddings for all employees."""
        print("\n[*] Generating embeddings for all employees...")
        print("=" * 60)

        all_employees = self.employee_service.get_all()
        success_count = 0

        for i, employee in enumerate(all_employees, 1):
            if self.create_embedding_for_employee(employee.id):
                success_count += 1
                if i % 10 == 0:
                    print(f"   [OK] Embeddings created {i}/{len(all_employees)}")

        print(f"\n[OK] Successfully created {success_count}/{len(all_employees)} embeddings")
        return success_count

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

    def create_embeddings_for_required_profiles(self) -> int:
        """Generate embeddings for all required profiles."""
        all_required = self.db.query(RequiredProfile).filter(
            RequiredProfile.project_id != None  # noqa: E711
        ).all()
        success_count = 0

        for i, required_profile in enumerate(all_required, 1):
            if self.create_embedding_for_required_profile(required_profile.id):
                success_count += 1
                if i % 10 == 0:
                    print(f"   [OK] Embeddings created {i}/{len(all_required)}")

        return success_count

    def get_employee_embedding(self, employee_id: int) -> Optional[np.ndarray]:
        """Get embedding vector for employee from pgvector."""
        try:
            employee = self.employee_service.get_by_id(employee_id)
            if not employee or not employee.profile:
                return None

            sql = text("SELECT vector FROM embeddings WHERE profile_id = :profile_id")
            result = self.db.execute(sql, {"profile_id": employee.profile.id}).first()

            if result:
                vector_data = result[0]
                if isinstance(vector_data, (list, tuple)):
                    return np.array(vector_data, dtype=np.float32)
                else:
                    return np.array(list(vector_data), dtype=np.float32)
            return None

        except Exception as e:
            print(f"Error retrieving embedding: {e}")
            return None

    def find_similar_employees(self, employee_id: int, top_k: int = 5) -> List[tuple]:
        """Find similar employees using pgvector cosine similarity."""
        try:
            employee = self.employee_service.get_by_id(employee_id)
            if not employee or not employee.profile:
                return []

            sql = text("""
                SELECT e.id as employee_id, 
                       1 - (emb.vector <#> (
                           SELECT vector FROM embeddings 
                           WHERE profile_id = :profile_id
                       )) as similarity
                FROM embeddings emb
                JOIN employees e ON e.profile_id = emb.profile_id
                WHERE emb.profile_id != :profile_id
                ORDER BY similarity DESC
                LIMIT :top_k
            """)

            results = self.db.execute(
                sql,
                {"profile_id": employee.profile.id, "top_k": top_k}
            ).fetchall()

            return [(row[0], float(row[1])) for row in results]

        except Exception as e:
            print(f"Error finding similar employees: {e}")
            return []

    def find_similar_employees_by_text(self, text: str, top_k: int = 5) -> List[tuple]:
        """Find similar employees matching text query."""
        try:
            embedding = string_a_embedding(text)
            sql = text("""
                SELECT e.id as employee_id, 
                       1 - (emb.vector <#> :search_vector::vector) as similarity
                FROM embeddings emb
                JOIN employees e ON e.profile_id = emb.profile_id
                ORDER BY similarity DESC
                LIMIT :top_k
            """)

            results = self.db.execute(
                sql,
                {"search_vector": embedding.tolist(), "top_k": top_k}
            ).fetchall()

            return [(row[0], float(row[1])) for row in results]

        except Exception as e:
            print(f"Error searching by text: {e}")

    def close(self):
        """Close database session and related services."""
        self.db.close()
        self.profile_service.close()
        self.employee_service.close()
