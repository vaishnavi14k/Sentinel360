import csv
import os
from datetime import date, timedelta

from config import (
    START_DATE,
    END_DATE,
    OUTPUT_FOLDER
)


OUTPUT_PATH = os.path.join(
    OUTPUT_FOLDER,
    "date.csv"
)


def generate_dates():

    start_date = date.fromisoformat(
        START_DATE
    )

    end_date = date.fromisoformat(
        END_DATE
    )

    dates = []

    current_date = start_date

    while current_date <= end_date:

        dates.append({
            "Date": current_date.isoformat(),
            "Year": current_date.year,
            "Month": current_date.strftime("%B"),
            "Month_Number": current_date.month,
            "Quarter": f"Q{((current_date.month - 1) // 3) + 1}",
            "Day": current_date.day,
            "Day_Name": current_date.strftime("%A"),
            "Week_Number": current_date.isocalendar().week,
        })

        current_date += timedelta(days=1)

    return dates


def save_dates(dates):

    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

    fieldnames = [
        "Date",
        "Year",
        "Month",
        "Month_Number",
        "Quarter",
        "Day",
        "Day_Name",
        "Week_Number",
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

        writer.writerows(dates)


if __name__ == "__main__":

    print("Generating date table...")

    dates = generate_dates()

    save_dates(dates)

    print(
        f"Generated {len(dates):,} dates."
    )

    print(
        f"Saved to: {OUTPUT_PATH}"
    )