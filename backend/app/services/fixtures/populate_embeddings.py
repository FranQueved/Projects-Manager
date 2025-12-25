"""Embedding population utility - Generate embeddings for all profiles."""

import time
from app.services.vectorial_services.embedding_service import EmbeddingService


def populate_embeddings() -> bool:
    """Generate and store embeddings for all employees and required profiles."""
    print("\n" + "=" * 70)
    print("POPULATING EMBEDDING TABLE")
    print("=" * 70)

    service = EmbeddingService()
    start_time = time.time()

    try:
        count = service.create_embeddings_for_all_employees()
        elapsed_time = time.time() - start_time

        print(f"\n" + "=" * 70)
        print(f"RESULT:")
        print(f"  Embeddings created: {count}")
        print(f"  Total time: {elapsed_time:.2f} seconds")
        print(f"=" * 70 + "\n")

        return True

    except Exception as e:
        print(f"Error: {e}")
        return False

    finally:
        service.close()


if __name__ == "__main__":
    populate_embeddings()
    success = populate_embeddings()
    exit(0 if success else 1)
