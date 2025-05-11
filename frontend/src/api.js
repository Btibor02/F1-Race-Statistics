import axios from 'axios';

const API = axios.create({
  baseURL: 'http://localhost:5000', // Flask backend URL
  withCredentials: true // important if using Flask-Login cookies
});

export default API;
