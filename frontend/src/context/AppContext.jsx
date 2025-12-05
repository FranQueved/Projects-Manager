/**
 * MÓDULO CONTEXT/APPCONTEXT.JSX - CONTEXTO GLOBAL DE LA APLICACIÓN
 * ==================================================================
 * 
 * Este módulo implementa React Context para compartir estado GLOBALMENTE sin prop drilling.
 * 
 * ¿QUÉ ES EL CONTEXTO?
 * Es un mecanismo de React que permite compartir datos entre componentes sin pasar props.
 * Imagina que tienes un componente muy anidado (App → Layout → Sidebar → MenuItem).
 * Con contexto no necesitas pasar props a través de todos esos niveles.
 * 
 * ESTRUCTURA DE ESTE ARCHIVO:
 * 1. createContext(): Crea el objeto contexto
 * 2. AppProvider: Componente que envuelve la app y proporciona el estado global
 * 3. useAppContext: Hook personalizado para acceder al contexto desde cualquier componente
 * 
 * ESTADO GLOBAL DISPONIBLE:
 * - user: Información del usuario autenticado
 * - loading: Indicador si algo se está cargando
 * - error: Mensaje de error si ocurre algo
 * 
 * CÓMO USARLO:
 * 1. En App.jsx envuelve todo con: <AppProvider><App/></AppProvider>
 * 2. En cualquier componente usa: const { user, loading } = useAppContext();
 */

import React, { createContext, useContext, useState } from 'react';

// Crear el contexto vacío
const AppContext = createContext();

/**
 * COMPONENT: AppProvider
 * ======================
 * Este componente envuelve la aplicación y proporciona el estado global.
 * Todos los componentes dentro pueden acceder a los valores del contexto.
 */
export function AppProvider({ children }) {
  // Estado global de la aplicación
  const [user, setUser] = useState(null);           // Usuario autenticado
  const [loading, setLoading] = useState(false);    // Indicador de carga
  const [error, setError] = useState(null);         // Mensaje de error

  // Objeto con todos los valores que queremos compartir globalmente
  const value = {
    user,
    setUser,
    loading,
    setLoading,
    error,
    setError,
  };

  return (
    <AppContext.Provider value={value}>
      {children}
    </AppContext.Provider>
  );
}

/**
 * HOOK: useAppContext
 * ====================
 * Hook personalizado para acceder al contexto desde cualquier componente.
 * Automáticamente verifica que se use dentro de AppProvider.
 * 
 * USO:
 * const { user, loading, error } = useAppContext();
 */
export function useAppContext() {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useAppContext debe ser usado dentro de AppProvider');
  }
  return context;
}
