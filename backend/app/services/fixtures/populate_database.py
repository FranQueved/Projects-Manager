"""Database population script - Entry point for seeding database with test data."""

from app.services.fixtures.seed_service import seed_all


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("DATABASE POPULATION SCRIPT")
    print("=" * 70)
    print("\nThis script will create:")
    print("  [x] Database tables")
    print("  [x] 100 employees with profiles")
    print("  [x] 30 projects")
    print("  [x] Employee-project assignments")
    print("  [x] Required profiles (1-4 per project)")
    print("  [x] Vector embeddings for profiles")
    print("  [x] Vector embeddings for employees")
    print("  [x] Vector embeddings for required profiles")
    print("\n" + "=" * 70 + "\n")

    success = seed_all(include_embeddings=True)

    if success:
        print("\n[SUCCESS] Database population completed")
        print("   Database is ready to use")
        print("   [OK] Tables created")
        print("   [OK] Test data populated")
        print("   [OK] All embeddings generated")
        exit(0)
    else:
        print("\n[ERROR] Population failed")
        print("   Check errors above")
        exit(1)
