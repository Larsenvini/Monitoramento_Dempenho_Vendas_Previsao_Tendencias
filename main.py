from trata_dados import clean_data
from loading_data import load_data

def main():
    # Step 1: Clean the data
    print("Cleaning data...")
    clean_data()

    # Step 2: Load the cleaned data into PostgreSQL
    print("Loading data into PostgreSQL...")
    load_data()

if __name__ == "__main__":
    main()
