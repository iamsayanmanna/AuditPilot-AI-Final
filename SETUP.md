# AuditPilot AI Setup Guide

## Prerequisites

Before running AuditPilot AI, make sure you have installed:

* Python 3.10+
* Node.js 18+
* npm
* Git

---

# Clone Repository

```bash
git clone https://github.com/your-username/AuditPilot-AI.git

cd AuditPilot-AI
```

---

# Backend Setup

Navigate to backend folder:

```bash
cd backend
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend server:

```bash
python api.py
```

Backend will start at:

```text
http://localhost:5000
```

---

# Frontend Setup

Open a new terminal.

Navigate to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

Frontend will start at:

```text
http://localhost:5173
```

---

# Default Login Credentials

## Admin

```text
Username: admin
Password: admin123
```

## Auditor

```text
Username: auditor
Password: audit123
```

## Accountant

```text
Username: accountant
Password: acc123
```

---

# Available Features

* Multi-Agent Investigation
* Risk Analysis
* Compliance Verification
* Invoice Intelligence
* Audit Trail Logs
* Role Based Access Control
* Session Authentication
* Executive PDF Reports
* Natural Language Investigation

---

# Troubleshooting

## Backend Not Starting

Check:

```bash
pip install -r requirements.txt
```

## Frontend Not Starting

Check:

```bash
npm install
```

## API Connection Error

Verify backend is running:

```text
http://localhost:5000/health
```

Expected Response:

```json
{
  "status": "running",
  "project": "AuditPilot AI"
}
```
