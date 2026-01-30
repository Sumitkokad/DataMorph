// src/components/Login.jsx
import { useState, useEffect, useRef } from "react"
import { useNavigate, Link } from "react-router-dom"
import AxiosInstance from "./AxiosInstance"
import '../styles/Login.css';
import { ArrowForward, PersonAdd, Email, Lock } from "@mui/icons-material"

function Login() {
  // Existing login state
  const [showLoginFields, setShowLoginFields] = useState(false)
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const navigate = useNavigate()

  // Dashboard state
  const [scrolled, setScrolled] = useState(false)
  const [animateMetrics, setAnimateMetrics] = useState(false)

  // Refs for scroll targets
  const heroRef = useRef(null)
  const exploreRef = useRef(null)
  const recruitmentRef = useRef(null)
  const whyChooseRef = useRef(null)
  const loginRef = useRef(null)

  // Existing login handlers
  const handleLoginClick = () => {
    setShowLoginFields(true)
  }

  const handleSubmit = async (e) => {
  e.preventDefault()
  try {
    const response = await AxiosInstance.post("/api/login/", {       email: email,
      password: password,
    })
    const token = response.data.token
    localStorage.setItem("token", token)

    // Redirect to preprocessing dashboard instead of home
    navigate("/upload")  // ← CHANGED FROM "/home" TO "/preprocessing"
  } catch (error) {
    console.error("Login failed:", error)
    alert("Login failed. Please check your credentials and try again.")
  }
}

  // Dashboard scroll effects
  useEffect(() => {
    const handleScroll = () => {
      setScrolled(window.scrollY > 10)

      // Check if recruitment section is in view for animation
      if (recruitmentRef.current) {
        const rect = recruitmentRef.current.getBoundingClientRect()
        if (rect.top < window.innerHeight - 100) {
          setAnimateMetrics(true)
        }
      }
    }

    window.addEventListener("scroll", handleScroll)
    return () => window.removeEventListener("scroll", handleScroll)
  }, [])

  // Smooth scroll function
  const scrollToSection = (elementRef) => {
    if (elementRef && elementRef.current) {
      window.scrollTo({
        top: elementRef.current.offsetTop - 120,
        behavior: "smooth",
      })
    }
  }

  return (
    <div className="Login-app">
      {/* Dashboard Content */}
      <div className="Dashboard-app-container">
        <header className={`Dashboard-main-header ${scrolled ? "Dashboard-header-scrolled" : ""}`}>
          <div className="Dashboard-header-container">
            <div className="Dashboard-logo-container">
              <div className="Dashboard-logo-icon">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                >
                  <path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z" />
                </svg>
              </div>
              <h1 className="Dashboard-logo-text">BisMit Co</h1>
            </div>
            <nav className="Dashboard-main-nav">
              <ul className="Dashboard-nav-list">
                <li>
                  <a
                    href="#"
                    className="Dashboard-nav-link-ai"
                    onClick={(e) => {
                      e.preventDefault()
                      scrollToSection(exploreRef)
                    }}
                  >
                    Explore
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="Dashboard-nav-link-ai"
                    onClick={(e) => {
                      e.preventDefault()
                      scrollToSection(recruitmentRef)
                    }}
                  >
                    For Companies
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="Dashboard-nav-link-ai"
                    onClick={(e) => {
                      e.preventDefault()
                      scrollToSection(whyChooseRef)
                    }}
                  >
                    Why Us
                  </a>
                </li>
                <li>
                  <a
                    href="#"
                    className="Dashboard-nav-link-ai Dashboard-nav-link-signin"
                    onClick={(e) => {
                      e.preventDefault()
                      scrollToSection(loginRef)
                    }}
                  >
                    Login
                  </a>
                </li>
              </ul>
            </nav>
          </div>
        </header>

        <main className="Dashboard-main-content">
          <section className="Dashboard-hero-section" ref={heroRef}>
            <div className="Dashboard-hero-container">
              <h2 className="Dashboard-dashboard-heading">
                Revolutionize Your Data Preprocessing
                <span className="Dashboard-gradient-text">With DataMorph</span>
              </h2>
              <p className="Dashboard-dashboard-subtext">
                AI-powered data preprocessing that cleans, validates, and prepares datasets intelligently.
              </p>
              <div className="Dashboard-hero-buttons">
                <button
                  className="Dashboard-hero-btn-primary Dashboard-btn-animated"
                  onClick={() => scrollToSection(loginRef)}
                >
                  Get Started
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <path d="M5 12h14M12 5l7 7-7 7" />
                  </svg>
                </button>
              </div>
            </div>
          </section>

          <section className="Dashboard-explore-section" ref={exploreRef}>
            <div className="Dashboard-explore-container">
              <h2 className="Dashboard-explore-heading">Explore Our Platform</h2>
              <p className="Dashboard-explore-subtext">
                Prepare datasets the way an expert data scientist would without writing repetitive code.
              </p>

              <div className="Dashboard-features-grid">
                <div className="Dashboard-feature-card">
                  <div className="Dashboard-feature-icon">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    >
                      <circle cx="12" cy="12" r="10"></circle>
                      <path d="M12 8v8"></path>
                      <path d="M8 12h8"></path>
                    </svg>
                  </div>
                  <h3 className="Dashboard-feature-title">Smart Column Understanding</h3>
                  <p className="Dashboard-feature-description">
Our AI automatically analyzes each column to identify intent numeric, categorical, datetime, identifier, or target and applies preprocessing only where it makes sense.                  </p>
                </div>

                <div className="Dashboard-feature-card">
                  <div className="Dashboard-feature-icon">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    >
                      <polyline points="16 18 22 12 16 6"></polyline>
                      <polyline points="8 6 2 12 8 18"></polyline>
                    </svg>
                  </div>
                  <h3 className="Dashboard-feature-title">Use Automation</h3>
                  <p className="Dashboard-feature-description">
From missing values to encoding and scaling, preprocessing is fully automated but always conservative, explainable, and non-destructive.                  </p>
                </div>

                <div className="Dashboard-feature-card">
                  <div className="Dashboard-feature-icon">
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                    >
                      <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                      <circle cx="9" cy="7" r="4"></circle>
                      <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                      <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                    </svg>
                  </div>
                  <h3 className="Dashboard-feature-title">Safe Data Handling</h3>
                  <p className="Dashboard-feature-description">
                    Find top talent faster with AI-driven filters built to handle data at scale..
                  </p>
                </div>
              </div>
            </div>
          </section>

          <section className="Dashboard-recruitment-section" ref={recruitmentRef}>
            <div className="Dashboard-recruitment-container">
              <h2 className="Dashboard-recruitment-heading">Core Product Message</h2>
              <p className="Dashboard-recruitment-subtext">
                Build Clean, Reliable, Model-Ready Data Faster.
              </p>

              <div className="Dashboard-recruitment-content">
                <div className="Dashboard-recruitment-features">
                  <div className="Dashboard-recruitment-feature">
                    <div className="Dashboard-recruitment-icon">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                      >
                        <circle cx="12" cy="12" r="10"></circle>
                        <circle cx="12" cy="12" r="6"></circle>
                        <circle cx="12" cy="12" r="2"></circle>
                      </svg>
                    </div>
                    <div className="Dashboard-recruitment-feature-content">
                      <h3 className="Dashboard-recruitment-feature-title">AI-Guided Preprocessing Intelligence</h3>
                      <p className="Dashboard-recruitment-feature-description">
Use AI to detect data quality issues, outliers, skewness, and leakage risks then recommend preprocessing steps that are safe, justified, and reversible.                      </p>
                    </div>
                  </div>

                  <div className="Dashboard-recruitment-feature">
                    <div className="Dashboard-recruitment-icon">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                      >
                        <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                        <circle cx="9" cy="7" r="4"></circle>
                        <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                        <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                      </svg>
                    </div>
                    <div className="Dashboard-recruitment-feature-content">
                      <h3 className="Dashboard-recruitment-feature-title">Centralized Data Preparation Engine</h3>
                      <p className="Dashboard-recruitment-feature-description">
                        Track all preprocessing decisions in one place with full transparency including column-wise operations, dataset-wide checks, and AI reasoning.


                      </p>
                    </div>
                  </div>

                  <div className="Dashboard-recruitment-feature">
                    <div className="Dashboard-recruitment-icon">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                      >
                        <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline>
                      </svg>
                    </div>
                    <div className="Dashboard-recruitment-feature-content">
                      <h3 className="Dashboard-recruitment-feature-title">Reduce Time Spent on Data Cleaning</h3>
                      <p className="Dashboard-recruitment-feature-description">
Spend less time fixing datasets and more time building models. Our system cuts preprocessing time from hours to minutes.                      </p>
                    </div>
                  </div>
                </div>

                <div className="Dashboard-analytics-card">
                  <div className="Dashboard-analytics-header">
                    <h4>Dashboard</h4>
                    <div className="Dashboard-analytics-filters">
                      <div className="Dashboard-analytics-filter">
                        <span>Search type: Web</span>
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 24 24"
                          fill="none"
                          stroke="currentColor"
                          strokeWidth="2"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          width="16"
                          height="16"
                        >
                          <path d="M12 20h9"></path>
                          <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
                        </svg>
                      </div>
                      <div className="Dashboard-analytics-filter">
                        <span>Date: Last 3 months</span>
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          viewBox="0 0 24 24"
                          fill="none"
                          stroke="currentColor"
                          strokeWidth="2"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          width="16"
                          height="16"
                        >
                          <path d="M12 20h9"></path>
                          <path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path>
                        </svg>
                      </div>
                    </div>
                  </div>

                  <div className="Dashboard-analytics-metrics">
                    <div className="Dashboard-metric" style={{ backgroundColor: "#1E88E5" }}>
                      <div className="Dashboard-metric-label">Automated accuracy: 99%</div>
                      <div className={`Dashboard-metric-value ${animateMetrics ? "animate" : ""}`} data-value="55">
                        55
                      </div>
                    </div>
                    <div className="Dashboard-metric" style={{ backgroundColor: "#7B1FA2" }}>
                      <div className="Dashboard-metric-label">Datasets processed: 55</div>
                      <div className={`Dashboard-metric-value ${animateMetrics ? "animate" : ""}`} data-value="6.71">
                        6.71
                      </div>
                      <div className="Dashboard-metric-unit">K</div>
                    </div>
                    <div className="Dashboard-metric" style={{ backgroundColor: "#388E3C" }}>
                      <div className="Dashboard-metric-label">Columns analyzed: 6.7K</div>
                      <div className={`Dashboard-metric-value ${animateMetrics ? "animate" : ""}`} data-value="0.8">
                        0.8
                      </div>
                      <div className="Dashboard-metric-unit">%</div>
                    </div>
                    <div className="Dashboard-metric" style={{ backgroundColor: "#E65100" }}>
                      <div className="Dashboard-metric-label">Average position</div>
                      <div className={`Dashboard-metric-value ${animateMetrics ? "animate" : ""}`} data-value="51.8">
                        51.8
                      </div>
                    </div>
                  </div>

                  <div className="Dashboard-analytics-chart">
                    <div className="Dashboard-chart-line blue"></div>
                    <div className="Dashboard-chart-line purple"></div>
                    <div className="Dashboard-chart-line green"></div>
                    <div className="Dashboard-chart-line orange"></div>
                  </div>
                </div>
              </div>
            </div>
          </section>

          <section className="Dashboard-why-choose-section" ref={whyChooseRef}>
            <div className="Dashboard-why-choose-container">
              <h2 className="Dashboard-why-choose-heading">Why Choose Us?</h2>

              <div className="Dashboard-why-choose-content">
                <div className="Dashboard-ai-visual">
                  <div className="Dashboard-network-container">
                    <div className="Dashboard-network-animation">
                      <div className="Dashboard-ai-robot">
                        <div className="Dashboard-ai-head">
                          <div className="Dashboard-ai-face"></div>
                        </div>
                        <div className="Dashboard-ai-body">
                          <div className="Dashboard-ai-text">Open AI</div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <div className="Dashboard-benefits-list">
                  <div className="Dashboard-benefit-item">
                    <div className="Dashboard-benefit-icon">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                      >
                        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                        <polyline points="22 4 12 14.01 9 11.01"></polyline>
                      </svg>
                    </div>
                    <div className="Dashboard-benefit-content">
                      <h3 className="Dashboard-benefit-title">Open AI-Powered Architecture</h3>
                      <p className="Dashboard-benefit-description">
                       Built on modern AI models and rule-based validation layers to ensure accuracy, safety, and reproducibility.
                      </p>
                    </div>
                  </div>

                  <div className="Dashboard-benefit-item">
                    <div className="Dashboard-benefit-icon">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                      >
                        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                        <polyline points="22 4 12 14.01 9 11.01"></polyline>
                      </svg>
                    </div>
                    <div className="Dashboard-benefit-content">
                      <h3 className="Dashboard-benefit-title">Expert-Level Data Decisions</h3>
                      <p className="Dashboard-benefit-description">
                        Our system behaves like a senior data scientist choosing median vs mean correctly, avoiding ID encoding, and preventing data corruption.
                      </p>
                    </div>
                  </div>

                  <div className="Dashboard-benefit-item">
                    <div className="Dashboard-benefit-icon">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                      >
                        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                        <polyline points="22 4 12 14.01 9 11.01"></polyline>
                      </svg>
                    </div>
                    <div className="Dashboard-benefit-content">
                      <h3 className="Dashboard-benefit-title">Automation Without Complexity</h3>
                      <p className="Dashboard-benefit-description">
                        Automate sourcing, shortlisting, and reporting with AI workflows,
                        all visualized in a preprocessing that simplifies your hiring process.
                      </p>
                    </div>
                  </div>

                  <div className="Dashboard-benefit-item">
                    <div className="Dashboard-benefit-icon">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                      >
                        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                        <polyline points="22 4 12 14.01 9 11.01"></polyline>
                      </svg>
                    </div>
                    <div className="Dashboard-benefit-content">
                      <h3 className="Dashboard-benefit-title">Scalable by Design</h3>
                      <p className="Dashboard-benefit-description">
                        From small CSVs to enterprise-scale datasets, preprocess efficiently with memory-optimized and chunk-based execution.
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </section>
        </main>

        {/* Login Section - Redesigned to Match Dashboard Theme */}
        <section className="Dashboard-login-section" ref={loginRef}>
          <div className="Dashboard-login-container">
            <div className="Dashboard-login-content">
              <div className="Dashboard-login-visual">
                <div className="Dashboard-login-animation">
                  <div className="Dashboard-login-circle"></div>
                  <div className="Dashboard-login-circle"></div>
                  <div className="Dashboard-login-circle"></div>
                </div>
                <div className="Dashboard-login-icon">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  >
                    <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4"></path>
                    <polyline points="10 17 15 12 10 7"></polyline>
                    <line x1="15" y1="12" x2="3" y2="12"></line>
                  </svg>
                </div>
              </div>

              <div className="Dashboard-login-form-container">
                <h2 className="Dashboard-login-heading">Ready to Get Started?</h2>
                <p className="Dashboard-login-subtext">
Join data scientists and ML engineers who are transforming raw data into high-quality, production-ready datasets using AI.                </p>

                <div className="Dashboard-login-card">
                  {!showLoginFields ? (
                    <div className="Dashboard-login-welcome">
                      <button className="Dashboard-login-btn-primary" onClick={handleLoginClick}>
                        <ArrowForward style={{ marginRight: "8px" }} />
                        Login to Your Account
                      </button>
                      <div className="Dashboard-login-divider">
                        <span>or</span>
                      </div>
                      <Link to="/register">
                        <button className="Dashboard-login-btn-secondary">
                          <PersonAdd style={{ marginRight: "8px" }} />
                          Create New Account
                        </button>
                      </Link>
                    </div>
                  ) : (
                    <form className="Dashboard-login-form" onSubmit={handleSubmit}>
                      <div className="Dashboard-login-input-group">
                        <div className="Dashboard-login-input-icon">
                          <Email />
                        </div>
                        <input
                          type="email"
                          placeholder="Enter your email"
                          required
                          value={email}
                          onChange={(e) => setEmail(e.target.value)}
                          className="Dashboard-login-input"
                        />
                      </div>
                      <div className="Dashboard-login-input-group">
                        <div className="Dashboard-login-input-icon">
                          <Lock />
                        </div>
                        <input
                          type="password"
                          placeholder="Enter your password"
                          required
                          value={password}
                          onChange={(e) => setPassword(e.target.value)}
                          className="Dashboard-login-input"
                        />
                      </div>
                      <button type="submit" className="Dashboard-login-btn-submit">
                        <ArrowForward style={{ marginRight: "8px" }} />
                        Sign In
                      </button>
                      <div className="Dashboard-login-options">
                        <Link to="/register" className="Dashboard-login-link">
                          Don't have an account? Sign up
                        </Link>
                        <Link to="/password-reset" className="Dashboard-login-link">
                          Forgot password?
                        </Link>
                      </div>
                    </form>
                  )}
                </div>
              </div>
            </div>
          </div>
        </section>

        <footer className="Dashboard-main-footer">
          <div className="Dashboard-footer-container">
            <div className="Dashboard-footer-logo">
              <h3>DataMorph</h3>
              <p>© 2025 DataMorph. All rights reserved.</p>
            </div>
            <div className="Dashboard-footer-links">
              <ul>
                <li>
                  <a href="#" className="Dashboard-footer-link">
                    About
                  </a>
                </li>
                <li>
                  <a href="#" className="Dashboard-footer-link">
                    Careers
                  </a>
                </li>
                <li>
                  <a href="#" className="Dashboard-footer-link">
                    Terms
                  </a>
                </li>
                <li>
                  <a href="#" className="Dashboard-footer-link">
                    Privacy
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </footer>
      </div>
    </div>
  )
}

export default Login
