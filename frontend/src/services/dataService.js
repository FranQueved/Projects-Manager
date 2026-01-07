import api from './api';

// Servicios para Empleados
export const employeeService = {
  getAll: () => api.get('/employees'),
  getById: (id) => api.get(`/employees/${id}`),
  create: (data) => api.post('/employees', data),
  update: (id, data) => api.put(`/employees/${id}`, data),
  delete: (id) => api.delete(`/employees/${id}`),
};

// Servicios para Proyectos
export const projectService = {
  getAll: () => api.get('/projects'),
  getById: (id) => api.get(`/projects/${id}`),
  create: (data) => api.post('/projects', data),
  update: (id, data) => api.put(`/projects/${id}`, data),
  delete: (id) => api.delete(`/projects/${id}`),
};

// Servicios para Asignaciones
export const assignmentService = {
  assignEmployee: (employeeId, projectId) =>
    api.post(`/assignments/assign/${employeeId}/${projectId}`),
  unassignEmployee: (employeeId, projectId) =>
    api.delete(`/assignments/unassign/${employeeId}/${projectId}`),
  getProjectEmployees: (projectId) =>
    api.get(`/assignments/project/${projectId}`),
  getEmployeeProjects: (employeeId) =>
    api.get(`/assignments/employee/${employeeId}`),
};
// Servicios para Recomendaciones
export const recommendationService = {
  getEmployeeRecommendations: (projectId) =>
    api.get(`/recommendations/employees/${projectId}`),
  getRequiredProfileRecommendations: (requiredProfileId) =>
    api.get(`/recommendations/required-profile/${requiredProfileId}`),
};

// Servicios para Required Profiles
export const requiredProfileService = {
  getProjectProfiles: (projectId) =>
    api.get(`/required-profiles/project/${projectId}`),
  getById: (id) =>
    api.get(`/required-profiles/${id}`),
  create: (data) =>
    api.post('/required-profiles', data),
  update: (id, data) =>
    api.put(`/required-profiles/${id}`, data),
  delete: (id) =>
    api.delete(`/required-profiles/${id}`),
};