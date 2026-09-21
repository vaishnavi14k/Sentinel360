import csv
import os
import random
from datetime import date, timedelta

from config import (
    NUMBER_OF_ACCOUNTS,
    RANDOM_SEED,
    OUTPUT_FOLDER
)


random.seed(RANDOM_SEED)

CUSTOMERS_PATH = os.path.join(
    OUTPUT_FOLDER,
    "customers.csv"
)

OUTPUT_PATH = os.path.join(
    OUTPUT_FOLDER,
    "accounts.csv"
)


ACCOUNT_TYPES = [
    "Savings",
    "Current",
]


ACCOUNT_STATUSES = [
    "Active",
    "Active",
    "Active",
    "Active",
    "Closed",
    "Frozen",
]


def random_date(start_date, end_date):

    days_between = (end_date - start_date).days

    random_days = random.randint(
        0,
        days_between
    )

    return start_date + timedelta(
        days=random_days
    )


def load_customer_ids():

    customer_ids = []

    with open(
        CUSTOMERS_PATH,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:
            customer_ids.append(
                row["Customer_ID"]
            )

    return customer_ids


def generate_accounts(customer_ids):

    accounts = []

    start_date = date(2019, 1, 1)
    end_date = date(2026, 8, 31)

    for i in range(
        1,
        NUMBER_OF_ACCOUNTS + 1
    ):

        account_id = f"ACC{i:06d}"

        customer_id = random.choice(
            customer_ids
        )

        account_type = random.choice(
            ACCOUNT_TYPES
        )

        account_open_date = random_date(
            start_date,
            end_date
        )

        account_status = random.choice(
            ACCOUNT_STATUSES
        )

        account = {
            "Account_ID": account_id,
            "Customer_ID": customer_id,
            "Account_Type": account_type,
            "Account_Open_Date": account_open_date.isoformat(),
            "Account_Status": account_status,
        }

        accounts.append(account)

    return accounts


def save_accounts(accounts):

    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

    fieldnames = [
        "Account_ID",
        "Customer_ID",
        "Account_Type",
        "Account_Open_Date",
        "Account_Status",
    ]

    with open(
        OUTPUT_PATH,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(accounts)


if __name__ == "__main__":

    print("Loading customers...")

    customer_ids = load_customer_ids()

    print(
        f"Loaded {len(customer_ids):,} customers."
    )

    print("Generating accounts...")

    accounts = generate_accounts(
        customer_ids
    )

    save_accounts(accounts)

    print(
        f"Generated {len(accounts):,} accounts."
    )

    print(
        f"Saved to: {OUTPUT_PATH}"
    )