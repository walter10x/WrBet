import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_BACKEND_URL // Asegúrate de que esta URL esté bien definida
});

export default api;
