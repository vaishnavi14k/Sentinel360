import csv
import os
import random
from copy import deepcopy


# ============================================================
# Sentinel360 - Data Quality Issue Injection
# ============================================================

INPUT_FILE = "data/raw/transactions.csv"
CUSTOMERS_FILE = "data/raw/customers.csv"
ACCOUNTS_FILE = "data/raw/accounts.csv"

OUTPUT_FOLDER = "data/processed"
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "transactions_dirty.csv")

RANDOM_SEED = 42

random.seed(RANDOM_SEED)


# ============================================================
# Create output folder
# ============================================================

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# ============================================================
# Load transactions
# ============================================================

print("Loading transactions...")

with open(INPUT_FILE, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    transactions = list(reader)

print(f"Loaded {len(transactions):,} transactions.")


# ============================================================
# Load valid customer IDs
# ============================================================

print("Loading customer IDs...")

with open(CUSTOMERS_FILE, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    customer_ids = {row["Customer_ID"] for row in reader}

print(f"Loaded {len(customer_ids):,} valid customer IDs.")


# ============================================================
# Load valid account IDs
# ============================================================

print("Loading account IDs...")

with open(ACCOUNTS_FILE, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    account_ids = {row["Account_ID"] for row in reader}

print(f"Loaded {len(account_ids):,} valid account IDs.")


# ============================================================
# Make a copy of original transactions
# ============================================================

dirty_transactions = deepcopy(transactions)


# ============================================================
# Track injected issues
# ============================================================

issue_counts = {
    "missing_customer_id": 0,
    "duplicate_transactions": 0,
    "invalid_currency": 0,
    "negative_amount": 0,
    "missing_country": 0,
    "inconsistent_country": 0,
    "invalid_customer_id": 0,
    "invalid_account_id": 0,
    "high_amount_anomaly": 0
}


# ============================================================
# 1. Missing Customer_ID
# Approximately 2% of transactions
# ============================================================

print("Injecting missing Customer_ID values...")

number_of_issues = int(len(dirty_transactions) * 0.02)

selected_rows = random.sample(
    range(len(dirty_transactions)),
    number_of_issues
)

for index in selected_rows:
    dirty_transactions[index]["Customer_ID"] = ""
    issue_counts["missing_customer_id"] += 1


# ============================================================
# 2. Invalid currencies
# Approximately 0.5%
# ============================================================

print("Injecting invalid currencies...")

number_of_issues = int(len(dirty_transactions) * 0.005)

selected_rows = random.sample(
    range(len(dirty_transactions)),
    number_of_issues
)

invalid_currencies = ["XYZ", "ABC", "XXX", "INVALID"]

for index in selected_rows:
    dirty_transactions[index]["Currency"] = random.choice(
        invalid_currencies
    )

    issue_counts["invalid_currency"] += 1


# ============================================================
# 3. Negative transaction amounts
# Approximately 0.3%
# ============================================================

print("Injecting negative transaction amounts...")

number_of_issues = int(len(dirty_transactions) * 0.003)

selected_rows = random.sample(
    range(len(dirty_transactions)),
    number_of_issues
)

for index in selected_rows:

    original_amount = float(
        dirty_transactions[index]["Amount"]
    )

    dirty_transactions[index]["Amount"] = str(
        round(-abs(original_amount), 2)
    )

    issue_counts["negative_amount"] += 1


# ============================================================
# 4. Missing country
# Approximately 0.5%
# ============================================================

print("Injecting missing country values...")

number_of_issues = int(len(dirty_transactions) * 0.005)

selected_rows = random.sample(
    range(len(dirty_transactions)),
    number_of_issues
)

for index in selected_rows:

    dirty_transactions[index]["Country"] = ""

    issue_counts["missing_country"] += 1


# ============================================================
# 5. Inconsistent country names
# Approximately 0.5%
# ============================================================

print("Injecting inconsistent country values...")

number_of_issues = int(len(dirty_transactions) * 0.005)

selected_rows = random.sample(
    range(len(dirty_transactions)),
    number_of_issues
)

country_variations = [
    "india",
    "INDIA",
    "IN",
    "India ",
    " india"
]

for index in selected_rows:

    dirty_transactions[index]["Country"] = random.choice(
        country_variations
    )

    issue_counts["inconsistent_country"] += 1


# ============================================================
# 6. Invalid Customer_ID
# Approximately 0.2%
# ============================================================

print("Injecting invalid Customer_ID references...")

number_of_issues = int(len(dirty_transactions) * 0.002)

selected_rows = random.sample(
    range(len(dirty_transactions)),
    number_of_issues
)

for index in selected_rows:

    dirty_transactions[index]["Customer_ID"] = (
        "CUST999999"
    )

    issue_counts["invalid_customer_id"] += 1


# ============================================================
# 7. Invalid Account_ID
# Approximately 0.2%
# ============================================================

print("Injecting invalid Account_ID references...")

number_of_issues = int(len(dirty_transactions) * 0.002)

selected_rows = random.sample(
    range(len(dirty_transactions)),
    number_of_issues
)

for index in selected_rows:

    dirty_transactions[index]["Account_ID"] = (
        "ACC999999"
    )

    issue_counts["invalid_account_id"] += 1


# ============================================================
# 8. Extremely large transaction amounts
# Approximately 0.2%
# ============================================================

print("Injecting unusually large transaction amounts...")

number_of_issues = int(len(dirty_transactions) * 0.002)

selected_rows = random.sample(
    range(len(dirty_transactions)),
    number_of_issues
)

for index in selected_rows:

    dirty_transactions[index]["Amount"] = str(
        random.randint(10000000, 50000000)
    )

    issue_counts["high_amount_anomaly"] += 1


# ============================================================
# 9. Duplicate transactions
# Approximately 1%
# ============================================================

print("Creating duplicate transactions...")

number_of_duplicates = int(len(dirty_transactions) * 0.01)

duplicate_rows = random.sample(
    dirty_transactions,
    number_of_duplicates
)

for row in duplicate_rows:

    duplicated_row = row.copy()

    dirty_transactions.append(
        duplicated_row
    )

    issue_counts["duplicate_transactions"] += 1


# ============================================================
# Shuffle final dataset
# ============================================================

print("Shuffling final dataset...")

random.shuffle(dirty_transactions)


# ============================================================
# Save dirty dataset
# ============================================================

print("Saving dirty dataset...")

fieldnames = list(dirty_transactions[0].keys())

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8",
    newline=""
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(
        dirty_transactions
    )


# ============================================================
# Final report
# ============================================================

print()
print("=" * 60)
print("DATA QUALITY ISSUE INJECTION COMPLETE")
print("=" * 60)

print()

for issue, count in issue_counts.items():

    print(
        f"{issue:<30}: {count:,}"
    )

print()

print(
    f"Original transactions       : {len(transactions):,}"
)

print(
    f"Final transactions           : {len(dirty_transactions):,}"
)

print()

print(
    f"Saved to: {OUTPUT_FILE}"
)

print()