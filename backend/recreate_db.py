from app.db.database import Base, engine
from app.models.employee import Employee
from app.models.profile import Profile
from app.models.project import Project
from app.models.embedding import Embedding
from app.models.required_profile import RequiredProfile
from app.models.employee_project import employee_project

def recreate_tables():
    print("Eliminando todas las tablas...")
    Base.metadata.drop_all(bind=engine)
    print("Tablas eliminadas.")
    
    print("Creando todas las tablas...")
    Base.metadata.create_all(bind=engine)
    print("Tablas creadas exitosamente.")

if __name__ == "__main__":
    recreate_tables()
