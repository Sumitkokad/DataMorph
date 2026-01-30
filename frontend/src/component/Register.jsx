// src/components/Register.jsx

import React, { useState } from 'react';
import '../styles/Register.css';
import { Email, Lock, LockOpen, ArrowForward } from '@mui/icons-material';
import { Link, useNavigate } from 'react-router-dom';
import AxiosInstance from "./AxiosInstance";
import axios from 'axios';

function Register() {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    confirmPassword: '',
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    const { email, password, confirmPassword } = formData;

    if (password !== confirmPassword) {
      alert('Passwords do not match.');
      return;
    }

    try {
      const response = await AxiosInstance.post('/api/register/', { email, password, password2: confirmPassword });
      alert('Registered successfully!');
      console.log(response.data);

      // Redirect to Login page after successful registration
      navigate('/');

    } catch (error) {
      console.error('Registration error:', error.response?.data || error.message);
      const errorMessage = error.response && error.response.data ? JSON.stringify(error.response.data) : error.message;
      alert('Registration failed: ' + errorMessage);
    }
  };

  return (
    <div className="Register-app">
      <h1 className="Register-heading">Create Your Account</h1>
      <div className="Register-container">
        <p className="Register-description">
          Sign up to experience AI-powered hiring. It's quick and free.
        </p>
        <form className="Register-form" onSubmit={handleRegister}>
          <div className="Register-input-group">
            <Email />
            <input
              type="email"
              name="email"
              placeholder="Email"
              required
              value={formData.email}
              onChange={handleChange}
            />
          </div>
          <div className="Register-input-group">
            <Lock />
            <input
              type="password"
              name="password"
              placeholder="Password"
              required
              value={formData.password}
              onChange={handleChange}
            />
          </div>
          <div className="Register-input-group">
            <LockOpen />
            <input
              type="password"
              name="confirmPassword"
              placeholder="Confirm Password"
              required
              value={formData.confirmPassword}
              onChange={handleChange}
            />
          </div>
          
          <button type="submit" className="Register-btn primary">
            <ArrowForward style={{ marginRight: '8px' }} />
            Register
          </button>
        </form>
        <Link to="/">
          <button className="Register-btn outline">
            Already have an account? Login
          </button>
        </Link>
        <p className="Register-help">
          Need help? <Link to="/support">Contact Support.</Link>
        </p>
      </div>
    </div>
  );
}

export default Register;