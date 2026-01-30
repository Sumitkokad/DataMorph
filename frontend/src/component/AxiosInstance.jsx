// // src/component/AxiosInstance.js
// import axios from 'axios';

// const AxiosInstance = axios.create({
//   baseURL: 'http://localhost:8000/',  // Your Django backend URL
//   headers: {
//     'Content-Type': 'application/json',
//   },
// });

// // Add token to requests if exists
// AxiosInstance.interceptors.request.use(
//   (config) => {
//     const token = localStorage.getItem('token');
//     if (token) {
//       config.headers.Authorization = `Token ${token}`;
//     }
//     return config;
//   },
//   (error) => {
//     return Promise.reject(error);
//   }
// );

// // Handle response errors
// AxiosInstance.interceptors.response.use(
//   (response) => response,
//   (error) => {
//     if (error.response?.status === 401) {
//       // Token expired or invalid
//       localStorage.removeItem('token');
//       localStorage.removeItem('user');
//       window.location.href = '/login';
//     }
//     return Promise.reject(error);
//   }
// );

// export default AxiosInstance;


// src/component/AxiosInstance.js
import axios from 'axios';

const AxiosInstance = axios.create({
  baseURL: 'http://localhost:8000/',  // Your Django backend URL
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000, // Add timeout
});

// Add logging to request interceptor
AxiosInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Token ${token}`;
    }
    
    // Log request for debugging
    console.log(`🚀 Axios Request: ${config.method.toUpperCase()} ${config.baseURL}${config.url}`);
    console.log('Request data:', config.data);
    console.log('Request headers:', config.headers);
    
    return config;
  },
  (error) => {
    console.error('❌ Axios Request Error:', error);
    return Promise.reject(error);
  }
);

// Add logging to response interceptor
AxiosInstance.interceptors.response.use(
  (response) => {
    console.log(`✅ Axios Response: ${response.status} ${response.config.url}`);
    console.log('Response data:', response.data);
    return response;
  },
  (error) => {
    console.error('❌ Axios Response Error:', {
      url: error.config?.url,
      method: error.config?.method,
      status: error.response?.status,
      statusText: error.response?.statusText,
      data: error.response?.data,
      message: error.message,
      request: error.request
    });
    
    if (error.response?.status === 401) {
      // Token expired or invalid
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    
    return Promise.reject(error);
  }
);

export default AxiosInstance;