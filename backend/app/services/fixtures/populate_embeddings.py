"""
Script para generar y almacenar embeddings de perfiles de empleados.

Este script es parte del módulo de fixtures y genera embeddings vectoriales
para todos los empleados de la base de datos.
"""

import time
from app.services.vectorial_services.embedding_service import EmbeddingService


def populate_embeddings():
    """
    Genera y almacena embeddings para todos los empleados en la BD.

    Returns:
        bool: True si se completó exitosamente, False en caso de error
    """
    print("\n" + "=" * 70)
    print("LLENANDO TABLA DE EMBEDDINGS CON PERFILES DE EMPLEADOS")
    print("=" * 70)

    service = EmbeddingService()
    start_time = time.time()

    try:
        # Generar embeddings para todos los empleados
        count = service.create_embeddings_for_all_employees()

        elapsed_time = time.time() - start_time

        print(f"\n" + "=" * 70)
        print(f"RESULTADO:")
        print(f"  Embeddings creados: {count}")
        print(f"  Tiempo total: {elapsed_time:.2f} segundos")
        print(f"=" * 70 + "\n")

        return True

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return False

    finally:
        service.close()


if __name__ == "__main__":
    success = populate_embeddings()
    exit(0 if success else 1)
