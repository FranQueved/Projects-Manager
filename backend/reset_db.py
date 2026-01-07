"""Reset database - drop all tables and recreate them empty."""

from sqlalchemy import inspect
from app.db.database import Base, engine
from app.models.employee import Employee
from app.models.profile import Profile
from app.models.project import Project
from app.models.embedding import Embedding
from app.models.required_profile import RequiredProfile
from app.models.employee_project import employee_project

print("=" * 60)
print("RESETEANDO BASE DE DATOS")
print("=" * 60)

# Drop all tables
try:
    print("\n[1] Eliminando todas las tablas...")
    Base.metadata.drop_all(bind=engine)
    print("✓ Todas las tablas eliminadas")
except Exception as e:
    print(f"✗ Error al eliminar tablas: {e}")
    exit(1)

# Create all tables
try:
    print("\n[2] Creando tablas vacías...")
    Base.metadata.create_all(bind=engine)
    
    # Verify tables
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print(f"✓ Tablas creadas: {', '.join(tables)}")
except Exception as e:
    print(f"✗ Error al crear tablas: {e}")
    exit(1)

print("\n" + "=" * 60)
print("✓ Base de datos reseteada correctamente")
print("  - Todas las tablas eliminadas")
print("  - Nuevas tablas creadas vacías")
print("=" * 60)
