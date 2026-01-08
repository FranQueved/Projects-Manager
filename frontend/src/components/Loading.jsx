import React from 'react';
import '../styles/Loading.css';

export const Loading = () => {
  return (
    <div className="loading">
      <div className="spinner"></div>
      <p>Cargando...</p>
    </div>
  );
};
