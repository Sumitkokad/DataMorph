# 🧬 DataMorph — AI-Native Data Preprocessing Platform

<div align="center">

> **Transform raw, messy datasets into ML-ready intelligence using AI reasoning with rule-based safety**

![divider](https://capsule-render.vercel.app/api?type=rect&color=0:0d0d0d,100:5b2cff&height=2)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-0d0d0d?style=for-the-badge&logo=python&logoColor=white)](#)
[![Flask](https://img.shields.io/badge/backend-flask-5b2cff?style=for-the-badge&logo=flask&logoColor=white)](#)
[![Mistral 7B](https://img.shields.io/badge/LLM-Mistral%207B-8a5cff?style=for-the-badge)](#)
[![Local AI](https://img.shields.io/badge/Local-LLM%20Only-black?style=for-the-badge)](#)
[![License MIT](https://img.shields.io/badge/license-MIT-1e1e1e?style=for-the-badge)](#)

</div>

---

## 🧠 What is DataMorph?

**DataMorph** is a **production-grade, AI-guided data preprocessing engine** built to safely analyze, validate, and prepare real-world datasets for machine learning and analytics.

Unlike traditional pipelines that blindly apply transformations, DataMorph **understands column intent**, **detects data risks**, and **applies only logically justified preprocessing steps** — never corrupting original data.

---

## ✨ Core Capabilities

### 🧬 Intelligent Column Understanding
DataMorph infers column semantics before acting.

```python
column_intent = {
    "user_id": "identifier",          # IDs / keys
    "age": "numeric_continuous",      # Continuous values
    "gender": "categorical_binary",   # Binary categorical
    "city": "categorical_low",        # Low-cardinality categorical
    "created_at": "datetime",         # Temporal data
    "review": "free_text",            # Text data
    "target": "label"                 # ML target (protected)
}
