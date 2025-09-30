# Inventory Management

class Inventory:
    total_items = 0

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        Inventory.total_items += quantity

    # instance method
    def show_product_details(self):
        print("\n--- Product Details ---")
        print(f"Product Name: {self.product_name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")

    # Sell product
    def sell_product(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            Inventory.total_items -= amount
            print(f"Sold {amount} {self.product_name}(s)")
        else:
            print("Insufficient quantity")

    # Calculate discount
    @staticmethod
    def calculate_discount(price, discount_percentage):
        return price * (1 - discount_percentage / 100)
    
    # Total items
    @classmethod
    def total_items_report(cls):
        print(f"Total items: {cls.total_items}")


# Daftar produk untuk menyimpan produk yang ada
products = []

# Menambahkan produk baru
def add_product():
    product_name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product = Inventory(product_name, price, quantity)
    products.append(product)  # Menambahkan produk ke dalam daftar

    print("Product added successfully!")

# Menampilkan semua produk
def view_products():
    print("\n--- All Products ---")
    if not products:
        print("No products found.")
    else:
        for product in products:
            product.show_product_details()

# Menjual produk
def sell_product():
    product_name = input("Enter product name: ")

    for product in products:
        if product.product_name == product_name:
            amount = int(input("Enter quantity to sell: "))
            product.sell_product(amount)
            break
    else:
        print("Product not found.")

# Menghitung harga setelah diskon
def discount_price():
    price = float(input("Enter price: "))
    discount_percentage = float(input("Enter discount percentage: "))

    discounted_price = Inventory.calculate_discount(price, discount_percentage)
    print(f"Discounted price: {discounted_price}")


# Main Menu
while True:
    print("\n--- Inventory Management ---")
    print("1. Add Product")
    print("2. View Products")
    print("3. Sell Product")
    print("4. Calculate Discount")
    print("5. Total Items Report")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        sell_product()
    elif choice == "4":
        discount_price()
    elif choice == "5":
        Inventory.total_items_report()  # Mengakses metode kelas dengan benar
    elif choice == "6":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-6).")
