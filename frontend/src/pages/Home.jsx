import React from 'react';
import { Link } from 'react-router-dom';
import { Button } from '../components/Button';
import { Card } from '../components/Card';
import '../styles/Home.css';

export const Home = () => {
  return (
    <div className="home">
      <div className="hero">
        <div className="hero-content">
          <h1>Project Manager</h1>
          <p>Sistema integral de gestión de proyectos y empleados con búsqueda semántica</p>
          <div className="hero-buttons">
            <Link to="/dashboard">
              <Button variant="primary">Ir al Dashboard</Button>
            </Link>
            <Link to="/employees">
              <Button variant="secondary">Ver Empleados</Button>
            </Link>
          </div>
        </div>
      </div>

      <div className="features">
        <div className="container">
          <h2>Características Principales</h2>
          <div className="features-grid">
            <Card>
              <div className="feature-icon">👥</div>
              <h3>Gestión de Empleados</h3>
              <p>Crea y administra perfiles de empleados con sus habilidades técnicas y blandas.</p>
            </Card>
            <Card>
              <div className="feature-icon">📋</div>
              <h3>Gestión de Proyectos</h3>
              <p>Organiza tus proyectos con detalles de cliente, presupuesto y fechas.</p>
            </Card>
            <Card>
              <div className="feature-icon">🔗</div>
              <h3>Asignaciones</h3>
              <p>Asigna empleados a proyectos de forma eficiente y automática.</p>
            </Card>
            <Card>
              <div className="feature-icon">🔍</div>
              <h3>Búsqueda Semántica</h3>
              <p>Utiliza embeddings vectoriales para encontrar el mejor match de habilidades.</p>
            </Card>
          </div>
        </div>
      </div>
    </div>
  );
};
