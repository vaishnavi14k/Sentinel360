-- ============================================================
-- Sentinel360 Database Schema
-- ============================================================

-- Customers
CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    customer_name VARCHAR(100),
    age INTEGER,
    country VARCHAR(50),
    customer_since DATE,
    risk_category VARCHAR(20),
    occupation VARCHAR(100),
    account_type VARCHAR(50)
);

-- Accounts
CREATE TABLE IF NOT EXISTS accounts (
    account_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20) NOT NULL,
    account_type VARCHAR(50),
    account_open_date DATE,
    account_status VARCHAR(30),

    CONSTRAINT fk_accounts_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);


-- Merchants
CREATE TABLE IF NOT EXISTS merchants (
    merchant_id VARCHAR(20) PRIMARY KEY,
    merchant_name VARCHAR(100),
    merchant_category VARCHAR(100),
    country VARCHAR(50),
    risk_level VARCHAR(20)
);


-- Devices
CREATE TABLE IF NOT EXISTS devices (
    device_id VARCHAR(20) PRIMARY KEY,
    device_type VARCHAR(50),
    operating_system VARCHAR(50),
    country VARCHAR(50)
);


-- Date dimension
CREATE TABLE IF NOT EXISTS date (
    date DATE PRIMARY KEY,
    year INTEGER,
    month VARCHAR(20),
    month_number INTEGER,
    quarter VARCHAR(10),
    day INTEGER,
    day_name VARCHAR(20),
    week_number INTEGER
);


-- Transactions
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20),
    account_id VARCHAR(20),
    transaction_datetime TIMESTAMP,
    amount NUMERIC(15,2),
    currency VARCHAR(10),
    transaction_type VARCHAR(30),
    payment_channel VARCHAR(30),
    merchant_id VARCHAR(20),
    country VARCHAR(50),
    transaction_status VARCHAR(30),
    device_id VARCHAR(20),

    CONSTRAINT fk_transactions_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    CONSTRAINT fk_transactions_account
        FOREIGN KEY (account_id)
        REFERENCES accounts(account_id),

    CONSTRAINT fk_transactions_merchant
        FOREIGN KEY (merchant_id)
        REFERENCES merchants(merchant_id),

    CONSTRAINT fk_transactions_device
        FOREIGN KEY (device_id)
        REFERENCES devices(device_id)
);


-- ============================================================
-- Indexes
-- ============================================================

CREATE INDEX IF NOT EXISTS idx_accounts_customer
ON accounts(customer_id);

CREATE INDEX IF NOT EXISTS idx_transactions_customer
ON transactions(customer_id);

CREATE INDEX IF NOT EXISTS idx_transactions_account
ON transactions(account_id);

CREATE INDEX IF NOT EXISTS idx_transactions_merchant
ON transactions(merchant_id);

CREATE INDEX IF NOT EXISTS idx_transactions_device
ON transactions(device_id);

CREATE INDEX IF NOT EXISTS idx_transactions_datetime
ON transactions(transaction_datetime);

CREATE INDEX IF NOT EXISTS idx_transactions_status
ON transactions(transaction_status);


