"use client";

import React, { useState, useRef, useCallback, useEffect } from 'react';
import axios from 'axios';
import '../styles/Upload.css';

// SVG Icons as components
const Icons = {
  Upload: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
      <polyline points="17 8 12 3 7 8" />
      <line x1="12" y1="3" x2="12" y2="15" />
    </svg>
  ),
  File: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
      <polyline points="14 2 14 8 20 8" />
      <line x1="16" y1="13" x2="8" y2="13" />
      <line x1="16" y1="17" x2="8" y2="17" />
      <polyline points="10 9 9 9 8 9" />
    </svg>
  ),
  X: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <line x1="18" y1="6" x2="6" y2="18" />
      <line x1="6" y1="6" x2="18" y2="18" />
    </svg>
  ),
  ArrowRight: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <line x1="5" y1="12" x2="19" y2="12" />
      <polyline points="12 5 19 12 12 19" />
    </svg>
  ),
  Brain: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M9.5 2A2.5 2.5 0 0 1 12 4.5v15a2.5 2.5 0 0 1-4.96.44 2.5 2.5 0 0 1-2.96-3.08 3 3 0 0 1-.34-5.58 2.5 2.5 0 0 1 1.32-4.24 2.5 2.5 0 0 1 1.98-3A2.5 2.5 0 0 1 9.5 2Z" />
      <path d="M14.5 2A2.5 2.5 0 0 0 12 4.5v15a2.5 2.5 0 0 0 4.96.44 2.5 2.5 0 0 0 2.96-3.08 3 3 0 0 0 .34-5.58 2.5 2.5 0 0 0-1.32-4.24 2.5 2.5 0 0 0-1.98-3A2.5 2.5 0 0 0 14.5 2Z" />
    </svg>
  ),
  Search: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <circle cx="11" cy="11" r="8" />
      <line x1="21" y1="21" x2="16.65" y2="16.65" />
    </svg>
  ),
  Zap: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2" />
    </svg>
  ),
  Shield: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
    </svg>
  ),
  Check: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <polyline points="20 6 9 17 4 12" />
    </svg>
  ),
  CheckCircle: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" />
      <polyline points="22 4 12 14.01 9 11.01" />
    </svg>
  ),
  Download: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
      <polyline points="7 10 12 15 17 10" />
      <line x1="12" y1="15" x2="12" y2="3" />
    </svg>
  ),
  Database: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <ellipse cx="12" cy="5" rx="9" ry="3" />
      <path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3" />
      <path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5" />
    </svg>
  ),
  Sparkles: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="m12 3-1.912 5.813a2 2 0 0 1-1.275 1.275L3 12l5.813 1.912a2 2 0 0 1 1.275 1.275L12 21l1.912-5.813a2 2 0 0 1 1.275-1.275L21 12l-5.813-1.912a2 2 0 0 1-1.275-1.275L12 3Z" />
      <path d="M5 3v4" />
      <path d="M19 17v4" />
      <path d="M3 5h4" />
      <path d="M17 19h4" />
    </svg>
  ),
  Columns: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <rect x="3" y="3" width="18" height="18" rx="2" ry="2" />
      <line x1="12" y1="3" x2="12" y2="21" />
    </svg>
  ),
  Rows: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <rect x="3" y="3" width="18" height="18" rx="2" />
      <line x1="3" y1="9" x2="21" y2="9" />
      <line x1="3" y1="15" x2="21" y2="15" />
    </svg>
  ),
  HardDrive: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <line x1="22" y1="12" x2="2" y2="12" />
      <path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z" />
      <line x1="6" y1="16" x2="6.01" y2="16" />
      <line x1="10" y1="16" x2="10.01" y2="16" />
    </svg>
  ),
  AlertCircle: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <circle cx="12" cy="12" r="10" />
      <line x1="12" y1="8" x2="12" y2="12" />
      <line x1="12" y1="16" x2="12.01" y2="16" />
    </svg>
  ),
  Target: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <circle cx="12" cy="12" r="10" />
      <circle cx="12" cy="12" r="6" />
      <circle cx="12" cy="12" r="2" />
    </svg>
  ),
  Filter: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3" />
    </svg>
  ),
  Hash: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <line x1="4" y1="9" x2="20" y2="9" />
      <line x1="4" y1="15" x2="20" y2="15" />
      <line x1="10" y1="3" x2="8" y2="21" />
      <line x1="16" y1="3" x2="14" y2="21" />
    </svg>
  ),
  Type: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <polyline points="4 7 4 4 20 4 20 7" />
      <line x1="9" y1="20" x2="15" y2="20" />
      <line x1="12" y1="4" x2="12" y2="20" />
    </svg>
  ),
  Calendar: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <rect x="3" y="4" width="18" height="18" rx="2" ry="2" />
      <line x1="16" y1="2" x2="16" y2="6" />
      <line x1="8" y1="2" x2="8" y2="6" />
      <line x1="3" y1="10" x2="21" y2="10" />
    </svg>
  ),
  Trash: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <polyline points="3 6 5 6 21 6" />
      <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" />
    </svg>
  ),
  Replace: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M16 3h5v5" />
      <path d="M8 21H3v-5" />
      <path d="M21 3L9 15" />
      <path d="M3 21l12-12" />
    </svg>
  ),
  Scale: () => (
    <svg viewBox="0 0 24 24" fill="none" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z" />
      <path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z" />
      <path d="M7 21h10" />
      <path d="M12 3v18" />
      <path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2" />
    </svg>
  ),
};

// Pipeline steps configuration
const PIPELINE_STEPS = [
  { id: 'profile', title: 'Profiling Columns', description: 'Analyzing data types and distributions', icon: Icons.Search },
  { id: 'detect', title: 'Detecting Data Issues', description: 'Finding missing values and anomalies', icon: Icons.AlertCircle },
  { id: 'infer', title: 'Inferring Column Intent', description: 'Understanding semantic meaning', icon: Icons.Target },
  { id: 'validate', title: 'Validating Transformations', description: 'Ensuring safe preprocessing', icon: Icons.Shield },
];

// Thinking messages that simulate AI processing
const THINKING_MESSAGES = [
  "Checking missing value patterns...",
  "Evaluating categorical cardinality...",
  "Assessing outlier validity...",
  "Analyzing column correlations...",
  "Determining optimal encoding strategy...",
  "Validating data type consistency...",
  "Profiling statistical distributions...",
  "Detecting potential data quality issues...",
  "Inferring feature importance...",
  "Calculating normalization parameters...",
];

export default function Upload() {
  const [file, setFile] = useState(null);
  const [fileMetadata, setFileMetadata] = useState(null);
  const [isDragging, setIsDragging] = useState(false);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [currentStep, setCurrentStep] = useState(-1);
  const [completedSteps, setCompletedSteps] = useState([]);
  const [thinkingMessage, setThinkingMessage] = useState('');
  const [results, setResults] = useState(null);
  const [progress, setProgress] = useState(0);
  const [status, setStatus] = useState('idle'); // idle, analyzing, completed, error
  const [downloadInfo, setDownloadInfo] = useState(null);
  const [connectionStatus, setConnectionStatus] = useState('');
  
  const fileInputRef = useRef(null);
  const thinkingIntervalRef = useRef(null);
  const actionSectionRef = useRef(null);
  const thinkingSectionRef = useRef(null);

  // Auto scroll function
  const scrollToSection = useCallback((ref) => {
    if (ref.current) {
      ref.current.scrollIntoView({
        behavior: 'smooth',
        block: 'start',
      });
    }
  }, []);

  // Format file size
  const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  // Parse CSV to get metadata
  const parseCSVMetadata = useCallback((content) => {
    const lines = content.split('\n').filter(line => line.trim());
    const headers = lines[0]?.split(',') || [];
    return {
      rows: lines.length - 1,
      columns: headers.length,
      headers: headers.map(h => h.trim().replace(/"/g, '')),
    };
  }, []);

  // Handle file selection
  const handleFileSelect = useCallback(async (selectedFile) => {
    if (!selectedFile || !selectedFile.name.endsWith('.csv')) {
      alert('Please select a valid CSV file');
      return;
    }

    setFile(selectedFile);
    setResults(null);
    setStatus('idle');

    // Read file to get metadata
    const reader = new FileReader();
    reader.onload = (e) => {
      const content = e.target?.result;
      const metadata = parseCSVMetadata(content);
      setFileMetadata({
        name: selectedFile.name,
        size: formatFileSize(selectedFile.size),
        ...metadata,
      });

      // Auto scroll to action section after file selection
      setTimeout(() => scrollToSection(actionSectionRef), 500);
    };
    reader.readAsText(selectedFile);
  }, [parseCSVMetadata, scrollToSection]);

  // Drag and drop handlers
  const handleDragOver = useCallback((e) => {
    e.preventDefault();
    setIsDragging(true);
  }, []);

  const handleDragLeave = useCallback((e) => {
    e.preventDefault();
    setIsDragging(false);
  }, []);

  const handleDrop = useCallback((e) => {
    e.preventDefault();
    setIsDragging(false);
    const droppedFile = e.dataTransfer.files[0];
    handleFileSelect(droppedFile);
  }, [handleFileSelect]);

  const handleInputChange = useCallback((e) => {
    const selectedFile = e.target.files?.[0];
    if (selectedFile) {
      handleFileSelect(selectedFile);
    }
  }, [handleFileSelect]);

  const removeFile = useCallback(() => {
    setFile(null);
    setFileMetadata(null);
    setResults(null);
    setStatus('idle');
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  }, []);

  // Cycle through thinking messages
  useEffect(() => {
    if (isAnalyzing) {
      let messageIndex = 0;
      setThinkingMessage(THINKING_MESSAGES[0]);
      
      thinkingIntervalRef.current = setInterval(() => {
        messageIndex = (messageIndex + 1) % THINKING_MESSAGES.length;
        setThinkingMessage(THINKING_MESSAGES[messageIndex]);
      }, 2000);
    } else {
      if (thinkingIntervalRef.current) {
        clearInterval(thinkingIntervalRef.current);
      }
    }
    
    return () => {
      if (thinkingIntervalRef.current) {
        clearInterval(thinkingIntervalRef.current);
      }
    };
  }, [isAnalyzing]);

  // Upload and analyze via API
  const startAnalysis = useCallback(async () => {
    if (!file) return;
    
    setIsAnalyzing(true);
    setStatus('analyzing');
    setCurrentStep(0);
    setCompletedSteps([]);
    setProgress(0);
    setDownloadInfo(null);
    
    const formData = new FormData();
    formData.append("file", file);

    try {
      // Start pipeline animation
      const pipelinePromise = (async () => {
        for (let i = 0; i < PIPELINE_STEPS.length; i++) {
          setCurrentStep(i);
          await new Promise(resolve => setTimeout(resolve, 1500 + Math.random() * 1000));
          setCompletedSteps(prev => [...prev, PIPELINE_STEPS[i].id]);
        }
      })();

      // Make the actual API call
      const response = await axios.post("http://127.0.0.1:8000/upload/", formData, {
        headers: { "Content-Type": "multipart/form-data" },
        onUploadProgress: (progressEvent) => {
          const percent = Math.round((progressEvent.loaded * 100) / progressEvent.total);
          setProgress(percent);
        },
      });

      // Wait for pipeline animation to complete
      await pipelinePromise;
      setProgress(100);

      // Process API response
      const apiResults = {
        datasetOperations: [],
        columns: [],
        summary: '',
      };

      // Handle column operations from API
      if (response.data.ai_analysis?.column_operations) {
        const columnOps = response.data.ai_analysis.column_operations;
        
        // Dataset-wide operations
        if (columnOps.dataset_wide) {
          apiResults.datasetOperations = columnOps.dataset_wide.map(op => ({
            name: op,
            description: 'Applied to entire dataset',
            icon: Icons.Database,
          }));
        }

        // Column-specific operations
        Object.entries(columnOps).forEach(([colName, ops]) => {
          if (colName !== 'dataset_wide' && Array.isArray(ops)) {
            apiResults.columns.push({
              name: colName,
              type: 'detected',
              actions: ops.map(op => ({ action: op, icon: Icons.Check })),
              reasoning: response.data.ai_analysis?.reasoning || 'AI-determined preprocessing',
            });
          }
        });
      }

      apiResults.summary = response.data.ai_analysis?.reasoning || 
        `Analyzed ${response.data.file_info?.columns || 0} columns and ${response.data.file_info?.rows || 0} rows.`;

      setResults(apiResults);

      // Check for download info
      if (response.data.download) {
        setDownloadInfo(response.data.download);
      }

      // Set connection status
      if (response.data.ai_analysis?.connection_verified) {
        setConnectionStatus("Connected to Mistral AI - Column-wise Mode");
      } else {
        setConnectionStatus("Using fallback recommendations");
      }

      setStatus('completed');
    } catch (error) {
      console.error("Upload error:", error);
      setStatus('error');
      
      // Fallback to mock results if API fails
      const mockResults = generateMockResults(fileMetadata);
      setResults(mockResults);
      setConnectionStatus("API unavailable - showing demo results");
    } finally {
      setIsAnalyzing(false);
      setCurrentStep(-1);
    }
  }, [file, fileMetadata]);

  // Generate mock preprocessing results
  const generateMockResults = (metadata) => {
    const columnTypes = ['numeric', 'categorical', 'datetime', 'text'];
    const actions = [
      { action: 'Fill Missing', icon: Icons.Replace },
      { action: 'Normalize', icon: Icons.Scale },
      { action: 'Encode', icon: Icons.Hash },
      { action: 'Remove Outliers', icon: Icons.Filter },
      { action: 'Parse Date', icon: Icons.Calendar },
    ];
    
    const columns = metadata?.headers?.map((header, index) => {
      const type = columnTypes[index % columnTypes.length];
      const columnActions = actions
        .filter(() => Math.random() > 0.5)
        .slice(0, 2 + Math.floor(Math.random() * 2));
      
      return {
        name: header,
        type,
        actions: columnActions,
        reasoning: generateReasoning(type, columnActions),
      };
    }) || [];
    
    return {
      datasetOperations: [
        { name: 'Remove Duplicates', description: '23 duplicates found', icon: Icons.Trash },
        { name: 'Handle Missing', description: '156 missing values', icon: Icons.AlertCircle },
        { name: 'Normalize Features', description: '8 columns scaled', icon: Icons.Scale },
        { name: 'Encode Categories', description: '4 columns encoded', icon: Icons.Hash },
      ],
      columns,
      summary: `The AI analyzed ${metadata?.columns || 0} columns and ${metadata?.rows || 0} rows. Based on the data patterns, column distributions, and semantic analysis, appropriate preprocessing transformations have been recommended. The model detected potential data quality issues and suggested safe, reversible operations to prepare your dataset for machine learning pipelines.`,
    };
  };

  const generateReasoning = (type, actions) => {
    const reasonings = {
      numeric: "Detected as numeric feature. Recommended normalization for optimal model performance.",
      categorical: "Identified as categorical variable. Suggested encoding based on cardinality analysis.",
      datetime: "Recognized datetime format. Extracted temporal features for time-series analysis.",
      text: "Classified as text field. Applied appropriate text preprocessing pipeline.",
    };
    return reasonings[type] || "Analyzed and preprocessed based on detected patterns.";
  };

  const handleDownload = async () => {
    if (!downloadInfo) {
      // Fallback to JSON download if no API download available
      const dataStr = JSON.stringify(results, null, 2);
      const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);
      const exportFileDefaultName = 'preprocessing_results.json';
      
      const linkElement = document.createElement('a');
      linkElement.setAttribute('href', dataUri);
      linkElement.setAttribute('download', exportFileDefaultName);
      linkElement.click();
      return;
    }
    
    try {
      const response = await axios.get(`http://127.0.0.1:8000/download/${downloadInfo.filename}`, {
        responseType: 'blob'
      });
      
      // Create download link
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', downloadInfo.filename);
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error("Download error:", error);
    }
  };

  return (
    <div className="upload-container">
      {/* Background Effects */}
      <div className="background-effects">
        <div className="gradient-orb orb-1" />
        <div className="gradient-orb orb-2" />
        <div className="gradient-orb orb-3" />
        <div className="grid-overlay" />
      </div>

      {/* Main Content */}
      <main className="main-content">
        {/* Header */}
        <header className="header">
          <div className="header-badge">
            <span className="badge-dot" />
            AI Preprocessing Engine
          </div>
          <h1>CSV Auto-Preprocessing</h1>
          <p>
            Upload your dataset and let AI analyze, detect issues, and recommend 
            optimal preprocessing transformations like a professional data scientist.
          </p>
        </header>

        {/* Upload Zone */}
        <div className="upload-zone-wrapper">
          <div
            className={`upload-zone ${isDragging ? 'drag-over' : ''} ${file ? 'has-file' : ''}`}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onDrop={handleDrop}
            onClick={() => fileInputRef.current?.click()}
          >
            <div className="upload-icon-wrapper">
              <div className="upload-icon-bg" />
              <div className="upload-icon">
                <Icons.Upload />
              </div>
            </div>
            <div className="upload-text">
              <h3>
                <span>Drop your CSV</span> or click to browse
              </h3>
              <p>Supports CSV files up to 50MB</p>
            </div>
            <input
              ref={fileInputRef}
              type="file"
              accept=".csv"
              onChange={handleInputChange}
              className="upload-input"
            />
          </div>

          {/* File Preview */}
          {fileMetadata && (
            <div className="file-preview">
              <div className="file-info">
                <div className="file-icon">
                  <Icons.File />
                </div>
                <div className="file-details">
                  <div className="file-name">{fileMetadata.name}</div>
                  <div className="file-meta">
                    <span>
                      <Icons.HardDrive />
                      {fileMetadata.size}
                    </span>
                    <span>
                      <Icons.Rows />
                      {fileMetadata.rows.toLocaleString()} rows
                    </span>
                    <span>
                      <Icons.Columns />
                      {fileMetadata.columns} columns
                    </span>
                  </div>
                </div>
                <button className="remove-file" onClick={(e) => { e.stopPropagation(); removeFile(); }}>
                  <Icons.X />
                </button>
              </div>
            </div>
          )}
        </div>

        {/* Action Button */}
        <div className="action-section" ref={actionSectionRef}>
          <button
            className="analyze-btn"
            onClick={() => {
              startAnalysis();
              setTimeout(() => scrollToSection(thinkingSectionRef), 100);
            }}
            disabled={!file || isAnalyzing}
          >
            <span>
              {isAnalyzing ? 'Analyzing...' : 'Upload & Analyze'}
              <Icons.ArrowRight />
            </span>
          </button>
        </div>

        {/* AI Thinking Section */}
        {isAnalyzing && (
          <section className="ai-thinking-section" ref={thinkingSectionRef}>
            <div className="thinking-card">
              <div className="thinking-header">
                <div className="ai-avatar">
                  <Icons.Brain />
                </div>
                <div className="thinking-title">
                  <h2>AI is analyzing your data</h2>
                  <p>Applying intelligent preprocessing decisions</p>
                </div>
              </div>

              {/* File Preprocessing Animation */}
              <div className="file-process-visualization">
                {/* Source File */}
                <div className="process-file source-file">
                  <div className="file-icon-large">
                    <Icons.File />
                  </div>
                  <div className="file-label">Raw CSV</div>
                  <div className="file-rows">
                    {[...Array(5)].map((_, i) => (
                      <div key={`row-${i}`} className="data-row" style={{ animationDelay: `${i * 0.1}s` }}>
                        <span className="cell" />
                        <span className="cell" />
                        <span className="cell" />
                        <span className="cell highlight" />
                      </div>
                    ))}
                  </div>
                </div>

                {/* Processing Flow */}
                <div className="process-flow">
                  <div className="flow-line">
                    <div className="flow-particle" />
                    <div className="flow-particle" style={{ animationDelay: '0.3s' }} />
                    <div className="flow-particle" style={{ animationDelay: '0.6s' }} />
                  </div>
                  <div className="process-gear">
                    <Icons.Zap />
                    <div className="gear-ring" />
                  </div>
                  <div className="flow-line">
                    <div className="flow-particle" />
                    <div className="flow-particle" style={{ animationDelay: '0.3s' }} />
                    <div className="flow-particle" style={{ animationDelay: '0.6s' }} />
                  </div>
                </div>

                {/* Processed File */}
                <div className="process-file processed-file">
                  <div className="file-icon-large success">
                    <Icons.CheckCircle />
                  </div>
                  <div className="file-label">Processed</div>
                  <div className="file-rows">
                    {[...Array(5)].map((_, i) => (
                      <div key={`row-proc-${i}`} className="data-row processed" style={{ animationDelay: `${i * 0.1 + 0.5}s` }}>
                        <span className="cell" />
                        <span className="cell" />
                        <span className="cell" />
                        <span className="cell success" />
                      </div>
                    ))}
                  </div>
                </div>

                {/* Floating Sparkles */}
                <div className="sparkle-container">
                  {[...Array(6)].map((_, i) => (
                    <div key={`sparkle-${i}`} className="floating-sparkle" style={{ animationDelay: `${i * 0.4}s` }} />
                  ))}
                </div>
              </div>

              {/* Pipeline Steps */}
              <div className="pipeline-steps">
                {PIPELINE_STEPS.map((step, index) => {
                  const isActive = currentStep === index;
                  const isCompleted = completedSteps.includes(step.id);
                  const StepIcon = step.icon;
                  
                  return (
                    <div
                      key={step.id}
                      className={`pipeline-step ${isActive ? 'active' : ''} ${isCompleted ? 'completed' : ''}`}
                    >
                      <div className="step-indicator">
                        {isActive && <div className="step-spinner" />}
                        {isCompleted ? <Icons.Check /> : <StepIcon />}
                      </div>
                      <div className="step-content">
                        <h4>{step.title}</h4>
                        <p>{step.description}</p>
                      </div>
                      <span className="step-status">
                        {isCompleted ? 'Complete' : isActive ? 'Processing...' : 'Pending'}
                      </span>
                    </div>
                  );
                })}
              </div>

              {/* Thinking Messages */}
              <div className="thinking-messages">
                <div className="thinking-message">
                  <div className="thinking-dots">
                    <span />
                    <span />
                    <span />
                  </div>
                  <p>{thinkingMessage}</p>
                </div>
              </div>

              {/* Progress Bar */}
              <div className="progress-bar">
                <div className="progress-fill" style={{ width: `${progress}%` }} />
              </div>
            </div>
          </section>
        )}

        {/* Results Section */}
        {results && !isAnalyzing && (
          <section className="results-section">
            <div className="results-header">
              <h2>
                <Icons.CheckCircle />
                Analysis Complete
              </h2>
              <button className="download-btn" onClick={handleDownload}>
                <Icons.Download />
                Download Results
              </button>
            </div>

            {/* Dataset Operations Card */}
            <div className="dataset-card">
              <h3>
                <Icons.Database />
                Dataset-wide Operations
              </h3>
              <div className="dataset-operations">
                {results.datasetOperations.map((op, index) => {
                  const OpIcon = op.icon;
                  return (
                    <div key={index} className="operation-item">
                      <div className="operation-icon">
                        <OpIcon />
                      </div>
                      <div className="operation-details">
                        <h4>{op.name}</h4>
                        <p>{op.description}</p>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Column Cards */}
            <div className="columns-grid">
              {results.columns.map((column, index) => (
                <div key={index} className="column-card">
                  <div className="column-header">
                    <span className="column-name">{column.name}</span>
                    <span className={`column-type ${column.type}`}>{column.type}</span>
                  </div>
                  <div className="column-actions">
                    {column.actions.map((action, actionIndex) => {
                      const ActionIcon = action.icon;
                      return (
                        <span key={actionIndex} className="action-tag">
                          <ActionIcon />
                          {action.action}
                        </span>
                      );
                    })}
                  </div>
                  <div className="column-reasoning">
                    <p>
                      <strong>AI Reasoning: </strong>
                      {column.reasoning}
                    </p>
                  </div>
                </div>
              ))}
            </div>

            {/* AI Reasoning Card */}
            <div className="reasoning-card">
              <div className="reasoning-header">
                <Icons.Sparkles />
                <h3>AI Summary & Recommendations</h3>
              </div>
              <div className="reasoning-content">
                <p>{results.summary}</p>
              </div>
            </div>
          </section>
        )}
      </main>

      {/* Status Bar */}
      {status !== 'idle' && (
        <div className="status-bar">
          <span className={`status-dot ${status === 'analyzing' ? 'analyzing' : ''}`} />
          {status === 'analyzing' && 'AI is analyzing your dataset...'}
          {status === 'completed' && 'Analysis complete — Results ready'}
          {status === 'error' && 'An error occurred'}
        </div>
      )}
    </div>
  );
}
