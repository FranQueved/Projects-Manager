"""
Servicio para gestionar embeddings de perfiles de empleados con pgvector.
Genera y almacena embeddings en la tabla embedding_table usando PostgreSQL pgvector.
"""

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
    """
    Servicio para manejar embeddings de perfiles de empleados con pgvector.
    
    - Genera embeddings usando Sentence Transformers (384 dimensiones)
    - Almacena en PostgreSQL con el tipo Vector de pgvector
    - Permite búsquedas rápidas de similitud vectorial
    """

    def __init__(self):
        self.db: Session = SessionLocal()
        self.profile_service = ProfileService()
        self.employee_service = EmployeeService()

    def generate_embedding(self, text: str) -> Optional[List[float]]:
        """
        Genera un embedding a partir de un texto.
        
        Args:
            text: Texto a convertir en embedding
            
        Returns:
            List[float] o None: El embedding como lista de floats (384 dimensiones)
        """
        try:
            embedding = string_a_embedding(text)
            # Convertir a lista para retornar
            return embedding.tolist()
        except Exception as e:
            print(f"   Error generando embedding para texto: {e}")
            return None

    def create_embedding_for_employee(self, employee_id: int) -> bool:
        """
        Genera un embedding para un empleado basado en su perfil profesional.
        
        Usa Sentence Transformers para generar embeddings de 384 dimensiones
        y los almacena en PostgreSQL con pgvector.
        
        Args:
            employee_id: ID del empleado
            
        Returns:
            bool: True si se generó exitosamente, False si hubo error
        """
        try:
            # Obtener el perfil del empleado
            employee = self.employee_service.get_by_id(employee_id)
            if not employee or not employee.profile:
                print(f"   No se encontró empleado o perfil para ID: {employee_id}")
                return False

            # Convertir perfil a string
            profile_str = self.profile_service.toString(employee.profile.id)
            if not profile_str:
                print(f"   Perfil vacío para empleado {employee_id}")
                return False

            # Generar embedding (384 dimensiones, normalizado)
            embedding = string_a_embedding(profile_str)
            if embedding is None:
                print(f"   No se pudo generar embedding para empleado {employee_id}")
                return False

            # Primero, intentar eliminar embedding anterior si existe
            sql_delete = text("""
                DELETE FROM embeddings 
                WHERE profile_id = :profile_id
            """)
            self.db.execute(sql_delete, {"profile_id": employee.profile.id})

            # Guardar en tabla embeddings usando pgvector
            # Convertir el array a formato string compatible con pgvector: [1.0, 2.0, 3.0, ...]
            vector_str = "[" + ",".join(str(x) for x in embedding) + "]"
            sql_insert = text("""
                INSERT INTO embeddings (profile_id, vector, created_at)
                VALUES (:profile_id, CAST(:vector_str AS vector), NOW())
            """)

            self.db.execute(sql_insert, {"profile_id": employee.profile.id, "vector_str": vector_str})
            self.db.commit()

            return True

        except Exception as e:
            print(f"   Error generando embedding para empleado {employee_id}: {e}")
            import traceback
            traceback.print_exc()
            self.db.rollback()
            return False

    def create_embeddings_for_all_employees(self) -> int:
        """
        Genera embeddings para todos los empleados.
        
        Returns:
            int: Número de embeddings creados exitosamente
        """
        print("\n[*] Generando embeddings para todos los empleados...")
        print("=" * 60)

        all_employees = self.employee_service.get_all()
        success_count = 0

        for i, employee in enumerate(all_employees, 1):
            if self.create_embedding_for_employee(employee.id):
                success_count += 1
                if i % 10 == 0:
                    print(f"   [OK] Embeddings creados {i}/{len(all_employees)}")

        print(f"\n[OK] Embeddings creados exitosamente: {success_count}/{len(all_employees)}")
        return success_count

    def create_embedding_for_required_profile(self, required_profile_id: int) -> bool:
        """Genera y persiste el embedding de un perfil requerido asociado a un proyecto."""
        try:
            print(f"   [DEBUG] Buscando required_profile {required_profile_id}")
            required_profile = self.db.query(RequiredProfile).filter(RequiredProfile.id == required_profile_id).first()
            if not required_profile or not required_profile.project_id:
                print(f"   No se encontró perfil requerido con proyecto para ID: {required_profile_id}")
                return False

            print(f"   [DEBUG] Generando texto para required_profile {required_profile_id}")
            profile_text = " ".join(
                filter(None, [
                    required_profile.hard_skills,
                    required_profile.soft_skills,
                    required_profile.languages,
                ])
            )

            print(f"   [DEBUG] Generando embedding para required_profile {required_profile_id}")
            embedding = string_a_embedding(profile_text)
            if embedding is None:
                print(f"   No se pudo generar embedding para required_profile {required_profile_id}")
                return False

            sql_delete = text(
                """
                DELETE FROM embeddings 
                WHERE required_profile_id = :required_profile_id
                """
            )
            self.db.execute(sql_delete, {"required_profile_id": required_profile_id})

            vector_str = "[" + ",".join(str(x) for x in embedding) + "]"
            sql_insert = text(
                """
                INSERT INTO embeddings (required_profile_id, vector, created_at)
                VALUES (:required_profile_id, CAST(:vector_str AS vector), NOW())
                """
            )

            print(f"   [DEBUG] Insertando embedding para required_profile {required_profile_id}")
            self.db.execute(sql_insert, {
                "required_profile_id": required_profile_id,
                "vector_str": vector_str
            })
            self.db.commit()
            print(f"   [OK] Embedding de required_profile {required_profile_id} guardado")
            return True
        except Exception as e:
            print(f"   Error generando embedding para required_profile {required_profile_id}: {e}")
            import traceback
            traceback.print_exc()
            self.db.rollback()
            return False

    def create_embeddings_for_required_profiles(self) -> int:
        """Genera embeddings para todos los perfiles requeridos con proyecto asociado."""
        all_required = self.db.query(RequiredProfile).filter(RequiredProfile.project_id != None).all()  # noqa: E711
        print(f"   [DEBUG] Encontrados {len(all_required)} required_profiles para generar embeddings")
        success_count = 0

        for i, required_profile in enumerate(all_required, 1):
            print(f"   [DEBUG] Procesando required_profile {i}/{len(all_required)}, id={required_profile.id}")
            if self.create_embedding_for_required_profile(required_profile.id):
                success_count += 1
                if i % 10 == 0:
                    print(f"   [OK] Embeddings de required_profiles {i}/{len(all_required)}")

        print(f"   [DEBUG] Total embeddings de required_profiles creados: {success_count}")
        return success_count

    def get_employee_embedding(self, employee_id: int) -> Optional[np.ndarray]:
        """
        Obtiene el embedding de un empleado desde pgvector.
        
        Args:
            employee_id: ID del empleado
            
        Returns:
            np.ndarray o None: El embedding si existe (384 dimensiones)
        """
        try:
            # Obtener el perfil del empleado
            employee = self.employee_service.get_by_id(employee_id)
            if not employee or not employee.profile:
                return None

            sql = text("""
                SELECT vector FROM embeddings
                WHERE profile_id = :profile_id
            """)
            result = self.db.execute(sql, {"profile_id": employee.profile.id}).first()

            if result:
                # pgvector devuelve el vector como una lista o objeto vector
                vector_data = result[0]
                if isinstance(vector_data, (list, tuple)):
                    return np.array(vector_data, dtype=np.float32)
                else:
                    # Si es un objeto Vector de pgvector, convertir a array
                    return np.array(list(vector_data), dtype=np.float32)
            return None

        except Exception as e:
            print(f"Error obteniendo embedding: {e}")
            return None

    def find_similar_employees(self, employee_id: int, top_k: int = 5) -> List[tuple]:
        """
        Encuentra empleados con perfiles similares usando pgvector.
        
        Utiliza el operador <=> (distancia euclidiana) o <#> (similitud coseno negativa)
        para búsquedas rápidas de vecinos más cercanos.
        
        Args:
            employee_id: ID del empleado de referencia
            top_k: Número de resultados similares a retornar
            
        Returns:
            List[tuple]: Lista de (employee_id, similarity_score)
        """
        try:
            # Obtener el perfil del empleado
            employee = self.employee_service.get_by_id(employee_id)
            if not employee or not employee.profile:
                return []

            # PostgreSQL con pgvector: usando <=> para distancia euclidiana
            # Para similitud coseno normalizada, usar 1 - (vector <#> vector_ref)
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
            print(f"Error buscando empleados similares: {e}")
            return []

    def find_similar_employees_by_text(self, text: str, top_k: int = 5) -> List[tuple]:
        """
        Encuentra empleados similares a un texto dado.
        
        Genera un embedding del texto y busca los empleados más similares.
        Útil para búsquedas por skill, descripción, etc.
        
        Args:
            text: Texto a buscar (skill, descripción, etc.)
            top_k: Número de resultados similares a retornar
            
        Returns:
            List[tuple]: Lista de (employee_id, similarity_score)
        """
        try:
            # Generar embedding del texto
            embedding = string_a_embedding(text)
            
            # Buscar empleados similares
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
            print(f"Error buscando por texto: {e}")

    def close(self):
        """Cierra la sesión de base de datos."""
        self.db.close()
        self.profile_service.close()
        self.employee_service.close()
