import tkinter as tk

# Main window
root = tk.Tk()
root.title("Click Counter")
root.geometry("400x300")
root.configure(bg="#e3f2fd")

# Counter Variable
counter = 0

# Increment Counter Function
def increment():
    global counter
    counter += 1
    counter_label.config(text=f"Clicks: {counter}")

def reset():
    global counter
    counter = 0
    counter_label.config(text=f"Clicks: 0")

# Title
title_label = tk.Label(root, text="Click Counter", font=("Arial", 20), bg="#e3f2fd")
title_label.pack(pady=20)

counter_label = tk.Label(root, text="Clicks: 0", font=("Arial", 16), bg="#e3f2fd")
counter_label.pack(pady=10)

# Increment Button
increment_button = tk.Button(root, text="Click", command=increment,font=("Arial", 14), bg="#4CAF50", fg="black")
increment_button.pack(pady=10)

# Reset Button
reset_button = tk.Button(root, text="Reset", command=reset,font=("Arial", 14), bg="#f44336", fg="black")
reset_button.pack(pady=10)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.quit,font=("Arial", 14), bg="#607d8b", fg="black")
exit_button.pack(pady=20)


root.mainloop()