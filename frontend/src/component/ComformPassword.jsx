// src/components/ConfirmPassword.jsx

import React, { useState } from 'react';
import { Lock } from '@mui/icons-material';
import { useParams, useNavigate } from 'react-router-dom';
import AxiosInstance from './AxiosInstance';
import '../styles/ConformPassword.css';



function ConfirmPassword() {
  const { uid, token } = useParams(); // expect /reset/:uid/:token
  const navigate = useNavigate();
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (newPassword !== confirmPassword) {
      setMessage('❌ Passwords do not match.');
      return;
    }

    try {
      await AxiosInstance.post('api/reset/password_confirm/', {
        uid,
        token,
        new_password: newPassword,
      });
      setMessage('✅ Password reset successfully.');
      setTimeout(() => navigate('/', { replace: true }), 2500); // redirect to login
    } catch (error) {
      console.error('Password reset failed:', error);
      setMessage('❌ Reset failed. Token might be invalid or expired.');
    }
  };

  return (
    <div className="Conform-app">
      <h1 className="Conform-heading">Set Your New Password</h1>

      <div className="Conform-container">
        <form className="Conform-form" onSubmit={handleSubmit}>
          <div className="Conform-input-group">
            <Lock />
            <input
              type="password"
              placeholder="New Password"
              required
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
            />
          </div>
          <div className="Conform-input-group">
            <Lock />
            <input
              type="password"
              placeholder="Confirm Password"
              required
              value={confirmPassword}
              onChange={(e) => setConfirmPassword(e.target.value)}
            />
          </div>
          <button type="submit" className="Login-btn primary">
            Reset Password
          </button>
        </form>

        {message && <p className="Conform-message">{message}</p>}
      </div>
    </div>
  );
}

export default ConfirmPassword;
