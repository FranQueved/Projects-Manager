#!/bin/bash
# Verificador de Instalación - Project Manager

echo "🔍 Verificando instalación de Project Manager..."
echo ""

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Contadores
TOTAL=0
PASSED=0

check() {
    TOTAL=$((TOTAL + 1))
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓${NC} $1"
        PASSED=$((PASSED + 1))
    else
        echo -e "${RED}✗${NC} $1"
    fi
}

# Verificaciones de Python
echo "📦 Verificaciones de Backend..."
which python3 > /dev/null 2>&1
check "Python 3 instalado"

which pip > /dev/null 2>&1
check "pip instalado"

# Verificaciones de Node
echo ""
echo "📦 Verificaciones de Frontend..."
which node > /dev/null 2>&1
check "Node.js instalado"

which npm > /dev/null 2>&1
check "npm instalado"

# Verificaciones de PostgreSQL
echo ""
echo "🗄️  Verificaciones de Base de Datos..."
which psql > /dev/null 2>&1
check "PostgreSQL instalado"

# Verificaciones de carpetas
echo ""
echo "📁 Verificaciones de Estructura..."
[ -d "backend" ]
check "Carpeta backend existe"

[ -d "frontend" ]
check "Carpeta frontend existe"

[ -f "backend/requirements.txt" ]
check "requirements.txt existe"

[ -f "frontend/package.json" ]
check "package.json existe"

[ -f "backend/.env.example" ]
check "Backend .env.example existe"

[ -f "frontend/.env" ]
check "Frontend .env existe"

# Verificaciones de archivos del backend
echo ""
echo "📄 Verificaciones de Archivos Backend..."
[ -f "backend/app/main.py" ]
check "main.py existe"

[ -f "backend/app/routers/employees.py" ]
check "employees.py router existe"

[ -f "backend/app/routers/projects.py" ]
check "projects.py router existe"

[ -f "backend/app/routers/assignments.py" ]
check "assignments.py router existe"

# Verificaciones de archivos del frontend
echo ""
echo "📄 Verificaciones de Archivos Frontend..."
[ -f "frontend/src/App.jsx" ]
check "App.jsx existe"

[ -f "frontend/src/context/AppContext.jsx" ]
check "AppContext.jsx existe"

[ -f "frontend/src/services/dataService.js" ]
check "dataService.js existe"

[ -d "frontend/src/components" ]
check "Carpeta components existe"

[ -d "frontend/src/pages" ]
check "Carpeta pages existe"

[ -d "frontend/src/styles" ]
check "Carpeta styles existe"

# Archivos de documentación
echo ""
echo "📚 Verificaciones de Documentación..."
[ -f "QUICKSTART.md" ]
check "QUICKSTART.md existe"

[ -f "SETUP.md" ]
check "SETUP.md existe"

[ -f "IMPLEMENTACION.md" ]
check "IMPLEMENTACION.md existe"

[ -f "NOTAS_TECNICAS.md" ]
check "NOTAS_TECNICAS.md existe"

# Resumen
echo ""
echo "================================"
echo "📊 RESUMEN DE VERIFICACIÓN"
echo "================================"
echo "Pruebas pasadas: $PASSED / $TOTAL"
echo ""

if [ $PASSED -eq $TOTAL ]; then
    echo -e "${GREEN}✓ ¡Todo está listo para desarrollar!${NC}"
    echo ""
    echo "Próximos pasos:"
    echo "1. cd backend && pip install -r requirements.txt"
    echo "2. cd frontend && npm install"
    echo "3. Ejecutar backend: python -m uvicorn app.main:app --reload"
    echo "4. Ejecutar frontend: npm start"
else
    echo -e "${YELLOW}⚠ Algunos verificadores fallaron${NC}"
    echo "Por favor, revisa la documentación en SETUP.md"
fi

echo ""
