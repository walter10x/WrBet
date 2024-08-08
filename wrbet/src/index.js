import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import injectContext from './store/appContext'; // Ajusta la ruta si es necesario

const AppWithContext = injectContext(App);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <AppWithContext />
  </React.StrictMode>
);
