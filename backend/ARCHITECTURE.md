# Project Manager API - Backend

FastAPI backend for project management system with employee-project allocation and semantic search using pgvector embeddings.

## Project Structure

```
backend/
├── app/
│   ├── db/                          # Database configuration
│   │   ├── database.py              # SQLAlchemy setup, engine, sessions
│   │   └── create_tables.py         # Database initialization
│   ├── models/                      # SQLAlchemy ORM models
│   │   ├── employee.py              # Employee model (1-1 with Profile)
│   │   ├── profile.py               # Professional profile model
│   │   ├── project.py               # Project model
│   │   ├── required_profile.py      # Required skills for projects (1-N)
│   │   ├── embedding.py             # Vector embeddings storage
│   │   └── employee_project.py      # M-N relationship table
│   ├── schemas/                     # Pydantic request/response schemas
│   │   ├── employee.py
│   │   ├── profile.py
│   │   └── project.py
│   ├── services/
│   │   ├── service_layer/           # Business logic services
│   │   │   ├── employee_service.py
│   │   │   ├── profile_service.py
│   │   │   ├── project_service.py
│   │   │   ├── employee_project_service.py
│   │   │   └── required_profile_service.py
│   │   ├── vectorial_services/      # Embedding generation
│   │   │   ├── embeding_creator.py  # Sentence Transformers wrapper
│   │   │   └── embedding_service.py
│   │   └── fixtures/                # Database seeding
│   │       ├── seed_service.py
│   │       ├── seed_data.py
│   │       └── populate_database.py
│   ├── routers/                     # API endpoints (future)
│   └── main.py                      # FastAPI application entry
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## Key Features

- **Employee Management**: Create and manage employees with professional profiles
- **Project Management**: Track projects with team assignments
- **Vector Embeddings**: 384-dimensional embeddings using Sentence Transformers (all-MiniLM-L6-v2)
- **Semantic Search**: Enable matching between employee skills and project requirements using pgvector
- **Database Relationships**:
  - Employee ↔ Profile: 1-to-1 (mandatory)
  - Project ↔ RequiredProfile: 1-to-N
  - Employee ↔ Project: M-to-N

## Technology Stack

- **Framework**: FastAPI
- **ORM**: SQLAlchemy 2.x
- **Database**: PostgreSQL with pgvector extension
- **Embeddings**: Sentence Transformers (all-MiniLM-L6-v2, 384-dimensional)
- **Validation**: Pydantic v2

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure database:
   - Update `DATABASE_URL` in `app/db/database.py` with your PostgreSQL connection string
   - Ensure pgvector extension is installed

3. Initialize database:
```bash
python -m app.db.create_tables
```

## Database Seeding

Populate the database with test data:

```bash
cd backend
python -m app.services.fixtures.populate_database
```

This will create:
- 100 profiles
- 100 employees (each with a profile)
- 30 projects
- Random employee-project assignments
- 1-4 required profiles per project
- Vector embeddings for both employee profiles and required profiles

## Running the API

```bash
cd backend
python -m uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`

## Service Layer

All business logic is encapsulated in service classes:

- `ProfileService`: Profile CRUD operations
- `EmployeeService`: Employee CRUD with profile validation
- `ProjectService`: Project CRUD and filtering
- `EmployeeProjectService`: Manage employee-project assignments
- `RequiredProfileService`: Manage required profiles for projects

## Embeddings

The `embeding_creator.py` module generates 384-dimensional normalized embeddings using Sentence Transformers. Embeddings are:
- Normalized for cosine similarity
- Stored in PostgreSQL with pgvector
- Generated for all employee profiles and required project profiles
- Used for semantic search and skill-matching

## Development

Code follows these conventions:
- Professional English docstrings
- Type hints for all functions
- Clean separation of concerns
- Proper error handling
- Database session management

## Notes

- All timestamps are UTC
- Embeddings use 384 dimensions (all-MiniLM-L6-v2 model)
- Vector storage uses pgvector extension in PostgreSQL
- All relationships enforce referential integrity with CASCADE delete
