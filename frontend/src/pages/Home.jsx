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
    </div>
  );
};
