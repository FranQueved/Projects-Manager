import React from 'react';
import '../styles/Form.css';

export const Input = ({ 
  label, 
  name, 
  type = 'text', 
  value, 
  onChange, 
  required = false,
  placeholder = ''
}) => {
  return (
    <div className="form-group">
      {label && <label htmlFor={name}>{label}</label>}
      <input
        id={name}
        name={name}
        type={type}
        value={value}
        onChange={onChange}
        required={required}
        placeholder={placeholder}
        className="form-control"
      />
    </div>
  );
};

export const TextArea = ({ 
  label, 
  name, 
  value, 
  onChange, 
  required = false,
  placeholder = ''
}) => {
  return (
    <div className="form-group">
      {label && <label htmlFor={name}>{label}</label>}
      <textarea
        id={name}
        name={name}
        value={value}
        onChange={onChange}
        required={required}
        placeholder={placeholder}
        className="form-control"
        rows="4"
      />
    </div>
  );
};

export const Select = ({ 
  label, 
  name, 
  value, 
  onChange, 
  options = [],
  required = false
}) => {
  return (
    <div className="form-group">
      {label && <label htmlFor={name}>{label}</label>}
      <select
        id={name}
        name={name}
        value={value}
        onChange={onChange}
        required={required}
        className="form-control"
      >
        <option value="">Seleccionar...</option>
        {options.map((opt) => (
          <option key={opt.value} value={opt.value}>
            {opt.label}
          </option>
        ))}
      </select>
    </div>
  );
};

export const Checkbox = ({ 
  label, 
  name, 
  checked, 
  onChange 
}) => {
  return (
    <div className="form-group checkbox">
      <input
        id={name}
        name={name}
        type="checkbox"
        checked={checked}
        onChange={onChange}
        className="form-checkbox"
      />
      {label && <label htmlFor={name}>{label}</label>}
    </div>
  );
};
