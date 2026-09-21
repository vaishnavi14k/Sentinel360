import csv
import os
import random

from config import (
    NUMBER_OF_DEVICES,
    RANDOM_SEED,
    OUTPUT_FOLDER
)


random.seed(RANDOM_SEED)

OUTPUT_PATH = os.path.join(
    OUTPUT_FOLDER,
    "devices.csv"
)


DEVICE_TYPES = [
    "Mobile",
    "Laptop",
    "Tablet",
]


OPERATING_SYSTEMS = {
    "Mobile": [
        "Android",
        "iOS"
    ],
    "Laptop": [
        "Windows",
        "macOS",
        "Linux"
    ],
    "Tablet": [
        "Android",
        "iPadOS"
    ]
}


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


def generate_devices():

    devices = []

    for i in range(
        1,
        NUMBER_OF_DEVICES + 1
    ):

        device_id = f"DEV{i:06d}"

        device_type = random.choice(
            DEVICE_TYPES
        )

        operating_system = random.choice(
            OPERATING_SYSTEMS[device_type]
        )

        country = random.choice(
            COUNTRIES
        )

        device = {
            "Device_ID": device_id,
            "Device_Type": device_type,
            "Operating_System": operating_system,
            "Country": country,
        }

        devices.append(device)

    return devices


def save_devices(devices):

    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )

    fieldnames = [
        "Device_ID",
        "Device_Type",
        "Operating_System",
        "Country",
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

        writer.writerows(devices)


if __name__ == "__main__":

    print("Generating devices...")

    devices = generate_devices()

    save_devices(devices)

    print(
        f"Generated {len(devices):,} devices."
    )

    print(
        f"Saved to: {OUTPUT_PATH}"
    )