# ⚡ Inicio Rápido - Project Manager

## 🎯 Para ejecutar la aplicación completamente:

### Terminal 1 - Backend (FastAPI)
```bash
cd backend

# Activar entorno virtual
venv\Scripts\activate  # Windows
# o
source venv/bin/activate  # Linux/Mac

# Instalar dependencias (si es la primera vez)
pip install -r requirements.txt

# Inicializar base de datos (si es la primera vez)
python -m app.db.create_tables

# Opcionalmente: cargar datos de ejemplo
python -m app.services.fixtures.populate_database

# Ejecutar servidor
python -m uvicorn app.main:app --reload
```

**API disponible en:** `http://localhost:8000`
**Documentación:** `http://localhost:8000/docs`

---

### Terminal 2 - Frontend (React)
```bash
cd frontend

# Instalar dependencias (si es la primera vez)
npm install

# Ejecutar servidor de desarrollo
npm start
```

**Aplicación disponible en:** `http://localhost:3000`

---

## ✅ Checklist Inicial

- [ ] PostgreSQL está corriendo
- [ ] Entorno virtual del backend está activado
- [ ] Backend corriendo en terminal 1
- [ ] Frontend corriendo en terminal 2
- [ ] Puedes acceder a `http://localhost:3000`

## 🎮 Prueba la aplicación

1. Ve a `http://localhost:3000`
2. Navega a "Dashboard"
3. Crea un nuevo empleado en "Empleados"
4. Crea un nuevo proyecto en "Proyectos"
5. ¡Listo!

## 📝 Variables de Entorno

### Backend (.env)
```env
DATABASE_URL=postgresql://user:password@localhost:5432/project_manager
```

### Frontend (.env)
```env
REACT_APP_API_URL=http://localhost:8000
```

---

Para más información, ver [SETUP.md](./SETUP.md)
