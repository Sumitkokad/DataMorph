// import React from "react";
// import Upload from "./component/Upload";  // ✅ path must match folder & file name exactly

// function App() {
//   return (
//     <div className="App">
//       <Upload />
//     </div>
//   );
// }

// export default App;

import { Routes, Route, Navigate, useLocation } from 'react-router-dom'
import Login from './component/Login'  // Changed from './components/Login'
import Register from './component/Register'  // Changed from './components/Register'
import Upload from './component/Upload'
import PasswordResetRequest from './component/PasswordResetRequest'  // Changed
import ConfirmPassword from './component/ComformPassword'
import ProtectedRoute from './component/ProtectedRoutes'  // Changed from './components/ProtectedRoute'
import './App.css'

function App() {
  const location = useLocation()
  
  // Check if current page should show navbar
  const showNavbar = location.pathname === "/upload"

  return (
    <div className="app-container">
      {/* Simple navbar for upload page only */}
      {showNavbar && (
        <nav className="simple-nav">
          <div className="nav-content">
            <h2>File Upload Dashboard</h2>
            <button 
              onClick={() => {
                localStorage.removeItem('token')
                localStorage.removeItem('user')
                window.location.href = '/login'
              }}
              className="logout-btn"
            >
              Logout
            </button>
          </div>
        </nav>
      )}

      <Routes>
        {/* Redirect root to login */}
        <Route path="/" element={<Navigate to="/login" replace />} />
        
        {/* Public routes */}
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/password-reset" element={<PasswordResetRequest />} />
        <Route path="/reset-password/:uid/:token" element={<ConfirmPassword />} />
        
        {/* Protected route - Only accessible after login */}
        <Route 
          path="/upload" 
          element={
            <ProtectedRoute>
              <Upload />
            </ProtectedRoute>
          } 
        />
        
        {/* Catch all - redirect to login */}
        <Route path="*" element={<Navigate to="/login" replace />} />
      </Routes>
    </div>
  )
}

export default App