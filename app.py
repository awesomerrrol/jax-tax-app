import tkinter as tk
from tkinter import ttk, messagebox
import csv
from datetime import datetime

# Florida Tax Configuration
STATE_RATE = 0.06
DUVAL_SURTAX_RATE = 0.015
SURTAX_LIMIT = 5000  # Per-item limit (disclosure needed)
PENALTY_RATE = 0.10
MIN_PENALTY = 50
COLLECTION_ALLOWANCE_RATE = 0.025
ALLOWANCE_CAP = 30

class TaxCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Florida Sales Tax Calculator - Duval County")
        
        # Create main container
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.grid(row=0, column=0)
        
        # Input Fields
        ttk.Label(self.main_frame, text="Cash Sales:").grid(row=0, column=0, sticky="w")
        self.cash_sales = ttk.Entry(self.main_frame)
        self.cash_sales.grid(row=0, column=1)
        
        ttk.Label(self.main_frame, text="Card Sales:").grid(row=1, column=0, sticky="w")
        self.card_sales = ttk.Entry(self.main_frame)
        self.card_sales.grid(row=1, column=1)
        
        # Late Filing Section
        self.late_var = tk.BooleanVar()
        ttk.Checkbutton(self.main_frame, text="Late Filing", variable=self.late_var).grid(row=2, column=0, sticky="w")
        
        ttk.Label(self.main_frame, text="Months Late:").grid(row=3, column=0, sticky="w")
        self.months_late = ttk.Spinbox(self.main_frame, from_=1, to=12, state='disabled')
        self.months_late.grid(row=3, column=1)
        self.late_var.trace_add('write', self.toggle_months_late)
        
        # Collection Allowance
        self.allowance_var = tk.BooleanVar()
        ttk.Checkbutton(self.main_frame, text="E-Filed On Time", variable=self.allowance_var).grid(row=4, column=0, sticky="w")
        
        self.donate_var = tk.BooleanVar()
        ttk.Checkbutton(self.main_frame, text="Donate Allowance", variable=self.donate_var).grid(row=4, column=1, sticky="w")
        
        # Calculate Button
        ttk.Button(self.main_frame, text="Calculate Tax", command=self.calculate).grid(row=5, column=0, columnspan=2)
        
        # Results Display
        self.results_text = tk.Text(self.main_frame, height=10, width=50)
        self.results_text.grid(row=6, column=0, columnspan=2)
        
        # Export Button
        ttk.Button(self.main_frame, text="Export to CSV", command=self.export_csv).grid(row=7, column=0, columnspan=2)
        
        # Input Validation
        for entry in [self.cash_sales, self.card_sales]:
            entry.configure(validate="key", validatecommand=(root.register(self.validate_number), '%P'))
    
    def validate_number(self, value):
        try:
            if value.strip() == "": return True
            float(value)
            return True
        except:
            return False
    
    def toggle_months_late(self, *args):
        self.months_late.config(state='normal' if self.late_var.get() else 'disabled')
    
    def calculate(self):
        try:
            # Base Calculations
            cash = float(self.cash_sales.get() or 0)
            card = float(self.card_sales.get() or 0)
            total_sales = cash + card
            
            # Tax Calculations
            state_tax = total_sales * STATE_RATE
            county_tax = total_sales * DUVAL_SURTAX_RATE  # Simplified assumption
            
            total_tax = state_tax + county_tax
            
            # Collection Allowance
            allowance = 0
            if self.allowance_var.get() and not self.donate_var.get():
                allowance_base = min(total_tax, 1200)
                allowance = min(allowance_base * COLLECTION_ALLOWANCE_RATE, ALLOWANCE_CAP)
            
            # Penalties & Interest
            penalty = 0
            interest = 0
            if self.late_var.get():
                penalty = max(total_tax * PENALTY_RATE, MIN_PENALTY)
                months = int(self.months_late.get())
                
                # Simplified interest - would need actual rate lookup
                interest_rate = 0.01  # Placeholder (1% monthly)
                interest = total_tax * interest_rate * months
            
            net_due = total_tax + penalty + interest - allowance
            
            # Display Results
            results = [
                f"Total Sales: ${total_sales:,.2f}",
                f"State Tax (6%): ${state_tax:,.2f}",
                f"County Surtax (1.5%): ${county_tax:,.2f}",
                f"Total Tax Due: ${total_tax:,.2f}",
                f"Collection Allowance: ${allowance:,.2f}" if allowance else "",
                f"Late Penalty: ${penalty:,.2f}" if penalty else "",
                f"Interest: ${interest:,.2f}" if interest else "",
                "--------------------------------",
                f"NET AMOUNT DUE: ${net_due:,.2f}",
                "\nNOTE: Surtax calculation assumes",
                "no single item > $5,000. For",
                "accurate calculations with items",
                "over $5k, use itemized input."
            ]
            
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "\n".join(results))
            
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {str(e)}")
    
    def export_csv(self):
        try:
            filename = f"tax_report_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Total Sales", "State Tax", "County Tax", 
                                "Total Tax", "Allowance", "Penalty", 
                                "Interest", "Net Due"])
                
                data = [
                    float(self.cash_sales.get() or 0) + float(self.card_sales.get() or 0),
                    (float(self.cash_sales.get() or 0) + float(self.card_sales.get() or 0)) * STATE_RATE,
                    (float(self.cash_sales.get() or 0) + float(self.card_sales.get() or 0)) * DUVAL_SURTAX_RATE,
                    (float(self.cash_sales.get() or 0) + float(self.card_sales.get() or 0)) * (STATE_RATE + DUVAL_SURTAX_RATE),
                    min((float(self.cash_sales.get() or 0) + float(self.card_sales.get() or 0)) * (STATE_RATE + DUVAL_SURTAX_RATE), 1200) * COLLECTION_ALLOWANCE_RATE if self.allowance_var.get() else 0,
                    max((float(self.cash_sales.get() or 0) + float(self.card_sales.get() or 0)) * (STATE_RATE + DUVAL_SURTAX_RATE) * PENALTY_RATE, MIN_PENALTY) if self.late_var.get() else 0,
                    (float(self.cash_sales.get() or 0) + float(self.card_sales.get() or 0)) * (STATE_RATE + DUVAL_SURTAX_RATE) * 0.01 * int(self.months_late.get() or 0) if self.late_var.get() else 0,
                    ((float(self.cash_sales.get() or 0) + float(self.card_sales.get() or 0)) * (STATE_RATE + DUVAL_SURTAX_RATE)) 
                    + (max((float(self.cash_sales.get() or 0) + float(self.card_sales.get() or 0)) * (STATE_RATE + DUVAL_SURTAX_RATE) * PENALTY_RATE, MIN_PENALTY) if self.late_var.get() else 0)
                    + ((float(self.cash_sales.get() or 0) + float(self.card_sales.get() or 0)) * (STATE_RATE + DUVAL_SURTAX_RATE) * 0.01 * int(self.months_late.get() or 0) if self.late_var.get() else 0)
                    - (min((float(self.cash_sales.get() or 0) + float(self.card_sales.get() or 0)) * (STATE_RATE + DUVAL_SURTAX_RATE), 1200) * COLLECTION_ALLOWANCE_RATE if self.allowance_var.get() else 0)
                ]
                writer.writerow(data)
            
            messagebox.showinfo("Success", f"Exported to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Export failed: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaxCalculatorApp(root)
    root.mainloop()
