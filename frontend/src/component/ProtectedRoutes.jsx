// // components/ProtectedRoute.jsx
// import { Navigate } from 'react-router-dom'
// import { useEffect, useState } from 'react'

// const ProtectedRoute = ({ children }) => {
//   const [isAuthenticated, setIsAuthenticated] = useState(false)
//   const [loading, setLoading] = useState(true)

//   useEffect(() => {
//     // Check authentication
//     const token = localStorage.getItem('token')
//     // Optional: Verify token with backend
//     setIsAuthenticated(!!token)
//     setLoading(false)
//   }, [])

//   if (loading) {
//     return (
//       <div className="loading-container">
//         <div className="spinner"></div>
//         <p>Checking authentication...</p>
//       </div>
//     )
//   }

//   return isAuthenticated ? children : <Navigate to="/login" replace />
// }

// export default ProtectedRoute


// src/component/ProtectedRoutes.jsx
import { Navigate } from "react-router-dom";

function ProtectedRoutes({ children }) {
  // Check if user is authenticated
  const isAuthenticated = () => {
    // Check for token in localStorage
    const token = localStorage.getItem("token") || 
                  localStorage.getItem("knoxToken") || 
                  localStorage.getItem("authToken");
    
    // If token exists, user is authenticated
    return !!token;
  };

  // If not authenticated, redirect to login
  if (!isAuthenticated()) {
    return <Navigate to="/login" replace />;
  }

  // If authenticated, render the children (protected content)
  return children;
}

export default ProtectedRoutes;