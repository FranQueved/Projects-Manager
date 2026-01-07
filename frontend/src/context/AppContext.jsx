import React, { createContext, useContext, useState, useCallback } from 'react';
import { employeeService, projectService, assignmentService, recommendationService, requiredProfileService } from '../services/dataService';

const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [employees, setEmployees] = useState([]);
  const [projects, setProjects] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [requiredProfiles, setRequiredProfiles] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Cargar todos los empleados
  const loadEmployees = useCallback(async () => {
    try {
      setLoading(true);
      const response = await employeeService.getAll();
      setEmployees(response.data);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  // Cargar todos los proyectos
  const loadProjects = useCallback(async () => {
    try {
      setLoading(true);
      const response = await projectService.getAll();
      setProjects(response.data);
      setError(null);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, []);

  // Crear empleado
  const createEmployee = useCallback(async (data) => {
    try {
      setLoading(true);
      const response = await employeeService.create(data);
      setEmployees([...employees, response.data]);
      setError(null);
      return response.data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [employees]);

  // Actualizar empleado
  const updateEmployee = useCallback(async (id, data) => {
    try {
      setLoading(true);
      const response = await employeeService.update(id, data);
      setEmployees(employees.map(emp => emp.id === id ? response.data : emp));
      setError(null);
      return response.data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [employees]);

  // Eliminar empleado
  const deleteEmployee = useCallback(async (id) => {
    try {
      setLoading(true);
      await employeeService.delete(id);
      setEmployees(employees.filter(emp => emp.id !== id));
      setError(null);
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [employees]);

  // Crear proyecto
  const createProject = useCallback(async (data) => {
    try {
      setLoading(true);
      const response = await projectService.create(data);
      setProjects([...projects, response.data]);
      setError(null);
      return response.data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [projects]);

  // Actualizar proyecto
  const updateProject = useCallback(async (id, data) => {
    try {
      setLoading(true);
      const response = await projectService.update(id, data);
      setProjects(projects.map(proj => proj.id === id ? response.data : proj));
      setError(null);
      return response.data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [projects]);

  // Eliminar proyecto
  const deleteProject = useCallback(async (id) => {
    try {
      setLoading(true);
      await projectService.delete(id);
      setProjects(projects.filter(proj => proj.id !== id));
      setError(null);
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [projects]);

  // Asignar empleado a proyecto
  const assignEmployeeToProject = useCallback(async (employeeId, projectId) => {
    try {
      setLoading(true);
      await assignmentService.assignEmployee(employeeId, projectId);
      await loadProjects();
      setError(null);
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [loadProjects]);

  // Desasignar empleado de proyecto
  const unassignEmployeeFromProject = useCallback(async (employeeId, projectId) => {
    try {
      setLoading(true);
      await assignmentService.unassignEmployee(employeeId, projectId);
      await loadProjects();
      setError(null);
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [loadProjects]);

  // Obtener recomendaciones de empleados para un proyecto
  const getRecommendations = useCallback(async (projectId) => {
    try {
      setLoading(true);
      const response = await recommendationService.getEmployeeRecommendations(projectId);
      setRecommendations(response.data);
      setError(null);
      return response.data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  // Cargar required profiles de un proyecto
  const loadRequiredProfiles = useCallback(async (projectId) => {
    try {
      setLoading(true);
      const response = await requiredProfileService.getProjectProfiles(projectId);
      setRequiredProfiles(response.data);
      setError(null);
      return response.data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  // Crear required profile
  const createRequiredProfile = useCallback(async (data) => {
    try {
      setLoading(true);
      const response = await requiredProfileService.create(data);
      setRequiredProfiles([...requiredProfiles, response.data]);
      setError(null);
      return response.data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [requiredProfiles]);

  // Actualizar required profile
  const updateRequiredProfile = useCallback(async (id, data) => {
    try {
      setLoading(true);
      const response = await requiredProfileService.update(id, data);
      setRequiredProfiles(requiredProfiles.map(rp => rp.id === id ? response.data : rp));
      setError(null);
      return response.data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [requiredProfiles]);

  // Eliminar required profile
  const deleteRequiredProfile = useCallback(async (id) => {
    try {
      setLoading(true);
      await requiredProfileService.delete(id);
      setRequiredProfiles(requiredProfiles.filter(rp => rp.id !== id));
      setError(null);
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [requiredProfiles]);

  const value = {
    // Estado
    employees,
    projects,
    recommendations,
    requiredProfiles,
    loading,
    error,
    // Acciones de empleados
    loadEmployees,
    createEmployee,
    updateEmployee,
    deleteEmployee,
    // Acciones de proyectos
    loadProjects,
    createProject,
    updateProject,
    deleteProject,
    // Acciones de asignaciones
    assignEmployeeToProject,
    unassignEmployeeFromProject,
    // Acciones de recomendaciones
    getRecommendations,
    // Acciones de required profiles
    loadRequiredProfiles,
    createRequiredProfile,
    updateRequiredProfile,
    deleteRequiredProfile,
  };

  return <AppContext.Provider value={value}>{children}</AppContext.Provider>;
};

export const useAppContext = () => {
  const context = useContext(AppContext);
  if (!context) {
    throw new Error('useAppContext debe usarse dentro de AppProvider');
  }
  return context;
};
