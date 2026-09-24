from cleaning_module import load_data, clean_books, clean_data, save_data


def main():
    print("Starting library data cleaning...")

    books, customers = load_data()

    books = clean_books(books)
    customers = clean_data(customers)

    save_data(books, customers)

    print("Data cleaning completed successfully.")


if __name__ == "__main__":
    main()