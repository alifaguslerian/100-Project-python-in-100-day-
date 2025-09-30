# Bank Acoount Simulator 

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

# Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

# Withdraw method
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

# Show account details
    def show_details(self):
        print("\n--- Account Details ---")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")

# Main program
accounts = {}

def create_account():
    name = input("Enter your name: ").strip()
    initial_deposit = float(input("Enter the initial deposit amount: "))
    account = BankAccount(name, initial_deposit)
    accounts[name] = account
    print("\nAccount created successfully!")

def access_account():
    name = input("Enter your name: ").strip()
    if name in accounts:
        account = accounts[name]
        while True:
            print("\n--- Account Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Details")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                amount = float(input("Enter the deposit amount: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter the withdrawal amount: "))
                account.withdraw(amount)
            elif choice == "3":
                account.show_details()
            elif choice == "4":
                print("Exiting the account menu. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option (1-4).")
    else:
        print("Account not found. Please create an account first.")

# Main menu
while True:
    print("\n--- Bank Account Simulator ---")
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        access_account()
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-3).")