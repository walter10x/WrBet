import React from 'react';

export const BackendURL = () => {
    return (
        <div style={{ padding: '20px', backgroundColor: 'red', color: 'white', textAlign: 'center' }}>
            <h1>Error: La URL del backend no está definida</h1>
            <p>Por favor, asegúrate de que la variable <code>REACT_APP_BACKEND_URL</code> esté correctamente configurada en el archivo <code>.env</code>.</p>
        </div>
    );
};


