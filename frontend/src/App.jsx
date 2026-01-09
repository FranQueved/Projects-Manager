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

import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { AppProvider } from './context/AppContext';
import { Home } from './pages/Home';
import { Dashboard } from './pages/Dashboard';
import { Employees } from './pages/Employees';
import { Projects } from './pages/Projects';
import { Information } from './pages/Information';
import { About } from './pages/About';
import './App.css';

function AppLayout() {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  return (
    <Router>
      <div className="App">
        <nav className="navbar">
          <div className="nav-container">
            <Link to="/" className="nav-brand">
              Project Manager
            </Link>
            <ul className="nav-menu">
              <li>
                <Link to="/dashboard">Dashboard</Link>
              </li>
              <li>
                <Link to="/employees">Empleados</Link>
              </li>
              <li>
                <Link to="/projects">Proyectos</Link>
              </li>
              <li className="dropdown-menu">
                <button 
                  className="dropdown-btn"
                  onClick={() => setIsDropdownOpen(!isDropdownOpen)}
                >
                  Más ▼
                </button>
                {isDropdownOpen && (
                  <div className="dropdown-content">
                    <Link 
                      to="/information"
                      onClick={() => setIsDropdownOpen(false)}
                    >
                      Información
                    </Link>
                    <Link 
                      to="/about"
                      onClick={() => setIsDropdownOpen(false)}
                    >
                      Funcionamiento
                    </Link>
                  </div>
                )}
              </li>
            </ul>
          </div>
        </nav>
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/employees" element={<Employees />} />
            <Route path="/projects" element={<Projects />} />
            <Route path="/information" element={<Information />} />
            <Route path="/about" element={<About />} />
          </Routes>
        </main>

        <footer>
          <img src="/logo.png" alt="Logo" />
          <p>© 2026 Project Manager. Practica CEEP.</p>
        </footer>
      </div>
    </Router>
  );
}

export default function App() {
  return (
    <AppProvider>
      <AppLayout />
    </AppProvider>
  );
}
