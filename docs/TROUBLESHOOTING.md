#  Troubleshooting

Solución de problemas comunes en Project Manager.

---

##  Base de Datos

### PostgreSQL no inicia

´´´bash
# Windows
Start-Service postgresql-x64-15

# macOS
brew services start postgresql@15

# Linux
sudo systemctl start postgresql
´´´

### Error: pgvector extension not found

´´´bash
psql -U postgres -d project_manager
CREATE EXTENSION vector;
´´´

### Error: Connection refused

Verificar que PostgreSQL está corriendo en puerto 5432 y que DATABASE_URL es correcto en .env.

---

##  Backend (Python/FastAPI)

### ModuleNotFoundError

´´´bash
pip install -r requirements.txt
´´´

### Port 8000 already in use

´´´bash
uvicorn app.main:app --port 8001
´´´

### CORS error en navegador

Verificar que http://localhost:3000 está en CORS_ORIGINS en pp/main.py.

---

##  Frontend (React)

### Cannot find module

´´´bash
npm install
´´´

### API not responding

1. Verificar que backend corre en http://localhost:8000
2. Verificar REACT_APP_API_URL en .env

### Página en blanco

Abrir F12  Console para ver errores.

---

##  Datos y Embeddings

### Sin embeddings generados

´´´bash
python populate_db.py
´´´

### Recomendaciones vacías

Verificar que existen empleados y proyectos con perfiles.

---

##  Reset Total

´´´bash
cd backend
python reset_db.py
python populate_db.py
´´´
