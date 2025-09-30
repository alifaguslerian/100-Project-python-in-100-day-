import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title("Drawing Pad")
root.geometry("600x600")
root.configure(bg="#f0f0f0")

current_color = "black"
current_thickness = 2

canvas = tk.Canvas(root, width=500, height=400, bg="white", relief="ridge", bd=2)
canvas.pack(pady=20)

def draw(event):
    x, y = event.x, event.y
    canvas.create_oval(
        x - current_thickness, y - current_thickness,
        x + current_thickness, y + current_thickness,
        fill=current_color, outline=current_color
    )

def clear_canvas():
    canvas.delete("all")

def change_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color

def change_thickness(value):
    global current_thickness
    current_thickness = int(value)

canvas.bind("<B1-Motion>", draw)

control_frame = tk.Frame(root, bg="#f0f0f0")
control_frame.pack(pady=10)

color_btn = tk.Button(control_frame, text="Color", command=change_color, font=("Arial", 10), bg="#4CAF50", fg="black", )
color_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(control_frame, text="Clear", command=clear_canvas, font=("Arial", 10), bg="#f44336", fg="black")
clear_btn.grid(row=0, column=1, padx=10)

thickness_label = tk.Label(control_frame, text="Thickness:", font=("Arial", 10), bg="#f0f0f0")
thickness_label.grid(row=0, column=2, padx=10)

thickness_slider = tk.Scale(control_frame, from_=1, to=10, orient="horizontal", command=change_thickness, bg="#f0f0f0")
thickness_slider.set(2)
thickness_slider.grid(row=0, column=3, padx=10)

root.mainloop()




