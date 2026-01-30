<div align="center">

# 🧬 DataMorph  
### AI-Native • Context-Aware • Safe Data Preprocessing Platform

<img src="https://img.shields.io/badge/Status-Active%20Development-8B5CF6?style=for-the-badge&labelColor=000000"/>
<img src="https://img.shields.io/badge/AI-Mistral%207B-9333EA?style=for-the-badge&labelColor=000000"/>
<img src="https://img.shields.io/badge/Backend-Flask-6366F1?style=for-the-badge&labelColor=000000"/>
<img src="https://img.shields.io/badge/Python-3.10+-7C3AED?style=for-the-badge&labelColor=000000"/>

<br/>

> **DataMorph transforms raw, messy datasets into ML-ready intelligence using  
AI reasoning + strict rule enforcement — with zero data corruption.**

<br/>

<a href="#"><img src="https://img.shields.io/badge/AI-Powered-Black?style=for-the-badge"/></a>
<a href="#"><img src="https://img.shields.io/badge/Safe-by-Design-Black?style=for-the-badge"/></a>
<a href="#"><img src="https://img.shields.io/badge/Production-Grade-Black?style=for-the-badge"/></a>

</div>

---

## 🖤 What is DataMorph?

```
┌──────────────────────────────────────────────┐
│ Traditional Preprocessing Pipelines          │
│                                              │
│ ❌ Blind rules                                │
│ ❌ Hard-coded logic                           │
│ ❌ Silent data corruption                    │
│ ❌ No explainability                         │
└──────────────────────────────────────────────┘

┌──────────────────────────────────────────────┐
│ DataMorph (AI-Native Engine)                 │
│                                              │
│ ✅ Column-wise intelligence                  │
│ ✅ Context-aware decisions                   │
│ ✅ Rule-based safety                         │
│ ✅ Explainable AI reasoning                  │
└──────────────────────────────────────────────┘
```

**DataMorph behaves like a senior data scientist, not a script.**  
It understands column intent, validates risks, and applies only safe operations.

---

## 🧠 Architecture Overview

```
┌──────────────┐
│ Raw Dataset  │
└──────┬───────┘
       ▼
┌────────────────────────┐
│ Rule Engine             │  ← hard constraints
│ (IDs, targets, ranges) │
└──────┬─────────────────┘
       ▼
┌────────────────────────┐
│ AI Reasoning Layer     │  ← Mistral / Ollama
│ (context awareness)    │
└──────┬─────────────────┘
       ▼
┌────────────────────────┐
│ Safety Validator       │  ← blocks risky ops
└──────┬─────────────────┘
       ▼
┌────────────────────────┐
│ Preprocessing Plan     │  ← safe & explainable
└────────────────────────┘
```

---

## 🔥 Core Features

```
┌──────────────────────────────────────────────┐
│ ✔ Column-wise intelligent preprocessing     │
│ ✔ Rule-based + AI-guided decisions           │
│ ✔ Non-destructive transformations            │
│ ✔ Large & messy dataset support               │
│ ✔ Local LLM (no API cost)                     │
│ ✔ Deterministic fallback logic                │
│ ✔ Memory-optimized inference                  │
└──────────────────────────────────────────────┘
```

---

## 🧩 Column Intelligence

DataMorph automatically detects:

- Identifier columns (ID, UUID, keys)
- Target / label columns
- Numeric (continuous / discrete)
- Categorical (binary / ordinal / high-cardinality)
- Datetime columns
- Free-text columns

Each column is processed **independently and safely**.

---

## 🛡️ Safety-First Philosophy

```
VALIDATE → FLAG → DECIDE → TRANSFORM
```

- ❌ No blind scaling  
- ❌ No unsafe encoding  
- ❌ No silent overwrites  

✔ Original data preserved  
✔ Risky operations blocked  
✔ Full reasoning & logs  

---

## 🤖 AI + Rules (Not Blind AI)

- Rules enforce **non-negotiable constraints**
- AI provides **contextual intelligence**
- AI output is validated before execution

> AI assists — rules decide.

---

## ⚡ Large Dataset Ready

- Chunk-based summarization
- Column-level AI calls
- VRAM-aware inference
- Tested on low-VRAM GPUs (RTX 4050)

---

## 📊 Example AI Output

```json
{
  "Age": ["validate:ranges", "impute:median"],
  "Income": ["detect:outliers_iqr", "scale:robust"],
  "Gender": ["encode:binary"],
  "CustomerID": ["validate:datatypes", "validate:uniqueness"],
  "dataset_wide": ["remove:duplicates_exact", "validate:integrity"]
}
```

---

## 🎯 Use Cases

```
✔ Machine Learning preparation
✔ Data quality validation
✔ Automated preprocessing pipelines
✔ Final-year & research projects
✔ Interview-grade system demos
✔ Startup MVPs
```

---

## ⚙️ Tech Stack

**Backend**
- Python
- Flask
- Pandas, NumPy
- Scikit-learn

**AI Layer**
- Mistral 7B (local)
- Ollama
- Expert-engineered prompts

**Frontend (Optional)**
- React
- Black + Purple AI theme
- Real-time preprocessing visualization

---

## 🚧 Project Status

**Active Development 🚀**

Upcoming:
- Chunk-based AI orchestration
- Domain-aware rules (Finance / Health / HR)
- Column confidence scoring
- Interactive AI reasoning UI

---

## 👨‍💻 Author

**Sumit Ravindra Kokad**  
Computer Science Engineer  
AI / ML • Data Systems • Intelligent Pipelines

---

<div align="center">

### ⭐ Star this repository if DataMorph inspired you

</div>
