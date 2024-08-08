import React, { useState, useEffect } from 'react';

export const Demo = () => {
  const backendUrl = process.env.REACT_APP_BACKEND_URL;
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (backendUrl) {
      fetch(`${backendUrl}/some-endpoint`)
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
          return response.json();
        })
        .then(data => setData(data))
        .catch(error => setError(error.message));
    } else {
      console.error('La URL del backend no está definida');
    }
  }, [backendUrl]);

  return (
    <div>
      <h1>Demo Page</h1>
      {error && <p>Error: {error}</p>}
      {data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : (
        <p>Cargando datos...</p>
      )}
    </div>
  );
};
