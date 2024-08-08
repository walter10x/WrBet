// wrbet/src/api/axiosConfig.js
import axios from 'axios';

// Configura Axios para usar la URL base del archivo .env
const api = axios.create({
  baseURL: process.env.REACT_APP_BACKEND_URL
});

export default api;
