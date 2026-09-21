# Sentinel360 Database Schema

## Dimension Tables

### customers

Primary Key:

Customer_ID

### accounts

Primary Key:

Account_ID

Foreign Key:

Customer_ID → customers.Customer_ID

### merchants

Primary Key:

Merchant_ID

### devices

Primary Key:

Device_ID

### date

Primary Key:

Date

---

# Fact Table

### transactions

Primary Key:

Transaction_ID

Foreign Keys:

Customer_ID → customers.Customer_ID

Account_ID → accounts.Account_ID

Merchant_ID → merchants.Merchant_ID

Device_ID → devices.Device_ID

Date → date.Date

---

# Supporting Tables

### transactions_source_b

Used for transaction reconciliation.

### data_quality_results

Stores results of data quality checks.

### reconciliation_results

Stores transaction reconciliation results.

### investigation_cases

Stores investigation cases created from anomalous activity.