import React, { useEffect, useState, useCallback } from 'react';
import { useAppContext } from '../context/AppContext';
import { Table } from '../components/Table';
import { Button } from '../components/Button';
import { Modal } from '../components/Modal';
import { Input, TextArea, Checkbox } from '../components/Form';
import { Loading } from '../components/Loading';
import { Alert } from '../components/Alert';
import { Card } from '../components/Card';
import { assignmentService, recommendationService, requiredProfileService } from '../services/dataService';
import '../styles/Projects.css';

export const Projects = () => {
  const {
    projects,
    employees,
    loading,
    error,
    loadProjects,
    createProject,
    updateProject,
    deleteProject,
    assignEmployeeToProject,
    unassignEmployeeFromProject,
  } = useAppContext();

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingId, setEditingId] = useState(null);
  const [assignedEmployees, setAssignedEmployees] = useState([]);
  const [projectRequiredProfiles, setProjectRequiredProfiles] = useState([]);
  const [requiredProfileRecommendations, setRequiredProfileRecommendations] = useState({});
  const [selectedRequiredProfileId, setSelectedRequiredProfileId] = useState(null);
  const [showRequiredProfileForm, setShowRequiredProfileForm] = useState(false);
  const [requiredProfileFormData, setRequiredProfileFormData] = useState({
    hard_skills: '',
    soft_skills: '',
    languages: '',
  });
  const [editingRequiredProfileId, setEditingRequiredProfileId] = useState(null);
  const [alertMessage, setAlertMessage] = useState('');
  const [alertType, setAlertType] = useState('success');
  const [deletingAssignment, setDeletingAssignment] = useState(null);
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    client: 'Internal',
    start_date: '',
    end_date: '',
    finished: false,
    budget: '',
    presential: false,
  });

  useEffect(() => {
    loadProjects();
  }, [loadProjects]);

  const resetForm = () => {
    setFormData({
      name: '',
      description: '',
      client: 'Internal',
      start_date: '',
      end_date: '',
      finished: false,
      budget: '',
      presential: false,
    });
    setEditingId(null);
  };

  const loadRequiredProfileRecommendations = useCallback(async (requiredProfileId) => {
    try {
      const response = await recommendationService.getRequiredProfileRecommendations(requiredProfileId);
      setRequiredProfileRecommendations((prev) => ({
        ...prev,
        [requiredProfileId]: response.data || [],
      }));
    } catch (err) {
      console.error('Error loading recommendations:', err);
    }
  }, []);

  // Ya no necesitamos este effect porque cargamos todo en handleOpen

  const getScoreClass = (score) => {
    if (score >= 0.8) return 'excellent';
    if (score >= 0.6) return 'good';
    if (score >= 0.4) return 'acceptable';
    return 'low';
  };

  const handleOpen = async (project = null) => {
    if (project && project.id) {
      // Buscar el proyecto completo en la lista para asegurar que tiene todos los datos
      const fullProject = projects.find(p => p.id === project.id) || project;
      
      setFormData({
        name: fullProject.name || '',
        description: fullProject.description || '',
        client: fullProject.client || 'Internal',
        start_date: fullProject.start_date || '',
        end_date: fullProject.end_date || '',
        finished: fullProject.finished || false,
        budget: fullProject.budget || '',
        presential: fullProject.presential || false,
      });
      setAssignedEmployees(fullProject.employees || []);
      setEditingId(fullProject.id);

      // Abrir modal inmediatamente
      setIsModalOpen(true);

      // Cargar required profiles en background
      requiredProfileService.getProjectProfiles(fullProject.id)
        .then((response) => {
          const profiles = response.data || [];
          setProjectRequiredProfiles(profiles);
          
          // Cargar recomendaciones de TODOS los perfiles EN PARALELO (no await)
          if (profiles && profiles.length > 0) {
            Promise.all(
              profiles.map(profile =>
                recommendationService.getRequiredProfileRecommendations(profile.id)
                  .then((recResponse) => ({
                    profileId: profile.id,
                    recommendations: recResponse.data || []
                  }))
                  .catch(err => {
                    console.error(`Error loading recommendations for profile ${profile.id}:`, err);
                    return { profileId: profile.id, recommendations: [] };
                  })
              )
            ).then((results) => {
              // Actualizar todo de una vez
              const newRecommendations = {};
              results.forEach(({ profileId, recommendations }) => {
                newRecommendations[profileId] = recommendations;
              });
              setRequiredProfileRecommendations(newRecommendations);
            });
            
            // Seleccionar el primer perfil por defecto
            setSelectedRequiredProfileId(profiles[0].id);
          }
        })
        .catch((err) => {
          console.error('Error loading project profiles:', err);
        });
    } else {
      resetForm();
      setAssignedEmployees([]);
      setProjectRequiredProfiles([]);
      setShowRequiredProfileForm(false);
      setEditingRequiredProfileId(null);
      setRequiredProfileFormData({
        hard_skills: '',
        soft_skills: '',
        languages: '',
      });
      setSelectedRequiredProfileId(null);
      setIsModalOpen(true);
    }
  };

  const handleClose = () => {
    setIsModalOpen(false);
    resetForm();
  };

  const handleRemoveEmployee = async (employeeId) => {
    setDeletingAssignment(employeeId);
    try {
      await assignmentService.unassignEmployee(employeeId, editingId);
      setAssignedEmployees(assignedEmployees.filter(e => e.id !== employeeId));
      await loadProjects();
      setAlertMessage('Asignación eliminada correctamente');
      setAlertType('success');
      setTimeout(() => setAlertMessage(''), 3000);
    } catch (err) {
      setAlertMessage('Error al eliminar la asignación');
      setAlertType('error');
      console.error(err);
    } finally {
      setDeletingAssignment(null);
    }
  };

  const handleRequiredProfileChange = (e) => {
    const { name, value } = e.target;
    setRequiredProfileFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSaveRequiredProfile = async () => {
    if (!requiredProfileFormData.hard_skills && !requiredProfileFormData.soft_skills && !requiredProfileFormData.languages) {
      setAlertType('error');
      setAlertMessage('Al menos un campo debe estar relleno');
      return;
    }

    try {
      if (editingRequiredProfileId) {
        await requiredProfileService.update(editingRequiredProfileId, requiredProfileFormData);
        setAlertType('success');
        setAlertMessage('Perfil requerido actualizado correctamente');
      } else {
        await requiredProfileService.create({
          project_id: editingId,
          ...requiredProfileFormData,
        });
        setAlertType('success');
        setAlertMessage('Perfil requerido creado correctamente');
      }

      // Recargar required profiles
      const response = await requiredProfileService.getProjectProfiles(editingId);
      const profiles = response.data || [];
      setProjectRequiredProfiles(profiles);

      // Cargar recomendaciones para cada perfil
      if (profiles && profiles.length > 0) {
        for (const profile of profiles) {
          const recResponse = await recommendationService.getRequiredProfileRecommendations(profile.id);
          setRequiredProfileRecommendations((prev) => ({
            ...prev,
            [profile.id]: recResponse.data || [],
          }));
        }
        // Si no hay uno seleccionado, selecciona el primero
        if (!selectedRequiredProfileId) {
          setSelectedRequiredProfileId(profiles[0].id);
        }
      }

      setShowRequiredProfileForm(false);
      setEditingRequiredProfileId(null);
      setRequiredProfileFormData({
        hard_skills: '',
        soft_skills: '',
        languages: '',
      });
    } catch (err) {
      setAlertType('error');
      setAlertMessage('Error al guardar el perfil requerido');
      console.error(err);
    }
  };

  const handleDeleteRequiredProfile = async (id) => {
    if (window.confirm('¿Estás seguro de que quieres eliminar este perfil requerido?')) {
      try {
        await requiredProfileService.delete(id);
        setProjectRequiredProfiles(projectRequiredProfiles.filter(rp => rp.id !== id));
        setAlertType('success');
        setAlertMessage('Perfil requerido eliminado correctamente');
      } catch (err) {
        setAlertType('error');
        setAlertMessage('Error al eliminar el perfil requerido');
        console.error(err);
      }
    }
  };

  const handleEditRequiredProfile = (profile) => {
    setEditingRequiredProfileId(profile.id);
    setRequiredProfileFormData({
      hard_skills: profile.hard_skills,
      soft_skills: profile.soft_skills,
      languages: profile.languages,
    });
    setShowRequiredProfileForm(true);
  };

  const handleSelectRequiredProfile = (profileId) => {
    setSelectedRequiredProfileId(selectedRequiredProfileId === profileId ? null : profileId);
  };

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value,
    }));
  };

  const handleSubmit = async (e) => {
    e?.preventDefault();
    try {
      if (editingId) {
        console.log('Actualizando proyecto:', editingId, formData);
        await updateProject(editingId, {
          ...formData,
          budget: parseInt(formData.budget),
          end_date: formData.end_date || null,
        });
        setAlertMessage('Proyecto actualizado exitosamente');
        setAlertType('success');
      } else {
        console.log('Creando proyecto:', formData);
        await createProject({
          ...formData,
          budget: parseInt(formData.budget),
          end_date: formData.end_date || null,
        });
        setAlertMessage('Proyecto creado exitosamente');
        setAlertType('success');
      }
      
      // Recargar proyectos para actualizar la tabla
      await loadProjects();
      
      setTimeout(() => {
        handleClose();
        setTimeout(() => setAlertMessage(''), 2000);
      }, 300);
    } catch (err) {
      console.error('Error completo:', err);
      console.error('Error response:', err.response);
      
      let errorMsg = 'Error al guardar el proyecto';
      
      if (typeof err === 'string') {
        errorMsg = err;
      } else if (err?.response?.data) {
        if (typeof err.response.data === 'string') {
          errorMsg = err.response.data;
        } else if (err.response.data.detail) {
          errorMsg = typeof err.response.data.detail === 'string' 
            ? err.response.data.detail 
            : JSON.stringify(err.response.data.detail);
        } else if (err.response.data.message) {
          errorMsg = err.response.data.message;
        } else {
          errorMsg = JSON.stringify(err.response.data);
        }
      } else if (err?.message) {
        errorMsg = err.message;
      }
      
      setAlertMessage(errorMsg);
      setAlertType('error');
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('¿Está seguro que desea eliminar este proyecto?')) {
      try {
        await deleteProject(id);
        setAlertMessage('Proyecto eliminado exitosamente');
        setTimeout(() => setAlertMessage(''), 3000);
      } catch (err) {
        console.error(err);
      }
    }
  };

  if (loading && projects.length === 0) return <Loading />;

  const columns = [
    { key: 'id', label: 'ID' },
    { key: 'name', label: 'Nombre' },
    { key: 'client', label: 'Cliente' },
    { key: 'budget', label: 'Presupuesto', render: (value) => `$${value.toLocaleString('es-ES')}` },
    {
      key: 'finished',
      label: 'Estado',
      render: (value) => (value ? 'Completado' : 'Activo'),
    },
  ];

  return (
    <div className="projects-page">
      <Alert
        type={alertType}
        message={alertMessage}
        onClose={() => setAlertMessage('')}
      />

      <div className="page-header">
        <h1>Gestión de Proyectos</h1>
        <Button variant="primary" onClick={() => handleOpen()}>
          + Nuevo Proyecto
        </Button>
      </div>

      <Card>
        {loading ? (
          <Loading />
        ) : projects.length > 0 ? (
          <Table
            columns={columns}
            data={projects}
            onEdit={(project) => handleOpen(project)}
            onDelete={handleDelete}
          />
        ) : (
          <p>No hay proyectos. Crea uno para empezar.</p>
        )}
      </Card>

      <Modal
        isOpen={isModalOpen}
        onClose={handleClose}
        title={editingId ? 'Editar Proyecto' : 'Nuevo Proyecto'}
        footer={
          <div style={{ display: 'flex', gap: '8px' }}>
            <Button variant="secondary" onClick={handleClose}>
              Cancelar
            </Button>
            <Button variant="primary" onClick={handleSubmit}>
              {editingId ? 'Actualizar' : 'Crear'}
            </Button>
          </div>
        }
      >
        <div>
          <Input
            label="Nombre"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
            placeholder="Ej: Sistema de Gestión"
          />
          <TextArea
            label="Descripción"
            name="description"
            value={formData.description}
            onChange={handleChange}
            required
            placeholder="Descripción del proyecto"
          />
          <Input
            label="Cliente"
            name="client"
            value={formData.client}
            onChange={handleChange}
            placeholder="Ej: Acme Corp"
          />
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '16px' }}>
            <Input
              label="Fecha de Inicio"
              name="start_date"
              type="date"
              value={formData.start_date}
              onChange={handleChange}
              required
            />
            <Input
              label="Fecha de Fin"
              name="end_date"
              type="date"
              value={formData.end_date}
              onChange={handleChange}
            />
          </div>
          <Input
            label="Presupuesto"
            name="budget"
            type="number"
            value={formData.budget}
            onChange={handleChange}
            required
            placeholder="Ej: 50000"
          />

          {editingId && (
            <div className="required-profiles-section">
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                <h4>Perfiles Requeridos para el Proyecto</h4>
                <Button 
                  variant="secondary" 
                  onClick={() => {
                    setShowRequiredProfileForm(true);
                    setEditingRequiredProfileId(null);
                    setRequiredProfileFormData({
                      hard_skills: '',
                      soft_skills: '',
                      languages: '',
                    });
                  }}
                >
                  + Agregar Perfil
                </Button>
              </div>

              {showRequiredProfileForm && (
                <div className="required-profile-form">
                  <h5>{editingRequiredProfileId ? 'Editar' : 'Nuevo'} Perfil Requerido</h5>
                  <Input
                    label="Hard Skills"
                    name="hard_skills"
                    value={requiredProfileFormData.hard_skills}
                    onChange={handleRequiredProfileChange}
                    placeholder="Ej: Python, JavaScript, SQL"
                  />
                  <Input
                    label="Soft Skills"
                    name="soft_skills"
                    value={requiredProfileFormData.soft_skills}
                    onChange={handleRequiredProfileChange}
                    placeholder="Ej: Liderazgo, Comunicación, Trabajo en equipo"
                  />
                  <Input
                    label="Idiomas"
                    name="languages"
                    value={requiredProfileFormData.languages}
                    onChange={handleRequiredProfileChange}
                    placeholder="Ej: Inglés fluido, Español nativo"
                  />
                  <div style={{ display: 'flex', gap: '8px', marginTop: '12px' }}>
                    <Button variant="primary" onClick={handleSaveRequiredProfile}>
                      Guardar
                    </Button>
                    <Button 
                      variant="secondary" 
                      onClick={() => {
                        setShowRequiredProfileForm(false);
                        setEditingRequiredProfileId(null);
                        setRequiredProfileFormData({
                          hard_skills: '',
                          soft_skills: '',
                          languages: '',
                        });
                      }}
                    >
                      Cancelar
                    </Button>
                  </div>
                </div>
              )}

              {projectRequiredProfiles && projectRequiredProfiles.length > 0 && (
                <div className="required-profiles-list">
                  {projectRequiredProfiles.map((profile) => (
                    <div 
                      key={profile.id} 
                      className={`required-profile-item-expanded ${selectedRequiredProfileId === profile.id ? 'selected' : ''}`}
                      onClick={() => handleSelectRequiredProfile(profile.id)}
                      style={{ cursor: 'pointer' }}
                    >
                      <div className="required-profile-header">
                        <div className="required-profile-info">
                          <h5>Perfil Requerido {selectedRequiredProfileId === profile.id ? '(Seleccionado)' : ''}</h5>
                          <div className="required-profile-skills">
                            {profile.hard_skills && <p><strong>Hard Skills:</strong> {profile.hard_skills}</p>}
                            {profile.soft_skills && <p><strong>Soft Skills:</strong> {profile.soft_skills}</p>}
                            {profile.languages && <p><strong>Idiomas:</strong> {profile.languages}</p>}
                          </div>
                        </div>
                        <div style={{ display: 'flex', gap: '8px' }}>
                          <Button
                            variant="secondary"
                            onClick={(e) => {
                              e.stopPropagation();
                              handleEditRequiredProfile(profile);
                            }}
                            style={{ fontSize: '12px', padding: '4px 8px' }}
                          >
                            Editar
                          </Button>
                          <Button
                            variant="secondary"
                            onClick={(e) => {
                              e.stopPropagation();
                              handleDeleteRequiredProfile(profile.id);
                            }}
                            style={{ fontSize: '12px', padding: '4px 8px', backgroundColor: '#dc3545' }}
                          >
                            Eliminar
                          </Button>
                        </div>
                      </div>

                      {selectedRequiredProfileId === profile.id && requiredProfileRecommendations[profile.id] && requiredProfileRecommendations[profile.id].length > 0 && (
                        <div className="profile-similar-employees">
                          <h6>Empleados más similares:</h6>
                          <div className="similar-employees-list">
                            {requiredProfileRecommendations[profile.id].slice(0, 5).map((emp) => {
                              const isAssigned = assignedEmployees.some(e => e.id === emp.id);
                              return (
                                <div key={emp.id} className={`similar-employee-card score-${getScoreClass(emp.similarity_score)}`}>
                                  <div className="employee-header">
                                    <div>
                                      <p className="employee-name">{emp.name}</p>
                                      <p className="employee-office">{emp.office || 'N/A'}</p>
                                    </div>
                                    <span className="score-badge-small">{Math.round(emp.similarity_score * 100)}%</span>
                                  </div>
                                  <div className="employee-skills">
                                    {emp.hard_skills && <p><small><strong>Hard:</strong> {emp.hard_skills}</small></p>}
                                    {emp.soft_skills && <p><small><strong>Soft:</strong> {emp.soft_skills}</small></p>}
                                  </div>
                                  <div style={{ marginTop: '8px' }}>
                                    {isAssigned ? (
                                      <span style={{ fontSize: '12px', color: '#28a745', fontWeight: 'bold' }}>✓ Asignado</span>
                                    ) : (
                                      <button
                                        type="button"
                                        onClick={() => assignEmployeeToProject(emp.id, editingId)}
                                        disabled={deletingAssignment === emp.id}
                                        style={{
                                          width: '100%',
                                          padding: '6px 12px',
                                          backgroundColor: '#28a745',
                                          color: '#fff',
                                          border: 'none',
                                          borderRadius: '4px',
                                          cursor: deletingAssignment === emp.id ? 'not-allowed' : 'pointer',
                                          fontSize: '12px',
                                          opacity: deletingAssignment === emp.id ? 0.6 : 1
                                        }}
                                      >
                                        Asignar
                                      </button>
                                    )}
                                  </div>
                                </div>
                              );
                            })}
                          </div>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              )}

              {(!projectRequiredProfiles || projectRequiredProfiles.length === 0) && !showRequiredProfileForm && (
                <p style={{ color: '#666', fontStyle: 'italic' }}>No hay perfiles requeridos. Agréguelos para obtener recomendaciones.</p>
              )}
            </div>
          )}

          {editingId && assignedEmployees && assignedEmployees.length > 0 && (
            <div style={{ marginTop: '20px', padding: '12px', backgroundColor: '#f0f8ff', borderRadius: '6px', border: '1px solid #17a2b8' }}>
              <h4 style={{ marginTop: 0 }}>Empleados Asignados al Proyecto</h4>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px' }}>
                {assignedEmployees.map((emp) => (
                  <div 
                    key={emp.id} 
                    style={{ 
                      display: 'flex',
                      alignItems: 'center',
                      gap: '8px',
                      backgroundColor: 'white', 
                      padding: '8px 12px', 
                      borderRadius: '4px', 
                      border: '1px solid #17a2b8', 
                      fontSize: '14px' 
                    }}
                  >
                    <div>
                      <strong>{emp.name}</strong> {emp.office && <span style={{ color: '#666' }}>({emp.office})</span>}
                    </div>
                    <button
                      type="button"
                      onClick={() => handleRemoveEmployee(emp.id)}
                      disabled={deletingAssignment === emp.id}
                      style={{
                        marginLeft: 'auto',
                        border: 'none',
                        backgroundColor: '#dc3545',
                        color: '#fff',
                        borderRadius: '3px',
                        padding: '4px 8px',
                        cursor: deletingAssignment === emp.id ? 'not-allowed' : 'pointer',
                        fontSize: '14px',
                        opacity: deletingAssignment === emp.id ? 0.6 : 1
                      }}
                    >
                      ×
                    </button>
                  </div>
                ))}
              </div>
            </div>
          )}

          <Checkbox
            label="Presencial"
            name="presential"
            checked={formData.presential}
            onChange={handleChange}
          />
          <Checkbox
            label="Completado"
            name="finished"
            checked={formData.finished}
            onChange={handleChange}
          />
        </div>
      </Modal>
    </div>
  );
};
