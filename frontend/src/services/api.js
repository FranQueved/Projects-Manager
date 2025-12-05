/**
 * MÓDULO SERVICES/API.JS - CLIENTE HTTP CENTRALIZADO
 * ===================================================
 * 
 * Este módulo crea una instancia centralizada de Axios para hacer peticiones HTTP.
 * Todas las llamadas a la API deben pasar por aquí.
 * 
 * ¿POR QUÉ CENTRALIZARLO?
 * 1. CONSISTENCIA: Todas las peticiones usan la misma configuración base
 * 2. INTERCEPTORES: Puedes agregar lógica común a TODAS las peticiones (ej: tokens)
 * 3. MANTENIBILIDAD: Si cambias la URL del API, solo cambias un lugar
 * 
 * FUNCIONALIDADES:
 * - Base URL: Configurable mediante variable de entorno o fallback a localhost
 * - Headers: Content-Type automático para JSON
 * - Interceptor de Request: Agrega token de autenticación si existe
 * 
 * USO:
 * import api from '../services/api';
 * api.get('/users') → GET a http://localhost:8000/api/users
 * api.post('/login', datos) → POST con datos automáticamente
 */

import axios from 'axios';

// URL base del API - se configura desde variables de entorno o usa localhost por defecto
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api';

// Crear instancia de Axios con configuración base
const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

/**
 * INTERCEPTOR DE REQUEST
 * =======================
 * Se ejecuta ANTES de cada petición HTTP.
 * Aquí agregamos el token JWT al header Authorization si existe en localStorage.
 */
api.interceptors.request.use(
  (config) => {
    // Obtener token del almacenamiento local
    const token = localStorage.getItem('token');
    // Si existe token, agregarlo al header de autenticación
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  // Si hay error en la configuración, rechazarlo
  (error) => Promise.reject(error)
);

export default api;
