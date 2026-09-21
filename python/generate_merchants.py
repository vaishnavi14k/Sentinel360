import csv
import os
import random

from config import (
    NUMBER_OF_MERCHANTS,
    RANDOM_SEED,
    OUTPUT_FOLDER
)


random.seed(RANDOM_SEED)

OUTPUT_PATH = os.path.join(
    OUTPUT_FOLDER,
    "merchants.csv"
)


MERCHANT_CATEGORIES = [
    "Grocery",
    "Electronics",
    "Travel",
    "Food",
    "Entertainment",
    "Healthcare",
    "Retail",
    "Online Services",
    "Financial Services",
    "Jewellery",
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


RISK_LEVELS = [
    "Low",
    "Medium",
    "High",
]


def generate_merchants():

    merchants = []

    for i in range(
        1,
        NUMBER_OF_MERCHANTS + 1
    ):

        merchant_id = f"MER{i:06d}"

        merchant_name = (
            f"Merchant_{i:04d}"
        )

        merchant_category = random.choice(
            MERCHANT_CATEGORIES
        )

        country = random.choice(
            COUNTRIES
        )

        risk_level = random.choices(
            RISK_LEVELS,
            weights=[70, 25, 5],
            k=1
        )[0]

        merchant = {
            "Merchant_ID": merchant_id,
            "Merchant_Name": merchant_name,
            "Merchant_Category": merchant_category,
            "Country": country,
            "Risk_Level": risk_level,
        }

        merchants.append(merchant)

    return merchants


def save_merchants(merchants):

    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

    fieldnames = [
        "Merchant_ID",
        "Merchant_Name",
        "Merchant_Category",
        "Country",
        "Risk_Level",
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

        writer.writerows(merchants)


if __name__ == "__main__":

    print("Generating merchants...")

    merchants = generate_merchants()

    save_merchants(merchants)

    print(
        f"Generated {len(merchants):,} merchants."
    )

    print(
        f"Saved to: {OUTPUT_PATH}"
    )