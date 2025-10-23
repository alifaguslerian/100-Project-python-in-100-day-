import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x300")
root.configure(bg="#f0f4c3")

title_label = tk.Label(root, text="BMI Calculator", font=("Arial", 20), bg="#f0f4c3")
title_label.pack(pady=20)

weight_label = tk.Label(root, text="Weight (kg):", font=("Arial", 12), bg="#f0f4c3")
weight_label.pack()

weight_entry = tk.Entry(root, font=("Arial", 12), width=15)
weight_entry.pack(pady=5)

height_label = tk.Label(root, text="Height (cm):", font=("Arial", 12), bg="#f0f4c3")
height_label.pack()

height_entry = tk.Entry(root, font=("Arial", 12), width=15)
height_entry.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f4c3")
result_label.pack(pady=20)

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) 
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be greater than 0.")
        bmi = weight / height ** 2
        status = ""
        if bmi < 18.5:
            status = "Underweight"
        elif 18.5 <= bmi < 25:
            status = "Normal"
        elif 25 <= bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"

        result_label.config(text=f"Your BMI is: {bmi:.2f}\nStatus: {status}", fg="green")   
    except ValueError:
        messagebox.showerror("Error", "Please enter valid weight and height.")

calculate_button = tk.Button(root, text="Calculate", command=calculate_bmi,font=("Arial", 12), bg="#4CAF50", fg="white")
calculate_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=lambda: [weight_entry.delete(0, tk.END), height_entry.delete(0, tk.END), result_label.config(text="")],font=("Arial", 12), bg="#f44336", fg="white")
reset_button.pack(pady=10)

root.mainloop() 