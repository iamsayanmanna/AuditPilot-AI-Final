# AuditPilot AI API Documentation

## Base URL

```text
http://localhost:5000
```

---

# Health Check

## GET /health

Check API status.

### Request

```http
GET /health
```

### Response

```json
{
  "status": "running",
  "project": "AuditPilot AI"
}
```

---

# Authentication

## GET /test-auth

Generate test authentication token.

### Request

```http
GET /test-auth
```

### Response

```json
{
  "authenticated": true,
  "role": "ADMIN",
  "token": "uuid-token"
}
```

---

# Investigation Engine

## GET /investigate

Run complete AI investigation workflow.

### Request

```http
GET /investigate
```

### Response

```json
{
  "case_id": "CASE001",
  "risk_score": 72,
  "risk_level": "HIGH",
  "audit_finding": "Suspicious transaction detected",
  "compliance_status": "COMPLIANT",
  "case_status": "UNDER_REVIEW",
  "approval_decision": "ESCALATE",
  "executive_summary": "...",
  "ai_recommendations": []
}
```

---

# Investigation History

## GET /history

Returns recent investigations.

### Request

```http
GET /history?token=YOUR_TOKEN
```

### Success Response

```json
[
  {
    "case_id": "CASE001",
    "amount": 5000,
    "risk_score": 72,
    "recommendation": "REVIEW"
  }
]
```

### Error Response

```json
{
  "error": "Unauthorized"
}
```

---

# Dashboard Statistics

## GET /stats

Returns analytics information.

### Request

```http
GET /stats?token=YOUR_TOKEN
```

### Response

```json
{
  "total_investigations": 50,
  "high_risk_cases": 12,
  "compliance_alerts": 3,
  "invoices_analyzed": 20
}
```

---

# Audit Logs

## GET /logs

Returns recent audit trail logs.

### Request

```http
GET /logs?token=YOUR_TOKEN
```

### Response

```json
[
  "Investigation executed: CASE001",
  "Investigation executed: CASE002"
]
```

---

# Invoice Intelligence

## POST /upload-invoice

Analyze uploaded invoice.

### Request

```http
POST /upload-invoice
Content-Type: multipart/form-data
```

### Form Field

```text
invoice
```

### Response

```json
{
  "invoice_number": "1001",
  "amount": 2500,
  "match_status": "MATCHED",
  "risk": "LOW"
}
```

---

# Case Notes

## POST /add-note

Save investigation notes.

### Request

```json
{
  "case_id": "CASE001",
  "note": "Potential anomaly detected"
}
```

### Response

```json
{
  "status": "Note Added Successfully"
}
```

---

# Natural Language Investigation

## POST /nl-investigation

Ask investigation questions in natural language.

### Request

```json
{
  "query": "Show high risk transactions"
}
```

### Response

```json
{
  "result": "3 high risk transactions found"
}
```

---

# PDF Reporting

## GET /export-report

Generate executive PDF report.

### Request

```http
GET /export-report
```

### Response

```text
audit_report.pdf
```

---

# Permissions

## GET /permissions/<role>

Returns role permissions.

### Example

```http
GET /permissions/ADMIN
```

### Response

```json
{
  "role": "ADMIN",
  "permissions": [
    "VIEW_CASES",
    "APPROVE_CASES",
    "MANAGE_USERS",
    "VIEW_LOGS"
  ]
}
```

---

# Security Features

* Session Authentication
* Token Validation
* Role Based Access Control (RBAC)
* Route Protection
* Audit Security Controls

---

# Supported Roles

## ADMIN

* View Cases
* Approve Cases
* Manage Users
* View Logs

## AUDITOR

* View Cases
* Add Notes
* View Logs

## ACCOUNTANT

* View Cases
* Add Notes
