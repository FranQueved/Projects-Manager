import React from 'react';
import { Link } from 'react-router-dom';
import { Button } from '../components/Button';
import '../styles/About.css';

export const About = () => {
  return (
    <div className="page-container">
      <div className="about-header">
        <h1>Funcionamiento de Project Manager</h1>
        <p className="subtitle">Descubre cómo nuestra plataforma facilita la gestión de proyectos</p>
      </div>

      <section className="about-section">
        <h2>Cómo Funciona</h2>
        <p>
          Project Manager utiliza un sistema inteligente de asignación de empleados a proyectos 
          basado en competencias y embeddings vectoriales. Esto permite realizar recomendaciones 
          automáticas y análisis comparativos entre perfiles.
        </p>
      </section>

      <section className="about-section">
        <h2>Gestión de Empleados</h2>
        <div className="workflow-steps">
          <div className="step">
            <div className="step-number">1</div>
            <h3>Registrar Empleados</h3>
            <p>Crea un perfil para cada miembro del equipo con su información personal y profesional.</p>
          </div>
          <div className="step">
            <div className="step-number">2</div>
            <h3>Definir Competencias</h3>
            <p>Asigna competencias específicas a cada empleado (lenguajes, frameworks, habilidades blandas).</p>
          </div>
          <div className="step">
            <div className="step-number">3</div>
            <h3>Generar Embeddings</h3>
            <p>El sistema crea representaciones vectoriales de cada perfil para comparaciones inteligentes.</p>
          </div>
        </div>
      </section>

      <section className="about-section">
        <h2>Gestión de Proyectos</h2>
        <div className="workflow-steps">
          <div className="step">
            <div className="step-number">1</div>
            <h3>Crear Proyecto</h3>
            <p>Define un nuevo proyecto con su descripción, duración y objetivos.</p>
          </div>
          <div className="step">
            <div className="step-number">2</div>
            <h3>Establecer Requerimientos</h3>
            <p>Especifica qué competencias son necesarias para el proyecto.</p>
          </div>
          <div className="step">
            <div className="step-number">3</div>
            <h3>Obtener Recomendaciones</h3>
            <p>El sistema sugiere los mejores empleados basándose en los requerimientos.</p>
          </div>
        </div>
      </section>

      <section className="about-section">
        <h2>Sistema de Recomendaciones Inteligentes</h2>
        <div className="features-list">
          <div className="feature">
            <h3>Análisis Vectorial</h3>
            <p>
              Utiliza embeddings (representaciones numéricas) de los perfiles para calcular 
              similitudes y encontrar los mejores candidatos.
            </p>
          </div>
          <div className="feature">
            <h3>Coincidencia de Competencias</h3>
            <p>
              Compara automáticamente las competencias requeridas con las disponibles 
              en cada empleado.
            </p>
          </div>
          <div className="feature">
            <h3>Puntuación de Compatibilidad</h3>
            <p>
              Calcula un score de compatibilidad para cada empleado con respecto a los 
              requerimientos del proyecto.
            </p>
          </div>
        </div>
      </section>

      <section className="about-section">
        <h2>Flujo de Trabajo Típico</h2>
        <div className="workflow-diagram">
          <div className="workflow-item">
            <div className="workflow-icon">👥</div>
            <h4>Empleados</h4>
            <p>Base de datos</p>
          </div>
          <div className="arrow">→</div>
          <div className="workflow-item">
            <div className="workflow-icon">📈</div>
            <h4>Embeddings</h4>
            <p>Análisis</p>
          </div>
          <div className="arrow">→</div>
          <div className="workflow-item">
            <div className="workflow-icon">📁</div>
            <h4>Proyectos</h4>
            <p>Requerimientos</p>
          </div>
          <div className="arrow">→</div>
          <div className="workflow-item">
            <div className="workflow-icon">👍</div>
            <h4>Recomendaciones</h4>
            <p>Resultados</p>
          </div>
        </div>
      </section>

      <section className="about-section">
        <h2>Características Técnicas</h2>
        <div className="tech-features">
          <div className="tech-item">
            <h3>PostgreSQL con pgvector</h3>
            <p>Base de datos con extensión de búsqueda vectorial para análisis avanzado.</p>
          </div>
          <div className="tech-item">
            <h3>Sentence Transformers</h3>
            <p>Modelos de ML para generar embeddings de alta calidad de texto.</p>
          </div>
          <div className="tech-item">
            <h3>FastAPI Backend</h3>
            <p>API rápida y escalable para todas las operaciones.</p>
          </div>
          <div className="tech-item">
            <h3>React Frontend</h3>
            <p>Interfaz moderna y responsiva para mejor experiencia de usuario.</p>
          </div>
        </div>
      </section>

      <section className="about-section about-footer">
        <h2>Comienza Ahora</h2>
        <p>
          Inicia registrando tus empleados y crea tu primer proyecto para ver cómo 
          el sistema te ayuda a tomar decisiones inteligentes de asignación.
        </p>
        <div className="cta-buttons">
          <Link to="/employees">
            <Button>Gestionar Empleados</Button>
          </Link>
          <Link to="/projects">
            <Button>Ver Proyectos</Button>
          </Link>
          <Link to="/dashboard">
            <Button>Ir al Dashboard</Button>
          </Link>
        </div>
      </section>
    </div>
  );
};
