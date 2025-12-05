/**
 * MÓDULO APP.JSX - COMPONENTE PRINCIPAL DE LA APLICACIÓN
 * ======================================================
 * 
 * Este es el componente raíz de toda la aplicación React. Sus responsabilidades son:
 * 
 * 1. ENRUTAMIENTO: Usa React Router para definir todas las rutas principales de la app.
 *    - Aquí se importan las páginas (Home, Dashboard, etc) y se asocian a rutas específicas.
 *    - El componente <Routes> renderiza la página correcta según la URL actual.
 * 
 * 2. ESTRUCTURA GENERAL: Define el layout general con header y main content.
 *    - El header contiene navegación y branding (aparece en todas las páginas).
 *    - El main contiene el contenido dinámico que cambia según la ruta.
 * 
 * 3. ENVOLVIMIENTO CON CONTEXTO: Aquí iría el AppProvider para compartir estado global.
 *    - Todos los componentes dentro del App pueden acceder al contexto global.
 * 
 * En resumen: App.jsx es el orquestador principal de la navegación y estructura visual.
 */

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';

// Importar páginas
// import Home from './pages/Home';
// import Dashboard from './pages/Dashboard';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1>Mi Proyecto</h1>
        </header>
        <main>
          <Routes>
            {/* <Route path="/" element={<Home />} />
            <Route path="/dashboard" element={<Dashboard />} /> */}
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
