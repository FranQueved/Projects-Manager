import React from 'react';
import { Link } from 'react-router-dom';
import { Button } from '../components/Button';
import { Card } from '../components/Card';
import '../styles/Information.css';


export const Information = () => {
  return (
    <div className="page-container">
      <div className="info-header">
        <h1>Información del Project Manager</h1>
        <p className="subtitle">Todo lo que necesitas saber sobre nuestra plataforma</p>
      </div>

      <section className="info-section">
        <h2>¿Qué es Project Manager?</h2>
        <p>
          Project Manager es una plataforma integral diseñada para facilitar la gestión de proyectos 
          y la asignación de empleados. Nuestro objetivo es proporcionar herramientas eficientes 
          para que los equipos trabajen de manera colaborativa y productiva.
        </p>
      </section>

      <section className="info-section">
        <h2>Características Principales</h2>
        <div className="features-grid">
          <Card>
            <h3>Dashboard</h3>
            <p>Visualiza un resumen completo de tus proyectos y el desempeño del equipo en tiempo real.</p>
          </Card>
          <Card>
            <h3>Gestión de Empleados</h3>
            <p>Administra tu equipo, consulta perfiles y competencias de cada miembro.</p>
          </Card>
          <Card>
            <h3>Proyectos</h3>
            <p>Crea, edita y supervisa todos tus proyectos desde un solo lugar.</p>
          </Card>
          <Card>
            <h3>Asignaciones</h3>
            <p>Asigna empleados a proyectos de manera inteligente según sus competencias.</p>
          </Card>
        </div>
      </section>

      <section className="info-section">
        <h2>Módulos Disponibles</h2>
        <div className="modules-list">
          <div className="module-item">
            <h3>Dashboard</h3>
            <p>Tu centro de control con métricas y gráficos importantes.</p>
            <Link to="/dashboard">
              <Button>Ir al Dashboard</Button>
            </Link>
          </div>
          <div className="module-item">
            <h3>Empleados</h3>
            <p>Gestiona la base de datos de tu equipo de trabajo.</p>
            <Link to="/employees">
              <Button>Ver Empleados</Button>
            </Link>
          </div>
          <div className="module-item">
            <h3>Proyectos</h3>
            <p>Administra tus proyectos y sus detalles.</p>
            <Link to="/projects">
              <Button>Ver Proyectos</Button>
            </Link>
          </div>
        </div>
      </section>


      <section className="info-section info-footer">
        <h2>¿Necesitas ayuda?</h2>
        <p>
          Si tienes preguntas sobre cómo usar la plataforma, consulta la sección 
          de "Funcionamiento" o contacta con nuestro equipo de soporte.
        </p>
        <Link to="/about">
          <Button>Ver Funcionamiento</Button>
        </Link>
      </section>
    </div>
  );
};
    