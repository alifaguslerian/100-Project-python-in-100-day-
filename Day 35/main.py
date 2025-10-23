# Objective: Build a simple expance tracker app


import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

EXPENSE_FILE = "expenses.csv"

root = tk.Tk()
root.title("Expance Tracker")
root.geometry("600x600")
root.configure(bg="#f0f4c3")

expence = []

def load_expenses():
    if os.path.exists(EXPENSE_FILE):
        with open(EXPENSE_FILE, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                expence.append(row)
                expense_listbox.insert(tk.END, f"{row[0]} - {row[1]} - {row[2]}")

def save_expenses():
    with open(EXPENSE_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for expense in expence:
            writer.writerow(expense)

def add_expense():
    category = category_var.get()
    amount = amount_entry.get()
    description = description_entry.get()

    if not amount.isdigit() or not category or not description:
        messagebox.showerror("Error", "Please enter valid amount, category, and description.")

    expence.append([category, amount, description])
    expense_listbox.insert(tk.END, f"{category} | ${amount} | {description}")
    calculate_total()
    clear_inputs()
    save_expenses()

def delete_expense():
    selected = expense_listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "Please select an expense to delete.")
        return
    
    index = selected[0]
    del expence[index]
    expense_listbox.delete(index)
    calculate_total()

    save_expenses()

def clear_inputs():
    category_var.set("select category")
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

def calculate_total():
    total = sum(float(expense[1]) for expense in expence)

    total_label.config(text=f"Total Expance: ${total:.2f}")

def clear_all():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all expenses?"):
        expence.clear()
        expense_listbox.delete(0, tk.END)
        calculate_total()
        save_expenses()
    
title_label = tk.Label(root, text="Expance Tracker", font=("Arial", 24), bg="#f0f4c3")
title_label.pack(pady=10)

input_frame = tk.Frame(root, bg="#f0f4c3")
input_frame.pack(pady=10)

category_label = tk.Label(input_frame, text="Category:", font=("Arial", 12), bg="#f0f4c3")
category_label.grid(row=0, column=0, padx=5, pady=5)

category_var = tk.StringVar(value="select category")
category_dropdown = ttk.Combobox(input_frame, textvariable=category_var, values=["Food", "Entertainment", "Transport", "Other"], state="readonly", font=("Arial", 12))
category_dropdown.grid(row=0, column=1, padx=5, pady=5)

amount_label = tk.Label(input_frame, text="Amount($):", font=("Arial", 12), bg="#f0f4c3")
amount_label.grid(row=1, column=0 , padx=5, pady=5)

amount_entry = tk.Entry(input_frame, font=("Arial", 12))
amount_entry.grid(row=1, column=1, padx=5, pady=5)

description_label = tk.Label(input_frame, text="Description:", font=("Arial", 12), bg="#f0f4c3")
description_label.grid(row=2, column=0, padx=5, pady=5)
description_entry = tk.Entry(input_frame, font=("Arial", 12))
description_entry.grid(row=2, column=1, padx=5, pady=5)

btn_frame = tk.Frame(root, bg="#f0f4c3")
btn_frame.pack(pady=10)

add_button = tk.Button(btn_frame, text="Add Expense", command=add_expense, bg="#4caf50", fg="white")
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(btn_frame, text="Delete Expense", command=delete_expense, bg="#f44336", fg="white")
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(btn_frame, text="Clear All", command=clear_all, bg="#607d8b", fg="white")
clear_button.grid(row=0, column=2, padx=5)

frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

expense_listbox = tk.Listbox(frame, width=50, height=15, yscrollcommand=scrollbar.set, font=("Arial", 12))
expense_listbox.pack()

scrollbar.config(command=expense_listbox.yview)

total_label = tk.Label(root, text="Total Expenses: $0.00", font=("Arial", 14),bg="#f0f4c3")
total_label.pack(pady=10)

load_expenses()
calculate_total()

exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="#d32f2f", fg="white")
exit_button.pack(pady=10)

root.mainloop()