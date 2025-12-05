/**
 * MÓDULO HOOKS/USEFETCH.JS - HOOK PERSONALIZADO PARA PETICIONES HTTP
 * ===================================================================
 * 
 * Este es un Custom Hook (gancho personalizado) que encapsula la lógica de
 * hacer peticiones HTTP y manejar los estados comunes.
 * 
 * ¿POR QUÉ UN HOOK PERSONALIZADO?
 * Evita repetir código. En lugar de escribir el mismo patrón de fetch en cada componente:
 * - Llamar al API
 * - Manejar loading
 * - Manejar errores
 * - Guardar datos
 * Lo haces UNA VEZ en el hook y lo reutilizas en todos los componentes.
 * 
 * FLUJO DE EJECUCIÓN:
 * 1. Se llama el hook en un componente: const { data, loading, error } = useFetch('/users')
 * 2. useEffect se ejecuta una sola vez cuando el componente monta
 * 3. Hace una petición GET a '/users'
 * 4. Actualiza los estados: loading → false, data o error
 * 5. El componente se re-renderiza con los nuevos datos
 * 
 * RETORNA:
 * - data: Los datos del API (null si aún está cargando o hay error)
 * - loading: true mientras está cargando, false cuando termina
 * - error: Mensaje de error si ocurre algo (null si todo OK)
 */

import { useState, useEffect } from 'react';
import api from '../services/api';

/**
 * HOOK: useFetch
 * ===============
 * @param {string} url - La URL o endpoint a solicitar (ej: '/users', '/products/1')
 * @returns {object} { data, loading, error }
 * 
 * EJEMPLO:
 * function MiComponente() {
 *   const { data: usuarios, loading, error } = useFetch('/api/usuarios');
 *   
 *   if (loading) return <p>Cargando...</p>;
 *   if (error) return <p>Error: {error}</p>;
 *   return <ul>{usuarios.map(u => <li key={u.id}>{u.nombre}</li>)}</ul>;
 * }
 */
export function useFetch(url) {
  const [data, setData] = useState(null);           // Datos traídos del API
  const [loading, setLoading] = useState(true);     // ¿Está cargando?
  const [error, setError] = useState(null);         // ¿Hubo error?

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        // Hacer petición GET al URL especificado
        const response = await api.get(url);
        // Guardar los datos
        setData(response.data);
        // Limpiar error
        setError(null);
      } catch (err) {
        // Si hay error, guardarlo y limpiar datos
        setError(err.message);
        setData(null);
      } finally {
        // Siempre terminar de cargar (éxito o error)
        setLoading(false);
      }
    };

    // Ejecutar fetch solo si el URL cambió
    fetchData();
  }, [url]); // Dependencia: solo re-ejecutar si URL cambia

  // Retornar los estados para que el componente los use
  return { data, loading, error };
}
