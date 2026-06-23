import { useState, useEffect } from "react";
import "./App.css";

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid
} from "recharts";

function App() {
  const [data, setData] = useState(null);
  const [history, setHistory] = useState([]);
  const [invoiceResult, setInvoiceResult] = useState(null);
  const [report, setReport] = useState(null);
  const [note, setNote] = useState("");
  const [logs, setLogs] = useState([]);
  const [nlQuery, setNlQuery] = useState("");
const [nlResult, setNlResult] = useState("");
const [isLoggedIn, setIsLoggedIn] = useState(false);

const [role, setRole] = useState("");

const [username, setUsername] = useState("");

const [password, setPassword] = useState("");
const [errorMessage, setErrorMessage] = useState("");
const [successMessage, setSuccessMessage] = useState("");
const [token, setToken] = useState("");

const [activePage, setActivePage] =
useState("dashboard");

const riskData = [
  { name: "Low", value: 45 },
  { name: "Medium", value: 30 },
  { name: "High", value: 15 },
  { name: "Critical", value: 10 }
];

const COLORS = [
  "#22c55e",
  "#eab308",
  "#f97316",
  "#ef4444"
];

const monthlyData = [
  { month: "Jan", cases: 45 },
  { month: "Feb", cases: 62 },
  { month: "Mar", cases: 58 },
  { month: "Apr", cases: 80 },
  { month: "May", cases: 95 },
  { month: "Jun", cases: 120 }
];

  const [stats, setStats] = useState({
  total_investigations: 0,
  high_risk_cases: 0,
  compliance_alerts: 0,
  invoices_analyzed: 0
});

  const runInvestigation = async () => {
    try {
      const response = await fetch(
        "http://localhost:5000/investigate"
      );

      const result = await response.json();

      setData(result);

      let recommendation = "";

if (result.risk_level === "LOW") {
  recommendation = "Approve Transaction";
}
else if (result.risk_level === "MEDIUM") {
  recommendation = "Review With Accounting Team";
}
else if (result.risk_level === "HIGH") {
  recommendation = "Escalate To Finance Manager";
}
else {
  recommendation = "Freeze Payment Immediately";
}



setReport({
  risk_level: result.risk_level,
  audit_finding: result.audit_finding,
  compliance_status: result.compliance_status,
  recommendation: recommendation,
  case_status: result.case_status,
  approval_decision: result.approval_decision,
  executive_summary: result.executive_summary,
  ai_recommendations: result.ai_recommendations,
  alert_message: result.alert_message,
alert_severity: result.alert_severity,
agent_flow: result.registered_agents,
mcp_tools: result.mcp_tools_used
});


      loadHistory();
      loadStats();
      loadLogs();
    } catch (error) {
      console.error(error);
      setErrorMessage(
  "AuditPilot API Connection Failed"
);
    }
  };

  const handleInvoiceUpload = async (event) => {

  const file = event.target.files[0];

  if (!file) return;

  const formData = new FormData();

  formData.append("invoice", file);

  const response = await fetch(
    "http://localhost:5000/upload-invoice",
    {
      method: "POST",
      body: formData,
    }
  );

  const result = await response.json();

  setInvoiceResult(result);
};

const loadHistory = async () => {

  const response = await fetch(
    `http://localhost:5000/history?token=${token}`
  );

  const result = await response.json();

  setHistory(
    Array.isArray(result)
      ? result
      : []
  );
};

const loadStats = async () => {

  const response = await fetch(
    `http://localhost:5000/stats?token=${token}`
  );

  const result = await response.json();

  setStats(result);
};

const loadLogs = async () => {

  const response = await fetch(
    `http://localhost:5000/logs?token=${token}`
  );

  const result = await response.json();

  setLogs(
    Array.isArray(result)
      ? result
      : []
  );
};

const saveNote = async () => {

  if (!data) {
    alert("Run Investigation First");
    return;
  }

  const response = await fetch(
    "http://localhost:5000/add-note",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        case_id: data.case_id,
        note: note
      })
    }
  );

  const result = await response.json();

  setSuccessMessage(
  result.status
);
};


const runNLInvestigation = async () => {

  const response = await fetch(
    "http://localhost:5000/nl-investigation",
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        query: nlQuery
      })
    }
  );

  const result = await response.json();

  setNlResult(result.result);
};

useEffect(() => {

  if(token){

    loadHistory();
    loadStats();
    loadLogs();

  }

}, [token]);


if (!isLoggedIn) {

  return (

    <div className="login-container">

      <h1>AuditPilot AI</h1>

      <h3>Enterprise Login</h3>
      {errorMessage && (
  <p className="error-box">
    {errorMessage}
  </p>
)}

      <input
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button
        onClick={async () => {

          if (
  username === "admin" &&
  password === "admin123"
) {

  const response = await fetch(
    "http://localhost:5000/test-auth"
  );

  const result = await response.json();

  console.log("LOGIN RESULT:", result);
console.log("TOKEN:", result.token);

  setToken("demo-admin-token");

setRole("ADMIN");

setIsLoggedIn(true);
}

          else if (
            username === "auditor" &&
            password === "audit123"
          ) {
            setRole("AUDITOR");
            setIsLoggedIn(true);
          }

          else if (
            username === "accountant" &&
            password === "acc123"
          ) {
            setRole("ACCOUNTANT");
            setIsLoggedIn(true);
          }

          else {
            setErrorMessage(
  "Invalid Username or Password"
);
          }

        }}
      >

        Login

      </button>

    </div>

  );

}

  return (
    <div className="app-layout">

  <div className="sidebar">

    <h2>AuditPilot AI</h2>

   <button
className={
activePage === "dashboard"
? "active-menu"
: ""
}
onClick={() =>
setActivePage("dashboard")
}
>
Dashboard
</button>

<button
className={
activePage === "investigations"
? "active-menu"
: ""
}
onClick={() =>
setActivePage("investigations")
}
>
Investigations
</button>

<button
className={
activePage === "reports"
? "active-menu"
: ""
}
onClick={() =>
setActivePage("reports")
}
>
 Reports
</button>

<button
className={
activePage === "analytics"
? "active-menu"
: ""
}
onClick={() =>
setActivePage("analytics")
}
>
 Analytics
</button>

<button
className={
activePage === "invoices"
? "active-menu"
: ""
}
onClick={() =>
setActivePage("invoices")
}
>
 Invoices
</button>

<button
className={
activePage === "security"
? "active-menu"
: ""
}
onClick={() =>
setActivePage("security")
}
>
 Security
</button>

<button
className={
activePage === "settings"
? "active-menu"
: ""
}
onClick={() =>
setActivePage("settings")
}
>
 Settings
</button>

    <button
      onClick={() => {
        setIsLoggedIn(false);
        setToken("");
      }}
    >
       Logout
    </button>

  </div>

  <div className="container">

{activePage === "dashboard" && (
<>

<div className="header">
        <h1>AuditPilot AI</h1>
        <p>Enterprise Financial Investigation Platform</p>

        <p>
  Logged In As:
  <strong> {role}</strong>
</p>

{successMessage && (
  <p className="success-box">
    {successMessage}
  </p>
)}

{errorMessage && (
  <p className="error-box">
    {errorMessage}
  </p>
)}

      </div>

      <div className="stats">

        <div className="stat-card">
          <h3>Total Cases</h3>
          <h2>{stats.total_investigations}</h2>
        </div>

        <div className="stat-card">
          <h3> High Risk Cases</h3>
          <h2>{stats.high_risk_cases}</h2>
        </div>

        <div className="stat-card">
          <h3>Financial Exposure</h3>
          <h2>{stats.compliance_alerts}</h2>
        </div>

        <div className="stat-card">
          <h3>Compliance Rate</h3>
          <h2>{stats.invoices_analyzed}</h2>
        </div>

      </div>

<div className="dashboard-card">

<h2>Risk Distribution</h2>

<div style={{ width: "100%", height: 350 }}>

<ResponsiveContainer>

<PieChart>

<Pie
  data={riskData}
  cx="50%"
  cy="50%"
  outerRadius={120}
  dataKey="value"
>

{riskData.map((entry, index) => (
  <Cell
    key={index}
    fill={COLORS[index]}
  />
))}

</Pie>

<Tooltip />

</PieChart>

</ResponsiveContainer>

</div>

</div>

<div className="dashboard-card">

<h2>Monthly Investigation Trend</h2>

<div
  style={{
    width: "100%",
    height: 350
  }}
>

<ResponsiveContainer>

<LineChart data={monthlyData}>

<CartesianGrid strokeDasharray="3 3" />

<XAxis dataKey="month" />

<YAxis />

<Tooltip />

<Line
  type="monotone"
  dataKey="cases"
  stroke="#2563eb"
  strokeWidth={3}
/>

</LineChart>

</ResponsiveContainer>

</div>

</div>



<div className="dashboard-card">

<h2>Executive Command Center</h2>

<div className="stats">

<div className="stat-card">
<h3> Total Exposure</h3>
<h2>$1.2M</h2>
</div>

<div className="stat-card">
<h3> Fraud Alerts</h3>
<h2>12</h2>
</div>

<div className="stat-card">
<h3> Compliance Score</h3>
<h2>98%</h2>
</div>

<div className="stat-card">
<h3> High Risk Cases</h3>
<h2>27</h2>
</div>

</div>

</div>


<div className="dashboard-card">

<h2>Business Impact</h2>

<div className="stats">

<div className="stat-card">
<h3> Estimated Savings</h3>
<h2>$120K</h2>
</div>

<div className="stat-card">
<h3> Investigation Time</h3>
<h2>2h → 5m</h2>
</div>

<div className="stat-card">
<h3> Compliance Accuracy</h3>
<h2>98%</h2>
</div>

<div className="stat-card">
<h3> Productivity Gain</h3>
<h2>85%</h2>
</div>

</div>

</div>


      <div className="dashboard-card">

  <h2>Executive Analytics Dashboard</h2>

  <div className="stats">

    <div className="stat-card">
      <h3>Total Cases</h3>
      <h2>{stats.total_investigations}</h2>
    </div>

    <div className="stat-card">
      <h3>High Risk Cases</h3>
      <h2>{stats.high_risk_cases}</h2>
    </div>

    <div className="stat-card">
      <h3>Compliance Rate</h3>
      <h2>98%</h2>
    </div>

    <div className="stat-card">
      <h3>Approval Rate</h3>
      <h2>92%</h2>
    </div>

  </div>

</div>

      <div className="dashboard-card">

        <h2>Latest Investigation</h2>

        <button onClick={runInvestigation}>
          Run Investigation
        </button>

        {data && (
          <div className="details">

            <p>
              <strong>Case ID:</strong> {data.case_id}
            </p>

            <p>
              <strong>Amount:</strong> ${Math.abs(data.amount)}
            </p>

            <p>
              <strong>Risk Score:</strong> {data.risk_score}/100
            </p>

            <p>
              <strong>Risk Level:</strong> {data.risk_level}
            </p>

            <p>
              <strong>Audit Finding:</strong> {data.audit_finding}
            </p>

            <p>
              <strong>Compliance:</strong> {data.compliance_status}
            </p>

          </div>
        )}

      </div>

      <div className="dashboard-card">

  <h2>Invoice Intelligence</h2>

  <input
    type="file"
    accept=".pdf"
    onChange={handleInvoiceUpload}
  />

  {invoiceResult && (

    <div className="details">

      <p>
        <strong>Invoice Number:</strong>
        {" "}
        {invoiceResult.invoice_number}
      </p>

      <p>
        <strong>Amount:</strong>
        {" "}
        ${invoiceResult.amount}
      </p>
      <p>
  <strong>Match Status:</strong>
  {" "}
  {invoiceResult.match_status}
</p>

<p>
  <strong>Risk:</strong>
  {" "}
  {invoiceResult.risk}
</p>

    </div>

  )}

</div>  

{report && (
  <div className="dashboard-card">

    <h2>AI Executive Report</h2>

    <button
  onClick={() =>
    window.open(
      "http://localhost:5000/export-report",
      "_blank"
    )
  }
>
  Download PDF Report
</button>

    <div className="details">

      <p>
        <strong>Risk Level:</strong> {report.risk_level}
      </p>

      <p>
        <strong>Audit Finding:</strong>
        {" "}
        {report.audit_finding}
      </p>

      <p>
        <strong>Compliance:</strong>
        {" "}
        {report.compliance_status}
      </p>

      <p>
        <strong>Recommendation:</strong>
        {" "}
        {report.recommendation}
      </p>
      <p>
  <strong>Case Status:</strong>
  {" "}
  {report.case_status}
</p>

<p>
  <strong>Approval:</strong>
  {" "}
  {report.approval_decision}
</p>
<p>
  <strong>Executive Summary:</strong>
</p>

<pre>
  {report.executive_summary}
</pre>

<p>
  <strong>Alert Severity:</strong>
  {" "}
  {report.alert_severity}
</p>

<p>
  <strong>Alert:</strong>
  {" "}
  {report.alert_message}
</p>

<p>
  <strong>AI Recommendations:</strong>
</p>

<ul>
  {report.ai_recommendations?.map(
    (item, index) => (
      <li key={index}>
        {item}
      </li>
    )
  )}
</ul>


    </div>

  </div>
)}

{role === "ADMIN" && (

<div className="dashboard-card">

<h2>Admin Workspace</h2>

<p>👤 User Management</p>

<p>⚙️ System Controls</p>

<p>📊 Audit Analytics</p>

</div>

)}

{role === "AUDITOR" && (

<div className="dashboard-card">

<h2>Auditor Workspace</h2>

<p>🔍 Audit Reviews</p>

<p>📋 Compliance Checks</p>

<p>📝 Investigation Notes</p>

</div>

)}

{role === "ACCOUNTANT" && (

<div className="dashboard-card">

<h2>Accounting Workspace</h2>

<p>💰 Payment Approval</p>

<p>📄 Invoice Validation</p>

<p>🏦 Financial Review</p>

</div>

)}


<div className="dashboard-card">

  <h2>Case Notes</h2>

  <textarea
    rows="4"
    cols="50"
    value={note}
    onChange={(e) => setNote(e.target.value)}
    placeholder="Enter investigation note..."
  />

  <br />

  <button onClick={saveNote}>
    Save Note
  </button>

</div>


<div className="dashboard-card">

  <h2>Audit Trail Logs</h2>

  {logs.map((log, index) => (
    <p key={index}>
      {log}
    </p>
  ))}

</div>


<div className="dashboard-card">

  <h2>Natural Language Investigation</h2>

  <input
    type="text"
    value={nlQuery}
    onChange={(e) => setNlQuery(e.target.value)}
    placeholder="Ask investigation question..."
  />

  <button onClick={runNLInvestigation}>
    Investigate
  </button>

  {nlResult && (
    <p>
      <strong>Result:</strong> {nlResult}
    </p>
  )}

</div>


{report && (
  <div className="dashboard-card">

    <h2>Agent Communication Flow</h2>

    <p>CASE CREATED</p>
    <p>↓</p>
    <p>COORDINATOR AGENT</p>
    <p>↓</p>

    {report.agent_flow?.map((agent, index) => (
      <div key={index}>
        <p>{agent}</p>
        <p>↓</p>
      </div>
    ))}

    <p>EXECUTIVE REPORT GENERATED</p>

  </div>
)}


{report && (
  <div className="dashboard-card">

    <h2>MCP Tool Routing</h2>

    <ul>
      {report.mcp_tools?.map((tool, index) => (
        <li key={index}>
          {tool}
        </li>
      ))}
    </ul>

  </div>
)}

{report && (

<div className="dashboard-card">

<h2>Live Investigation Pipeline</h2>

<p>✅ Case Created</p>
<p>⬇</p>

<p>✅ Audit Agent</p>
<p>⬇</p>

<p>✅ Risk Agent</p>
<p>⬇</p>

<p>✅ Compliance Agent</p>
<p>⬇</p>

<p>✅ Fraud Agent</p>
<p>⬇</p>

<p>✅ Executive Report</p>

</div>

)}

{report && (

<div className="dashboard-card">

<h2>Agent Monitoring Panel</h2>

<table>

<thead>
<tr>
<th>Agent</th>
<th>Status</th>
</tr>
</thead>

<tbody>

<tr>
<td>AUDIT_AGENT</td>
<td>🟢 ACTIVE</td>
</tr>

<tr>
<td>RISK_AGENT</td>
<td>🟢 ACTIVE</td>
</tr>

<tr>
<td>COMPLIANCE_AGENT</td>
<td>🟢 ACTIVE</td>
</tr>

<tr>
<td>FRAUD_AGENT</td>
<td>🟢 ACTIVE</td>
</tr>

<tr>
<td>RECOMMENDATION_AGENT</td>
<td>🟢 ACTIVE</td>
</tr>

</tbody>

</table>

</div>

)}

{report && (

<div className="dashboard-card">

<h2>Investigation Timeline</h2>

<ul>

<li>10:01 - Case Created</li>

<li>10:02 - Audit Agent Executed</li>

<li>10:03 - Risk Agent Executed</li>

<li>10:04 - Compliance Agent Executed</li>

<li>10:05 - Fraud Agent Executed</li>

<li>10:06 - Executive Report Generated</li>

</ul>

</div>

)}


{report && (

<div className="dashboard-card">

<h2>Risk Heatmap</h2>

<div className="heatmap">

<div className="risk-low">
LOW
</div>

<div className="risk-medium">
MEDIUM
</div>

<div className="risk-high">
HIGH
</div>

<div className="risk-critical">
CRITICAL
</div>

</div>

</div>

)}

      <div className="history-card">

        <h2>Investigation History</h2>

        <table>
          <thead>
            <tr>
              <th>Case ID</th>
              <th>Amount</th>
              <th>Risk Score</th>
              <th>Decision</th>
            </tr>
          </thead>

          <tbody>

  {history.map((item, index) => (
    <tr key={index}>

      <td>{item.case_id}</td>

      <td>
        ${Math.abs(item.amount)}
      </td>

      <td>{item.risk_score}</td>

      <td>{item.recommendation}</td>

    </tr>
  ))}

</tbody>

        </table>

            </div>
            </>
)}

    </div>

  </div>

  );
}

export default App;