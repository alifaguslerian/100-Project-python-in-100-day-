# temperatur converter

def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def calcius_to_kelvin(celcius):
    return celcius + 273.15


def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9 

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celcius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def show_menu():
    print("\n--- Temperature Converter Menu ---")
    print("1. Celcius to Fahrenheit & kelvin")
    print("2. Fahrenheit to Celcius & kelvin")
    print("3. Kelvin to Celcius & Fahrenheit")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        celcius = float(input("Enter temperature in Celcius: "))
        print(f"Fahrenheit: {celcius_to_fahrenheit(celcius): 2f}")
        print(f"Kelvin: {calcius_to_kelvin(celcius): 2f}")

    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"Celcius: {fahrenheit_to_celcius(fahrenheit): 2f}")
        print(f"Kelvin: {fahrenheit_to_kelvin(fahrenheit): 2f}")

    elif choice == "3":
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"Celcius: {kelvin_to_celcius(kelvin): 2f}")
        print(f"Fahrenheit: {kelvin_to_fahrenheit(kelvin): 2f}")

    elif choice == "4":
        print("Exiting the temperature converter. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1-4).")