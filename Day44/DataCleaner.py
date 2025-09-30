import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
def clean_data(df):
    print("\n---- Cleaning Data ----")
    print("Initial Data:", df.shape)

    print("\nHandling Missing Values")
    choice = input("Choose method to handle missing values (drop/fill): ").strip().lower()
    
    if choice == 'fill':
        fill_value = input("Enter value to fill missing data (e.g., 0, 'unknown'): ")
        df = df.fillna(fill_value)
        print("After Filling Missing Values:", df.shape)
    elif choice == 'drop':
        df = df.dropna()
        print("After Dropping Missing Values:", df.shape)
    else:
        print("Invalid choice. No changes made to missing values.")
        print("Shape after invalid choice (unchanged):", df.shape)

    print("\nRemoving Duplicates")
    df = df.drop_duplicates()
    print("After Removing Duplicates:", df.shape)

    return df

def save_data(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        print(f"Data saved to {output_path}")
    except Exception as e:
        print(f"Error saving data: {e}")

def main():
    print("---- Data Cleaning Script ----")

    input_file = input("Enter the path to the CSV file: ")
    df = load_data(input_file)
    if df is None:
        return
    
    print("\n---- Initial Data Preview ----")
    print(df.head())

    df = clean_data(df)

    output_file = input("Enter the path to save the cleaned CSV file: ")
    save_data(df, output_file)

if __name__ == "__main__":
    main()
        