import csv
import os
import random
from datetime import datetime, timedelta

from config import (
    NUMBER_OF_TRANSACTIONS,
    RANDOM_SEED,
    OUTPUT_FOLDER,
    START_DATE,
    END_DATE,
)


random.seed(RANDOM_SEED)


CUSTOMERS_PATH = os.path.join(
    OUTPUT_FOLDER,
    "customers.csv"
)

ACCOUNTS_PATH = os.path.join(
    OUTPUT_FOLDER,
    "accounts.csv"
)

MERCHANTS_PATH = os.path.join(
    OUTPUT_FOLDER,
    "merchants.csv"
)

DEVICES_PATH = os.path.join(
    OUTPUT_FOLDER,
    "devices.csv"
)

OUTPUT_PATH = os.path.join(
    OUTPUT_FOLDER,
    "transactions.csv"
)


TRANSACTION_TYPES = [
    "Purchase",
    "Transfer",
    "Withdrawal",
    "Deposit",
    "Payment",
]


PAYMENT_CHANNELS = [
    "Online",
    "Mobile App",
    "ATM",
    "POS",
    "Bank Transfer",
]


CURRENCIES = [
    "INR",
    "USD",
    "EUR",
    "GBP",
]


COUNTRIES = [
    "India",
    "United States",
    "United Kingdom",
    "Germany",
    "Singapore",
    "United Arab Emirates",
    "Canada",
    "Australia",
]


TRANSACTION_STATUSES = [
    "Success",
    "Success",
    "Success",
    "Success",
    "Success",
    "Failed",
    "Pending",
]


def load_csv(path):

    with open(
        path,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        return list(
            csv.DictReader(file)
        )


def generate_random_datetime():

    start = datetime.fromisoformat(
        START_DATE + " 00:00:00"
    )

    end = datetime.fromisoformat(
        END_DATE + " 23:59:59"
    )

    seconds_between = int(
        (end - start).total_seconds()
    )

    random_seconds = random.randint(
        0,
        seconds_between
    )

    return start + timedelta(
        seconds=random_seconds
    )


def generate_transactions(
    customers,
    accounts,
    merchants,
    devices
):

    transactions = []

    customer_to_accounts = {}

    for account in accounts:

        customer_id = account["Customer_ID"]

        if customer_id not in customer_to_accounts:

            customer_to_accounts[customer_id] = []

        customer_to_accounts[customer_id].append(
            account["Account_ID"]
        )


    for i in range(
        1,
        NUMBER_OF_TRANSACTIONS + 1
    ):

        customer = random.choice(
            customers
        )

        customer_id = customer["Customer_ID"]

        available_accounts = customer_to_accounts.get(
            customer_id,
            []
        )

        if available_accounts:

            account_id = random.choice(
                available_accounts
            )

        else:

            account_id = random.choice(
                accounts
            )["Account_ID"]


        merchant = random.choice(
            merchants
        )

        device = random.choice(
            devices
        )


        transaction_id = f"TXN{i:08d}"


        transaction_datetime = (
            generate_random_datetime()
        )


        transaction_type = random.choice(
            TRANSACTION_TYPES
        )


        payment_channel = random.choice(
            PAYMENT_CHANNELS
        )


        currency = random.choice(
            CURRENCIES
        )


        country = random.choice(
            COUNTRIES
        )


        transaction_status = random.choice(
            TRANSACTION_STATUSES
        )


        amount = round(
            random.uniform(
                100,
                250000
            ),
            2
        )


        transaction = {
            "Transaction_ID": transaction_id,
            "Customer_ID": customer_id,
            "Account_ID": account_id,
            "Transaction_DateTime": transaction_datetime.isoformat(
                sep=" "
            ),
            "Amount": amount,
            "Currency": currency,
            "Transaction_Type": transaction_type,
            "Payment_Channel": payment_channel,
            "Merchant_ID": merchant["Merchant_ID"],
            "Country": country,
            "Transaction_Status": transaction_status,
            "Device_ID": device["Device_ID"],
        }


        transactions.append(
            transaction
        )


        if i % 100_000 == 0:

            print(
                f"Generated {i:,} transactions..."
            )


    return transactions


def save_transactions(transactions):

    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

    fieldnames = [
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
        "Device_ID",
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

        writer.writerows(
            transactions
        )


if __name__ == "__main__":

    print("Loading source data...")


    customers = load_csv(
        CUSTOMERS_PATH
    )

    accounts = load_csv(
        ACCOUNTS_PATH
    )

    merchants = load_csv(
        MERCHANTS_PATH
    )

    devices = load_csv(
        DEVICES_PATH
    )


    print(
        f"Customers loaded: {len(customers):,}"
    )

    print(
        f"Accounts loaded: {len(accounts):,}"
    )

    print(
        f"Merchants loaded: {len(merchants):,}"
    )

    print(
        f"Devices loaded: {len(devices):,}"
    )


    print(
        "Generating transactions..."
    )


    transactions = generate_transactions(
        customers,
        accounts,
        merchants,
        devices
    )


    print(
        "Saving transactions..."
    )


    save_transactions(
        transactions
    )


    print(
        f"Generated {len(transactions):,} transactions."
    )

    print(
        f"Saved to: {OUTPUT_PATH}"
    )