// src/components/PasswordResetRequest.jsx

import React, { useState } from 'react';
import { Email } from '@mui/icons-material';
import AxiosInstance from './AxiosInstance';
import '../styles/PasswordResetRequest.css';

function PasswordResetRequest() {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await AxiosInstance.post('/api/password-reset-email/', { email });
      setMessage('✅ Password reset link sent to your email.');
    } catch (error) {
      console.error('Reset request failed:', error);
      setMessage('❌ Failed to send reset link. Please try again.');
    }
  };

  return (
    <div className="Reset_pass-app">
      <h1 className="Reset_pass-heading">Reset Your Password</h1>

      <div className="Reset_pass-container">
        <p className="Reset_pass-description">
          Enter your registered email address. You'll receive a link to reset your password.
        </p>

        <form className="Reset_pass-form" onSubmit={handleSubmit}>
          <div className="Reset_pass-input-group">
            <Email />
            <input
              type="email"
              placeholder="Email"
              required
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>

          <button type="submit" className="Login-btn primary">
            Send Reset Link
          </button>
        </form>

        {message && <p className="Reset_pass-message">{message}</p>}
      </div>
    </div>
  );
}

export default PasswordResetRequest;
