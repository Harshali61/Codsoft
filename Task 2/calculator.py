import tkinter as tk
from math import sqrt

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

def button_sqrt():
    try:
        expression = display.get()
        result = sqrt(eval(expression))
        display.delete(0, tk.END)
        display.insert(tk.END, result)
    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

# Create a window
window = tk.Tk()
window.title("Calculator")

# Create an output/display window
display = tk.Entry(window, font=("Arial", 20))
display.grid(row=0, column=0, columnspan=4)

# Define buttons layout using a nested list
button_layout = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", ".", "=", "/"],
    ["√", "C"]
]

# Create buttons based on the layout
buttons = []
for i, row in enumerate(button_layout):
    button_row = []
    for item in row:
        button = tk.Button(window, text=item, padx=20, pady=10, command=lambda item=item: button_click(item))
        button_row.append(button)
    buttons.append(button_row)

# Position buttons on the grid
for i, button_row in enumerate(buttons):
    for j, button in enumerate(button_row):
        button.grid(row=i+1, column=j)

# Run the main event loop
window.mainloop()
