"""Database table initialization."""

from sqlalchemy import inspect
from app.db.database import Base, engine
from app.models.employee import Employee
from app.models.profile import Profile
from app.models.project import Project
from app.models.embedding import Embedding
from app.models.required_profile import RequiredProfile
from app.models.employee_project import employee_project


class InitDB:
    """Database initialization utility."""

    @staticmethod
    def create_tables():
        """Create database tables if they don't exist."""
        print("Initializing database tables...")

        inspector = inspect(engine)
        tables_to_create = Base.metadata.tables.keys()
        existing_tables = inspector.get_table_names()
        tables_to_create_filtered = [
            table for table in tables_to_create if table not in existing_tables
        ]

        if tables_to_create_filtered:
            print(f"Creating {len(tables_to_create_filtered)} new table(s): {', '.join(tables_to_create_filtered)}")
            Base.metadata.create_all(bind=engine, checkfirst=True)
            print("Tables created successfully.")
        else:
            print("All tables already exist.")


InitDB.create_tables()