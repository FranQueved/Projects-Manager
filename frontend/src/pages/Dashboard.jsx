import React, { useEffect } from 'react';
import { useAppContext } from '../context/AppContext';
import { Card } from '../components/Card';
import { Loading } from '../components/Loading';
import '../styles/Dashboard.css';

export const Dashboard = () => {
  const { employees, projects, loading, loadEmployees, loadProjects } = useAppContext();

  useEffect(() => {
    loadEmployees();
    loadProjects();
  }, [loadEmployees, loadProjects]);

  if (loading) return <Loading />;

  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <h1>Dashboard</h1>
        <p>Bienvenido al gestor de proyectos y empleados</p>
      </div>

      <div className="dashboard-stats">
        <Card className="stat-card">
          <div className="stat-content">
            <h3>{employees.length}</h3>
            <p>Empleados</p>
          </div>
        </Card>
        <Card className="stat-card">
          <div className="stat-content">
            <h3>{projects.length}</h3>
            <p>Proyectos</p>
          </div>
        </Card>
        <Card className="stat-card">
          <div className="stat-content">
            <h3>
              {projects.filter(p => p.finished).length}/{projects.length}
            </h3>
            <p>Proyectos Completados</p>
          </div>
        </Card>
        <Card className="stat-card">
          <div className="stat-content">
            <h3>
              {projects.length > 0 
                ? projects.reduce((acc, p) => acc + p.budget, 0).toLocaleString('es-ES')
                : 0
              }
            </h3>
            <p>Presupuesto Total</p>
          </div>
        </Card>
      </div>

      <div className="dashboard-content">
        <Card>
          <h2>Empleados Recientes</h2>
          {employees.length > 0 ? (
            <table className="quick-table">
              <thead>
                <tr>
                  <th>Nombre</th>
                  <th>Oficina</th>
                </tr>
              </thead>
              <tbody>
                {employees.slice(0, 5).map((emp) => (
                  <tr key={emp.id}>
                    <td>{emp.name}</td>
                    <td>{emp.office || '-'}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : (
            <p>No hay empleados</p>
          )}
        </Card>

        <Card>
          <h2>Proyectos Activos</h2>
          {projects.filter(p => !p.finished).length > 0 ? (
            <table className="quick-table">
              <thead>
                <tr>
                  <th>Nombre</th>
                  <th>Cliente</th>
                  <th>Presupuesto</th>
                </tr>
              </thead>
              <tbody>
                {projects.filter(p => !p.finished).slice(0, 5).map((proj) => (
                  <tr key={proj.id}>
                    <td>{proj.name}</td>
                    <td>{proj.client}</td>
                    <td>${proj.budget.toLocaleString('es-ES')}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : (
            <p>No hay proyectos activos</p>
          )}
        </Card>
      </div>
    </div>
  );
};
