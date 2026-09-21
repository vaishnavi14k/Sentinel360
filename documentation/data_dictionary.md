# Sentinel360 Data Dictionary

## Project Overview

Sentinel360 is an educational Financial Compliance Intelligence
and Investigation Platform built using synthetic financial data.

The system analyzes financial transactions for:

- Data quality issues
- Reconciliation problems
- Transaction anomalies
- Risk indicators
- Investigation cases

All financial data used in this project is synthetic.

---

# 1. Customers

The customers table contains information about customers of the
fictional financial institution.

| Column | Description | Example |
|---|---|---|
| Customer_ID | Unique identifier for a customer | CUST000001 |
| Customer_Name | Customer's name | Ananya Sharma |
| Age | Customer age | 29 |
| Country | Customer's country | India |
| Customer_Since | Date customer joined | 2021-05-12 |
| Risk_Category | Customer risk category | Medium |
| Occupation | Customer occupation | Software Engineer |
| Account_Type | Primary account type | Savings |

---

# 2. Accounts

The accounts table contains accounts belonging to customers.

| Column | Description | Example |
|---|---|---|
| Account_ID | Unique account identifier | ACC000001 |
| Customer_ID | Customer who owns the account | CUST000001 |
| Account_Type | Type of account | Savings |
| Account_Open_Date | Date account was opened | 2022-03-15 |
| Account_Status | Current account status | Active |

Relationship:

One customer can have multiple accounts.

---

# 3. Transactions

The transactions table contains financial transaction events.

Grain:

One row represents one financial transaction.

| Column | Description | Example |
|---|---|---|
| Transaction_ID | Unique transaction identifier | TXN00000001 |
| Customer_ID | Customer performing transaction | CUST000001 |
| Account_ID | Account used | ACC000001 |
| Transaction_DateTime | Date and time of transaction | 2026-02-14 22:32:15 |
| Amount | Transaction amount | 85000 |
| Currency | Transaction currency | INR |
| Transaction_Type | Type of transaction | Transfer |
| Payment_Channel | Channel used | Online |
| Merchant_ID | Merchant involved | MER000123 |
| Country | Transaction country | India |
| Transaction_Status | Transaction status | Success |
| Device_ID | Device used | DEV000321 |

---

# 4. Merchants

The merchants table contains information about merchants involved
in transactions.

| Column | Description | Example |
|---|---|---|
| Merchant_ID | Unique merchant identifier | MER000001 |
| Merchant_Name | Merchant name | Merchant_001 |
| Merchant_Category | Business category | Electronics |
| Country | Merchant country | India |
| Risk_Level | Merchant risk level | Medium |

---

# 5. Devices

The devices table contains information about devices used for
transactions.

| Column | Description | Example |
|---|---|---|
| Device_ID | Unique device identifier | DEV000001 |
| Device_Type | Type of device | Mobile |
| Operating_System | Device operating system | Android |
| Country | Device country | India |

---

# 6. Date

The date table provides calendar information for analysis.

| Column | Description | Example |
|---|---|---|
| Date | Calendar date | 2026-01-01 |
| Year | Year | 2026 |
| Month | Month name | January |
| Month_Number | Numeric month | 1 |
| Quarter | Quarter | Q1 |
| Day | Day of month | 1 |
| Day_Name | Day name | Thursday |
| Week_Number | Week number | 1 |

---

# 7. Transactions Source B

A second transaction source is used to simulate a separate
financial system.

It is used for transaction reconciliation.

The source contains transaction information that can be compared
against the primary transaction source.

---

# 8. Data Quality Results

This table stores the results of data quality checks.

| Column | Description |
|---|---|
| Check_ID | Unique quality check identifier |
| Check_Name | Name of quality check |
| Table_Name | Table being checked |
| Column_Name | Column being checked |
| Total_Records | Total records checked |
| Failed_Records | Number of failed records |
| Failure_Rate | Percentage of failed records |
| Check_Status | PASS or FAIL |
| Run_Date | Date check was performed |

---

# 9. Reconciliation Results

This table stores comparison results between transaction sources.

| Column | Description |
|---|---|
| Transaction_ID | Transaction being compared |
| Source_A_Amount | Amount in Source A |
| Source_B_Amount | Amount in Source B |
| Amount_Difference | Difference between amounts |
| Source_A_Status | Source A transaction status |
| Source_B_Status | Source B transaction status |
| Reconciliation_Status | Result of reconciliation |

Possible reconciliation statuses:

- MATCHED
- MISSING_IN_SOURCE_A
- MISSING_IN_SOURCE_B
- AMOUNT_MISMATCH
- DUPLICATE

---

# 10. Investigation Cases

This table contains cases created from suspicious or anomalous
activity.

| Column | Description |
|---|---|
| Case_ID | Unique investigation case |
| Customer_ID | Customer associated with case |
| Risk_Score | Illustrative risk score |
| Priority | Case priority |
| Reason | Reason case was created |
| Assigned_Analyst | Analyst assigned to case |
| Status | Current case status |
| Created_Date | Date case was created |
| Resolution_Date | Date case was resolved |
| Notes | Investigation notes |

---

# Relationships

The main relationships are:

Customers → Accounts

Customers → Transactions

Accounts → Transactions

Merchants → Transactions

Devices → Transactions

Date → Transactions

Transactions → Investigation Cases