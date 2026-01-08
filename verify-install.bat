@echo off
REM Verificador de Instalación - Project Manager (Windows)

echo.
echo ========================================
echo   Verificando instalación del Proyecto
echo ========================================
echo.

setlocal enabledelayedexpansion

set PASSED=0
set TOTAL=0

REM Función para verificar
:check_item
set /a TOTAL+=1
where /q %1 >nul 2>nul
if %errorlevel% equ 0 (
    echo [OK] %2
    set /a PASSED+=1
) else (
    echo [FAIL] %2
)
goto :eof

REM Verificaciones de Python
echo Verificaciones de Backend:
call :check_item python "Python 3 instalado"
call :check_item pip "pip instalado"

echo.
echo Verificaciones de Frontend:
call :check_item node "Node.js instalado"
call :check_item npm "npm instalado"

echo.
echo Verificaciones de Base de Datos:
call :check_item psql "PostgreSQL instalado"

echo.
echo Verificaciones de Estructura:
if exist "backend" (
    echo [OK] Carpeta backend existe
    set /a PASSED+=1
) else (
    echo [FAIL] Carpeta backend existe
)
set /a TOTAL+=1

if exist "frontend" (
    echo [OK] Carpeta frontend existe
    set /a PASSED+=1
) else (
    echo [FAIL] Carpeta frontend existe
)
set /a TOTAL+=1

if exist "backend\requirements.txt" (
    echo [OK] requirements.txt existe
    set /a PASSED+=1
) else (
    echo [FAIL] requirements.txt existe
)
set /a TOTAL+=1

if exist "frontend\package.json" (
    echo [OK] package.json existe
    set /a PASSED+=1
) else (
    echo [FAIL] package.json existe
)
set /a TOTAL+=1

echo.
echo Verificaciones de Archivos Backend:
if exist "backend\app\main.py" (
    echo [OK] main.py existe
    set /a PASSED+=1
) else (
    echo [FAIL] main.py existe
)
set /a TOTAL+=1

if exist "backend\app\routers\employees.py" (
    echo [OK] employees.py router existe
    set /a PASSED+=1
) else (
    echo [FAIL] employees.py router existe
)
set /a TOTAL+=1

if exist "backend\app\routers\projects.py" (
    echo [OK] projects.py router existe
    set /a PASSED+=1
) else (
    echo [FAIL] projects.py router existe
)
set /a TOTAL+=1

if exist "backend\app\routers\assignments.py" (
    echo [OK] assignments.py router existe
    set /a PASSED+=1
) else (
    echo [FAIL] assignments.py router existe
)
set /a TOTAL+=1

echo.
echo Verificaciones de Archivos Frontend:
if exist "frontend\src\App.jsx" (
    echo [OK] App.jsx existe
    set /a PASSED+=1
) else (
    echo [FAIL] App.jsx existe
)
set /a TOTAL+=1

if exist "frontend\src\context\AppContext.jsx" (
    echo [OK] AppContext.jsx existe
    set /a PASSED+=1
) else (
    echo [FAIL] AppContext.jsx existe
)
set /a TOTAL+=1

if exist "frontend\src\services\dataService.js" (
    echo [OK] dataService.js existe
    set /a PASSED+=1
) else (
    echo [FAIL] dataService.js existe
)
set /a TOTAL+=1

if exist "frontend\src\components" (
    echo [OK] Carpeta components existe
    set /a PASSED+=1
) else (
    echo [FAIL] Carpeta components existe
)
set /a TOTAL+=1

if exist "frontend\src\pages" (
    echo [OK] Carpeta pages existe
    set /a PASSED+=1
) else (
    echo [FAIL] Carpeta pages existe
)
set /a TOTAL+=1

if exist "frontend\src\styles" (
    echo [OK] Carpeta styles existe
    set /a PASSED+=1
) else (
    echo [FAIL] Carpeta styles existe
)
set /a TOTAL+=1

echo.
echo Verificaciones de Documentación:
if exist "QUICKSTART.md" (
    echo [OK] QUICKSTART.md existe
    set /a PASSED+=1
) else (
    echo [FAIL] QUICKSTART.md existe
)
set /a TOTAL+=1

if exist "SETUP.md" (
    echo [OK] SETUP.md existe
    set /a PASSED+=1
) else (
    echo [FAIL] SETUP.md existe
)
set /a TOTAL+=1

if exist "IMPLEMENTACION.md" (
    echo [OK] IMPLEMENTACION.md existe
    set /a PASSED+=1
) else (
    echo [FAIL] IMPLEMENTACION.md existe
)
set /a TOTAL+=1

if exist "NOTAS_TECNICAS.md" (
    echo [OK] NOTAS_TECNICAS.md existe
    set /a PASSED+=1
) else (
    echo [FAIL] NOTAS_TECNICAS.md existe
)
set /a TOTAL+=1

echo.
echo ========================================
echo   RESUMEN DE VERIFICACIÓN
echo ========================================
echo Pruebas pasadas: %PASSED% / %TOTAL%
echo.

if %PASSED% equ %TOTAL% (
    echo ✓ ¡Todo está listo para desarrollar!
    echo.
    echo Próximos pasos:
    echo 1. cd backend ^&^& pip install -r requirements.txt
    echo 2. cd frontend ^&^& npm install
    echo 3. Ejecutar backend: python -m uvicorn app.main:app --reload
    echo 4. Ejecutar frontend: npm start
) else (
    echo ⚠ Algunos verificadores fallaron
    echo Por favor, revisa la documentación en SETUP.md
)

echo.
pause
