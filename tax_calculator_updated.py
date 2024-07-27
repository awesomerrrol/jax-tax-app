
import tkinter as tk
from tkinter import messagebox

# Function to calculate tax at 6%
def calculate_tax_6(value):
    return round(value * 0.06, 2)

# Function to calculate tax at 1.5%
def calculate_tax_1_5(value):
    return round(value * 0.015, 2)

# Function to calculate combined tax at 7.5%
def calculate_tax_7_5(value):
    return round(value * 0.075, 2)

# Function to handle button click and perform calculations
def calculate_taxes():
    try:
        value = float(entry_value.get())
        if value < 0:
            raise ValueError("Negative value")
        tax_6 = calculate_tax_6(value)
        tax_1_5 = calculate_tax_1_5(value)
        tax_7_5 = calculate_tax_7_5(value)
        
        label_tax_6.config(text=f"Tax at 6%: ${tax_6}")
        label_tax_1_5.config(text=f"Tax at 1.5%: ${tax_1_5}")
        label_tax_7_5.config(text=f"Combined tax at 7.5%: ${tax_7_5}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive monetary value.")

# Function to reset the input and results
def reset_fields():
    entry_value.delete(0, tk.END)
    label_tax_6.config(text="")
    label_tax_1_5.config(text="")
    label_tax_7_5.config(text="")

# Create the main window
root = tk.Tk()
root.title("Tax Calculator")

# Create and place the input field
label_value = tk.Label(root, text="Enter monetary value:")
label_value.pack(pady=5)
entry_value = tk.Entry(root)
entry_value.pack(pady=5)

# Create and place the Calculate button
button_calculate = tk.Button(root, text="Calculate", command=calculate_taxes)
button_calculate.pack(pady=10)

# Create and place the Reset button
button_reset = tk.Button(root, text="Reset", command=reset_fields)
button_reset.pack(pady=5)

# Create and place the result labels
label_tax_6 = tk.Label(root, text="", justify="left")
label_tax_6.pack(pady=5)
label_tax_1_5 = tk.Label(root, text="", justify="left")
label_tax_1_5.pack(pady=5)
label_tax_7_5 = tk.Label(root, text="", justify="left")
label_tax_7_5.pack(pady=5)

# Run the application
root.mainloop()
