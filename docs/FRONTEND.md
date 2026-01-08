#  Frontend - Project Manager

Documentación de los componentes React del proyecto.

---

##  Estructura

\\\
frontend/src/
 components/
    Alert.jsx       # Alertas
    Button.jsx      # Botones
    Card.jsx        # Tarjetas
    Form.jsx        # Formularios
    Modal.jsx       # Diálogos
    Table.jsx       # Tablas

 pages/
    Home.jsx        # Inicio
    Dashboard.jsx   # Dashboard
    Employees.jsx   # Gestión empleados
    Projects.jsx    # Gestión proyectos

 services/
    api.js          # Configuración Axios
    dataService.js  # Llamadas API

 context/
    AppContext.jsx  # Estado global

 hooks/
    useFetch.js     # Hook para fetching

 App.jsx             # Root component
\\\

---

##  Componentes Principales

### Alert
Mostrar mensajes (success, error, warning)
\\\jsx
<Alert type=\"success\" message=\"Creado exitosamente!\" />
\\\

### Button
Botones reutilizables
\\\jsx
<Button variant=\"primary\" size=\"lg\">Guardar</Button>
\\\

### Table
Tablas de datos
\\\jsx
<Table columns={columns} data={employees} onEdit={handleEdit} />
\\\

### Form
Formularios con validación
\\\jsx
<Form fields={fields} onSubmit={handleSubmit} />
\\\

### Modal
Diálogos
\\\jsx
<Modal isOpen={open} onClose={handleClose}>Contenido</Modal>
\\\

---

##  Hook useFetch

Para obtener datos del backend:
\\\jsx
const { data, loading, error } = useFetch('/employees');
\\\

---

##  Servicios HTTP

dataService proporciona métodos para todas las operaciones:

- \getEmployees()\ - Obtener empleados
- \createEmployee(data)\ - Crear empleado
- \updateEmployee(id, data)\ - Actualizar
- \deleteEmployee(id)\ - Eliminar
- \getProjects()\ - Obtener proyectos
- \ssignEmployee(empId, projId)\ - Asignar empleado a proyecto
- \getRecommendedEmployees(projId)\ - Obtener recomendaciones

---

##  Rutas

- \/\ - Inicio
- \/dashboard\ - Dashboard
- \/employees\ - Gestión empleados
- \/projects\ - Gestión proyectos

---

##  Estilos

Usar CSS Modules en \styles/\ carpeta.
\\\jsx
import styles from './Component.module.css';
<div className={styles.container}>...</div>
\\\

---

**Última actualización:** Enero 2026
