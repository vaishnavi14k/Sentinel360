# Sentinel360 Data Flow

## Overall Flow

Synthetic Data
↓
Python Data Generation
↓
Raw CSV Files
↓
PostgreSQL
↓
Data Quality Checks
↓
Data Validation
↓
Transaction Reconciliation
↓
Risk & Anomaly Detection
↓
Investigation Cases
↓
Power BI
↓
Power Automate
↓
Power Apps
↓
AI Investigation Assistant

---

## Data Sources

### Source A

Primary transaction source.

### Source B

Secondary transaction source used for reconciliation.

---

## Processing

Python generates synthetic financial data.

SQL and Python are used for validation and processing.

Power Query is used for data transformation before Power BI analysis.

---

## Analytics

Power BI analyzes:

- Transaction volume
- Transaction value
- Data quality
- Reconciliation
- Risk indicators
- Anomalies
- Investigation cases

---

## Workflow Automation

Power Automate is used for:

- Case notifications
- Analyst assignment
- Escalations
- Data quality alerts
- Case status updates

---

## Case Management

Power Apps provides an interface for analysts to:

- View cases
- Start investigations
- Add notes
- Escalate cases
- Resolve cases

---

## AI

The AI component generates an explanation of why a case was
flagged using the available case information.