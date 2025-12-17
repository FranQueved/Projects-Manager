"""
Servicio para gestionar embeddings de perfiles de empleados.
Genera y almacena embeddings en la tabla embedding_table.
"""

from typing import Optional, List
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.services.vectorial_services.embeding_creator import string_a_embedding
from app.services.service_layer.profile_service import ProfileService
from app.services.service_layer.employee_service import EmployeeService
import numpy as np


class EmbeddingService:
    """
    Servicio para manejar embeddings de perfiles de empleados.
    Genera embeddings a partir de los skills del perfil y los almacena en la BD.
    """

    def __init__(self):
        self.db: Session = SessionLocal()
        self.profile_service = ProfileService()
        self.employee_service = EmployeeService()

    def create_embedding_for_employee(self, employee_id: int) -> bool:
        """
        Genera un embedding para un empleado basado en su perfil profesional.
        
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

            # Generar embedding
            embedding = string_a_embedding(profile_str)

            # Convertir a lista para almacenar en BD
            embedding_list = embedding.tolist()

            # Primero, intentar eliminar embedding anterior si existe
            sql_delete = text("""
                DELETE FROM embeding_table 
                WHERE id_employee = :employee_id
            """)
            self.db.execute(sql_delete, {"employee_id": employee_id})

            # Guardar en tabla embedding_table
            sql_insert = text("""
                INSERT INTO embeding_table (id_employee, vector)
                VALUES (:employee_id, :vector)
            """)

            # PostgreSQL requiere que el array se envíe como string o como lista
            self.db.execute(sql_insert, {"employee_id": employee_id, "vector": embedding_list})
            self.db.commit()

            return True

        except Exception as e:
            print(f"   Error generando embedding para empleado {employee_id}: {e}")
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

    def get_employee_embedding(self, employee_id: int) -> Optional[np.ndarray]:
        """
        Obtiene el embedding de un empleado.
        
        Args:
            employee_id: ID del empleado
            
        Returns:
            np.ndarray o None: El embedding si existe
        """
        try:
            sql = text("""
                SELECT vector FROM embeding_table
                WHERE id_employee = :employee_id
            """)
            result = self.db.execute(sql, {"employee_id": employee_id}).first()

            if result:
                return np.array(result[0], dtype=np.float32)
            return None

        except Exception as e:
            print(f"Error obteniendo embedding: {e}")
            return None

    def find_similar_employees(self, employee_id: int, top_k: int = 5) -> List[tuple]:
        """
        Encuentra empleados con perfiles similares usando similitud coseno.
        
        Args:
            employee_id: ID del empleado de referencia
            top_k: Número de resultados similares a retornar
            
        Returns:
            List[tuple]: Lista de (employee_id, similarity_score)
        """
        try:
            # PostgreSQL con pgvector usa el operador <-> para distancia euclidiana
            # o <#> para similitud coseno negativa
            sql = text("""
                SELECT id_employee, 
                       1 - (vector <#> (
                           SELECT vector FROM embeding_table 
                           WHERE id_employee = :employee_id
                       )) as similarity
                FROM embeding_table
                WHERE id_employee != :employee_id
                ORDER BY similarity DESC
                LIMIT :top_k
            """)

            results = self.db.execute(
                sql,
                {"employee_id": employee_id, "top_k": top_k}
            ).fetchall()

            return [(row[0], row[1]) for row in results]

        except Exception as e:
            print(f"Error buscando empleados similares: {e}")
            return []

    def close(self):
        """Cierra la sesión de base de datos."""
        self.db.close()
        self.profile_service.close()
        self.employee_service.close()
