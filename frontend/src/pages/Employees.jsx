import React, { useEffect, useState } from 'react';
import { useAppContext } from '../context/AppContext';
import { Table } from '../components/Table';
import { Button } from '../components/Button';
import { Modal } from '../components/Modal';
import { Input, TextArea } from '../components/Form';
import { Loading } from '../components/Loading';
import { Alert } from '../components/Alert';
import { Card } from '../components/Card';
import { assignmentService } from '../services/dataService';
import '../styles/Employees.css';

export const Employees = () => {
  const {
    employees,
    projects,
    loading,
    error,
    loadEmployees,
    loadProjects,
    createEmployee,
    updateEmployee,
    deleteEmployee,
  } = useAppContext();

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [editingId, setEditingId] = useState(null);
  const [assignedProjects, setAssignedProjects] = useState([]);
  const [formData, setFormData] = useState({
    name: '',
    office: '',
    hard_skills: '',
    soft_skills: '',
    languages: '',
  });
  const [alertMessage, setAlertMessage] = useState('');
  const [deletingAssignment, setDeletingAssignment] = useState(null);

  useEffect(() => {
    loadEmployees();
  }, [loadEmployees]);

  const resetForm = () => {
    setFormData({
      name: '',
      office: '',
      hard_skills: '',
      soft_skills: '',
      languages: '',
    });
    setEditingId(null);
  };

  const handleOpen = (employee = null) => {
    if (employee) {
      setFormData({
        name: employee.name,
        office: employee.office || '',
        hard_skills: employee.hard_skills || '',
        soft_skills: employee.soft_skills || '',
        languages: employee.languages || '',
      });
      setEditingId(employee.id);
      
      // Cargar proyectos asignados al empleado
      const empProjects = projects.filter(proj => 
        proj.employees && proj.employees.some(emp => emp.id === employee.id)
      );
      setAssignedProjects(empProjects);
    } else {
      resetForm();
      setAssignedProjects([]);
    }
    setIsModalOpen(true);
  };

  const handleClose = () => {
    setIsModalOpen(false);
    resetForm();
  };

  const handleRemoveProject = async (projectId) => {
    setDeletingAssignment(projectId);
    try {
      await assignmentService.unassignEmployee(editingId, projectId);
      setAssignedProjects(assignedProjects.filter(p => p.id !== projectId));
      await loadEmployees();
      setAlertMessage('Asignación eliminada correctamente');
      setTimeout(() => setAlertMessage(''), 3000);
    } catch (err) {
      setAlertMessage('Error al eliminar la asignación');
      console.error(err);
    } finally {
      setDeletingAssignment(null);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (editingId) {
        await updateEmployee(editingId, {
          name: formData.name,
          office: formData.office,
          hard_skills: formData.hard_skills,
          soft_skills: formData.soft_skills,
          languages: formData.languages,
        });
        setAlertMessage('Empleado actualizado exitosamente');
      } else {
        await createEmployee(formData);
        setAlertMessage('Empleado creado exitosamente');
      }
      await Promise.all([loadEmployees(), loadProjects()]);
      handleClose();
      setTimeout(() => setAlertMessage(''), 3000);
    } catch (err) {
      console.error(err);
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm('¿Está seguro que desea eliminar este empleado?')) {
      try {
        await deleteEmployee(id);
        await Promise.all([loadEmployees(), loadProjects()]);
        setAlertMessage('Empleado eliminado exitosamente');
        setTimeout(() => setAlertMessage(''), 3000);
      } catch (err) {
        console.error(err);
      }
    }
  };

  if (loading && employees.length === 0) return <Loading />;

  const columns = [
    { key: 'id', label: 'ID' },
    { key: 'name', label: 'Nombre' },
    { key: 'office', label: 'Oficina' },
    { key: 'hard_skills', label: 'Hard Skills', render: (value) => value || '-' },
    { key: 'soft_skills', label: 'Soft Skills', render: (value) => value || '-' },
    { key: 'languages', label: 'Idiomas', render: (value) => value || '-' },
    {
      key: 'profile_id',
      label: 'Perfil ID',
      render: (value) => value || '-',
    },
  ];

  return (
    <div className="employees-page">
      <Alert
        type="success"
        message={alertMessage}
        onClose={() => setAlertMessage('')}
      />
      <Alert type="error" message={error} />

      <div className="page-header">
        <h1>Gestión de Empleados</h1>
        <Button variant="primary" onClick={() => handleOpen()}>
          + Nuevo Empleado
        </Button>
      </div>

      <Card>
        {loading ? (
          <Loading />
        ) : employees.length > 0 ? (
          <Table
            columns={columns}
            data={employees}
            onEdit={() => handleOpen(employees.find(e => e.id))}
            onDelete={handleDelete}
          />
        ) : (
          <p>No hay empleados. Crea uno para empezar.</p>
        )}
      </Card>

      <Modal
        isOpen={isModalOpen}
        onClose={handleClose}
        title={editingId ? 'Editar Empleado' : 'Nuevo Empleado'}
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
        <form onSubmit={handleSubmit}>
          <Input
            label="Nombre"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
            placeholder="Ej: Juan Pérez"
          />
          <Input
            label="Oficina"
            name="office"
            value={formData.office}
            onChange={handleChange}
            placeholder="Ej: Madrid"
          />
          <TextArea
            label="Habilidades Técnicas"
            name="hard_skills"
            value={formData.hard_skills}
            onChange={handleChange}
            placeholder="Ej: Python, JavaScript, React"
          />
          <TextArea
            label="Habilidades Blandas"
            name="soft_skills"
            value={formData.soft_skills}
            onChange={handleChange}
            placeholder="Ej: Comunicación, Liderazgo"
          />
          <Input
            label="Idiomas"
            name="languages"
            value={formData.languages}
            onChange={handleChange}
            placeholder="Ej: Español, Inglés"
          />
          {editingId && assignedProjects.length > 0 && (
            <div style={{
              marginTop: '20px',
              padding: '12px',
              backgroundColor: '#f0f8ff',
              border: '1px solid #17a2b8',
              borderRadius: '4px'
            }}>
              <h4 style={{ marginTop: 0, marginBottom: '12px', color: '#17a2b8' }}>
                Proyectos Asignados
              </h4>
              <div style={{
                display: 'flex',
                flexWrap: 'wrap',
                gap: '8px'
              }}>
                {assignedProjects.map(project => (
                  <div
                    key={project.id}
                    style={{
                      display: 'flex',
                      alignItems: 'center',
                      gap: '8px',
                      padding: '8px 12px',
                      backgroundColor: '#fff',
                      border: '1px solid #17a2b8',
                      borderRadius: '4px',
                      fontSize: '14px'
                    }}
                  >
                    <div>
                      <strong>{project.name}</strong>
                      {project.client && <div style={{ fontSize: '12px', color: '#666' }}>{project.client}</div>}
                    </div>
                    <button
                      type="button"
                      onClick={() => handleRemoveProject(project.id)}
                      disabled={deletingAssignment === project.id}
                      style={{
                        marginLeft: 'auto',
                        border: 'none',
                        backgroundColor: '#dc3545',
                        color: '#fff',
                        borderRadius: '3px',
                        padding: '4px 8px',
                        cursor: deletingAssignment === project.id ? 'not-allowed' : 'pointer',
                        fontSize: '14px',
                        opacity: deletingAssignment === project.id ? 0.6 : 1
                      }}
                    >
                      ×
                    </button>
                  </div>
                ))}
              </div>
            </div>
          )}        </form>
      </Modal>
    </div>
  );
};
