import React from 'react';
import '../styles/Alert.css';

export const Alert = ({ type = 'error', message, onClose }) => {
  if (!message) return null;

  return (
    <div className={`alert alert-${type}`}>
      <span>{message}</span>
      {onClose && <button onClick={onClose} className="alert-close">×</button>}
    </div>
  );
};
