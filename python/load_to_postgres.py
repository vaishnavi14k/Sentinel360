import csv
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


# ============================================================
# Sentinel360 - PostgreSQL Data Loader
# ============================================================


# ------------------------------------------------------------
# Database configuration
# ------------------------------------------------------------

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# IMPORTANT:
# Replace this with the PostgreSQL password you created
# when installing PostgreSQL.
DB_PASSWORD = "Vaishu123$"


# ------------------------------------------------------------
# Data folder
# ------------------------------------------------------------

DATA_FOLDER = "data/raw"


# ------------------------------------------------------------
# Connect to PostgreSQL
# ------------------------------------------------------------

print("Connecting to PostgreSQL...")

connection = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

cursor = connection.cursor()

print("Connected successfully.")


# ============================================================
# Helper function
# ============================================================

def load_csv_to_table(
    filename,
    table_name,
    columns
):

    file_path = os.path.join(
        DATA_FOLDER,
        filename
    )

    print()
    print(f"Loading {filename}...")
    
    with open(
        file_path,
        "r",
        encoding="utf-8",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        rows = []

        for row in reader:

            values = []

            for column in columns:

                value = row[column]

                if value == "":
                    value = None

                values.append(value)

            rows.append(tuple(values))


    placeholders = ", ".join(
        ["%s"] * len(columns)
    )

    column_names = ", ".join(
        columns
    )

    insert_query = f"""
        INSERT INTO {table_name}
        ({column_names})
        VALUES ({placeholders})
    """

    cursor.executemany(
        insert_query,
        rows
    )

    connection.commit()

    print(
        f"Loaded {len(rows):,} rows into {table_name}."
    )


# ============================================================
# Load customers
# ============================================================

load_csv_to_table(
    "customers.csv",
    "customers",
    [
        "Customer_ID",
        "Customer_Name",
        "Age",
        "Country",
        "Customer_Since",
        "Risk_Category",
        "Occupation",
        "Account_Type"
    ]
)


# ============================================================
# Load accounts
# ============================================================

load_csv_to_table(
    "accounts.csv",
    "accounts",
    [
        "Account_ID",
        "Customer_ID",
        "Account_Type",
        "Account_Open_Date",
        "Account_Status"
    ]
)


# ============================================================
# Load merchants
# ============================================================

load_csv_to_table(
    "merchants.csv",
    "merchants",
    [
        "Merchant_ID",
        "Merchant_Name",
        "Merchant_Category",
        "Country",
        "Risk_Level"
    ]
)


# ============================================================
# Load devices
# ============================================================

load_csv_to_table(
    "devices.csv",
    "devices",
    [
        "Device_ID",
        "Device_Type",
        "Operating_System",
        "Country"
    ]
)


# ============================================================
# Load date dimension
# ============================================================

load_csv_to_table(
    "date.csv",
    "date",
    [
        "Date",
        "Year",
        "Month",
        "Month_Number",
        "Quarter",
        "Day",
        "Day_Name",
        "Week_Number"
    ]
)


# ============================================================
# Load transactions
# ============================================================

load_csv_to_table(
    "transactions.csv",
    "transactions",
    [
        "Transaction_ID",
        "Customer_ID",
        "Account_ID",
        "Transaction_DateTime",
        "Amount",
        "Currency",
        "Transaction_Type",
        "Payment_Channel",
        "Merchant_ID",
        "Country",
        "Transaction_Status",
        "Device_ID"
    ]
)


# ============================================================
# Close connection
# ============================================================

cursor.close()
connection.close()

print()
print("=" * 60)
print("DATA LOADING COMPLETE")
print("=" * 60)