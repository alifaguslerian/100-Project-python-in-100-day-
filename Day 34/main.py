import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg="#e3f2fd")


def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwerror("Error", "Please enter a task.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])
    else:
        messagebox.showerror("Error", "Please select a task to delete.")

def clear_tasks():
    task_listbox.delete(0, tk.END)

task_label = tk.Label(root, text="To-Do List", font=("Arial", 24), bg="#e3f2fd")
task_label.pack(pady=10)

task_entry = tk.Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#e3f2fd")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task,font=("Arial", 12), bg="#4CAF50", fg="white")
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task,font=("Arial", 12), bg="#f44336", fg="white")
delete_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear Tasks", command=clear_tasks,font=("Arial", 12), bg="#607d8b", fg="white")
clear_button.grid(row=0, column=2, padx=5)

frame = tk.Frame(root)
frame.pack(pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(frame, font=("Arial", 12), width=50, height=15, yscrollcommand=scrollbar.set)
task_listbox.pack(pady=10)

scrollbar.config(command=task_listbox.yview)

exit_button = tk.Button(root, text="Exit", command=root.quit,font=("Arial", 12), bg="#607d8b", fg="white")
exit_button.pack(pady=10)

root.mainloop()