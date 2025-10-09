class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print("\n--- Employee Details ---")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")

    def calculate_bonus(self):
        return self.salary * 0.1


class Manager(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

    def calculate_bonus(self):
        return self.salary * 0.2


class Developer(Employee):
    def __init__(self, name, emp_id, salary, programming_language):
        super().__init__(name, emp_id, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")

    def calculate_bonus(self):
        return self.salary * 0.5


# List untuk menyimpan data karyawan
employees = []

def add_employee():
    print("\n--- Choose Employee Type ---")
    print("1. Regular Employee")
    print("2. Manager")
    print("3. Developer")
    choice = input("Enter your choice: ").strip()

    name = input("Enter Employee Name: ").strip()
    emp_id = input("Enter Employee ID: ").strip()
    salary = float(input("Enter Employee Salary: ").strip())

    if choice == "1":
        employees.append(Employee(name, emp_id, salary))
    elif choice == "2":
        department = input("Enter Department: ").strip()
        employees.append(Manager(name, emp_id, salary, department))
    elif choice == "3":
        programming_language = input("Enter Programming Language: ").strip()
        employees.append(Developer(name, emp_id, salary, programming_language))
    else:
        print("Invalid choice")


def display_all_employees():
    if not employees:
        print("No employees available.")
    else:
        print("\n--- Employee List ---")
        for emp in employees:
            emp.display_info()
            print(f"Bonus: {emp.calculate_bonus()}")


# **Loop utama untuk program**
while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_employee()
    elif choice == "2":
        display_all_employees()
    elif choice == "3":
        print("Exiting the program.")
        break  # <-- Sekarang `break` ada di dalam loop utama, bukan di fungsi.
    else:
        print("Invalid Choice.")
