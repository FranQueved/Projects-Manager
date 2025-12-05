/**
 * MÓDULO INDEX.JSX - PUNTO DE ENTRADA DE LA APLICACIÓN
 * =====================================================
 * 
 * Este es el archivo más importante para iniciar la app React. Sus funciones son:
 * 
 * 1. RENDERIZACIÓN INICIAL: Toma el elemento DOM con id="root" del HTML y lo llena con la app React.
 *    - Este elemento se encuentra en public/index.html
 * 
 * 2. COMPONENTE RAÍZ: Renderiza <App /> que es el componente principal.
 *    - Todo lo que ves en la aplicación desciende de este componente.
 * 
 * 3. STRICT MODE: Envuelve la app en <React.StrictMode> para detectar problemas de desarrollo.
 *    - Ayuda a identificar bugs y malas prácticas durante el desarrollo.
 *    - Se desactiva automáticamente en producción.
 * 
 * El flujo es: index.jsx → App.jsx → componentes de páginas → componentes pequeños
 */

import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
