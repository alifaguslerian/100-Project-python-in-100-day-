import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    try:
        data=pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
def clean_data(data):
    print("\nCleaning Data")
    data['Product_Category'] = data['Product_Category'].fillna("Unknown")
    data = data.dropna()

    data['Date'] = pd.to_datetime(data['Date'])
    data['Sales_amount'] = pd.to_numeric(data['Sales_amount'], errors='coerce')

    data['Year_mount'] = data['Date'].dt.to_period('M')
    if 'Quantity' in data.columns and 'price' in data.columns:
        data['Revenue'] = data['Quantity'] * data['price']

    print("Data Clean Succesfully")
    return data

def analyze_data(data):
    print("\n--- Sales insight ---")

    montly_sales = data.groupby("Year_mount")["Sales_amount"].sum()
    print("\nMontly Sales:")
    print(montly_sales)

    if "Revenue" in data.columns:
        top_products = data.groupby("Product_name")["Revenue"].sum().sort_values(ascending=False).head(5)
        print("\nTop 5 Products by Revenue:")
        print(top_products)

    montly_sales.plot(kind="bar", figsize=(10, 6), color="blue")
    plt.title("monthly sales")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.show()

def main():
    print("Welcome to sales report Analyzer!")

    file_path = input("Enter the path to the sales data CSV file: ")
    data = load_data(file_path)
    if data is None:
        return
    data = clean_data(data)

    analyze_data(data)

if __name__ == "__main__":
    main()