from app.db.database import Base, engine
from app.models.epmloyees import Employee
from app.models.profile import  Profile
from app.models.project import Project
from app.models.employee_project import employee_project
from sqlalchemy import inspect



class InitDB:
    @staticmethod
    def create_tables():
        print("Verificando y creando tablas desde InitDB...")

        # Crear un inspector para verificar tablas existentes
        inspector = inspect(engine)

        # Obtener todas las tablas definidas en los modelos
        tables_to_create = Base.metadata.tables.keys()

        # Verificar cuáles tablas ya existen
        existing_tables = inspector.get_table_names()
        tables_to_create_filtered = [table for table in tables_to_create if table not in existing_tables]

        if tables_to_create_filtered:
            print(f"Creando {len(tables_to_create_filtered)} tabla(s) nueva(s): {', '.join(tables_to_create_filtered)}")
            # Crear solo las tablas que no existen
            Base.metadata.create_all(bind=engine, checkfirst=True)
            print("Tablas creadas correctamente.")
        else:
            print("Todas las tablas ya existen. No se creó ninguna tabla nueva.")




InitDB.create_tables()