import csv
import os
import random
from datetime import date, timedelta

from config import NUMBER_OF_CUSTOMERS, RANDOM_SEED, OUTPUT_FOLDER


# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

random.seed(RANDOM_SEED)

OUTPUT_PATH = os.path.join(OUTPUT_FOLDER, "customers.csv")


# ---------------------------------------------------------
# Sample data
# ---------------------------------------------------------

FIRST_NAMES = [
    "Aarav",
    "Vihaan",
    "Aditya",
    "Arjun",
    "Rohan",
    "Karan",
    "Rahul",
    "Ishaan",
    "Kabir",
    "Ananya",
    "Diya",
    "Isha",
    "Meera",
    "Aditi",
    "Sneha",
    "Priya",
    "Nisha",
    "Kavya",
    "Riya",
    "Tanya",
]

LAST_NAMES = [
    "Sharma",
    "Patel",
    "Reddy",
    "Kumar",
    "Singh",
    "Verma",
    "Gupta",
    "Mehta",
    "Iyer",
    "Nair",
    "Rao",
    "Joshi",
    "Shah",
    "Kapoor",
    "Malhotra",
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

OCCUPATIONS = [
    "Software Engineer",
    "Data Analyst",
    "Business Analyst",
    "Teacher",
    "Doctor",
    "Consultant",
    "Accountant",
    "Entrepreneur",
    "Designer",
    "Marketing Manager",
    "Student",
    "Sales Manager",
]

RISK_CATEGORIES = [
    "Low",
    "Medium",
    "High",
]

ACCOUNT_TYPES = [
    "Savings",
    "Current",
]


# ---------------------------------------------------------
# Helper function
# ---------------------------------------------------------

def random_date(start_date, end_date):
    """Generate a random date between two dates."""

    days_between = (end_date - start_date).days

    random_days = random.randint(0, days_between)

    return start_date + timedelta(days=random_days)


# ---------------------------------------------------------
# Generate customers
# ---------------------------------------------------------

def generate_customers():

    start_date = date(2018, 1, 1)
    end_date = date(2025, 1, 1)

    customers = []

    for i in range(1, NUMBER_OF_CUSTOMERS + 1):

        customer_id = f"CUST{i:06d}"

        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)

        customer_name = f"{first_name} {last_name}"

        age = random.randint(21, 70)

        country = random.choice(COUNTRIES)

        customer_since = random_date(
            start_date,
            end_date
        )

        risk_category = random.choices(
            RISK_CATEGORIES,
            weights=[70, 25, 5],
            k=1
        )[0]

        occupation = random.choice(OCCUPATIONS)

        account_type = random.choice(ACCOUNT_TYPES)

        customer = {
            "Customer_ID": customer_id,
            "Customer_Name": customer_name,
            "Age": age,
            "Country": country,
            "Customer_Since": customer_since.isoformat(),
            "Risk_Category": risk_category,
            "Occupation": occupation,
            "Account_Type": account_type,
        }

        customers.append(customer)

    return customers


# ---------------------------------------------------------
# Save customers
# ---------------------------------------------------------

def save_customers(customers):

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    fieldnames = [
        "Customer_ID",
        "Customer_Name",
        "Age",
        "Country",
        "Customer_Since",
        "Risk_Category",
        "Occupation",
        "Account_Type",
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

        writer.writerows(customers)


# ---------------------------------------------------------
# Main program
# ---------------------------------------------------------

if __name__ == "__main__":

    print("Generating customers...")

    customers = generate_customers()

    save_customers(customers)

    print(
        f"Generated {len(customers):,} customers."
    )

    print(
        f"Saved to: {OUTPUT_PATH}"
    )