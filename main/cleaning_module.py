from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = DATA_DIR / "processed"


def load_data():
    books = pd.read_csv(DATA_DIR / "library.csv")
    customers = pd.read_csv(DATA_DIR / "library_customers.csv")

    return books, customers


def clean_data(data):
    # Remove completely empty rows
    data = data.dropna(how="all")

    # Remove duplicate rows
    data = data.drop_duplicates()

    # Clean column names
    data.columns = data.columns.str.strip()

    # Remove whitespace from text values
    for column in data.select_dtypes(include="object").columns:
        data[column] = data[column].str.strip()

    return data


def clean_books(books):
    books = clean_data(books)

    if "Book checkout" in books.columns:
        books["Book checkout"] = pd.to_datetime(
            books["Book checkout"],
            errors="coerce",
            dayfirst=True
        )

    return books


def save_data(books, customers):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    books.to_csv(
        OUTPUT_DIR / "library_clean.csv",
        index=False
    )

    customers.to_csv(
        OUTPUT_DIR / "library_customers_clean.csv",
        index=False
    )