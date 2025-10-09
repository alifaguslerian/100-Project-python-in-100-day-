# The mini atm machine

class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self._pin = pin
        self._balance = balance

    # Validate PIN
    def validate_pin(self, entered_pin):
        return entered_pin == self._pin
    
    # Check balance
    def check_balance(self):
        print(f"Your balance is: ${self._balance}")

    # Deposit
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    # Withdraw
    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds.")
        elif amount > 0:
            self._balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    # Change PIN
    def change_pin(self, old_pin, new_pin):
        if self.validate_pin(old_pin) and len(new_pin) == 4 and new_pin.isdigit():
            self._pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Invalid PIN or invalid PIN format.")

class ATM:
    def __init__(self):
        self.accounts = {}

    # Create account
    def create_account(self):
        account_number = input("Enter the account number: ")
        pin = input("Enter the PIN: ")
        if len(pin) == 4 and pin.isdigit():
            self.accounts[account_number] = BankAccount(account_number, pin)
            print("Account created successfully!")
        else:
            print("Invalid PIN format. Please enter a 4-digit PIN.")

    # Access account
    def authenticate_account(self):
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")

        account = self.accounts.get(account_number)
        if account and account.validate_pin(pin):
            print("Authentication successful.")
            self.account_menu(account)
        else:
            print("Invalid account number or PIN. Please try again.")

    # Account menu
    def account_menu(self, account):
        while True:
            print("\n--- Account Menu ---")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                account.check_balance()
            elif choice == "2":
                amount = float(input("Enter the deposit amount: "))
                account.deposit(amount)
            elif choice == "3":
                amount = float(input("Enter the withdrawal amount: "))
                account.withdraw(amount)
            elif choice == "4":
                old_pin = input("Enter your current PIN: ")
                new_pin = input("Enter your new PIN: ")
                account.change_pin(old_pin, new_pin)
            elif choice == "5":
                print("Exiting the account menu. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option (1-5).")

        # Main menu
    def main_menu(self):
            while True:
                print("\n--- Main Menu ---")
                print("1. Create Account")
                print("2. Access Account")
                print("3. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    self.create_account()
                elif choice == "2":
                    self.authenticate_account()
                elif choice == "3":
                    print("Exiting the program. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please select a valid option (1-3).")

if __name__ == "__main__":
    atm = ATM()
    atm.main_menu()