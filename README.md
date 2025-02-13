# Florida Sales Tax Calculator

A Python Tkinter desktop application for calculating sales tax in Duval County, Florida, compliant with DR-15EZ regulations.

---

## 📝 Description
This tool calculates Florida state sales tax (6%) and Duval County discretionary surtax (1.5%) for businesses, with support for:
- Late payment penalties and interest
- Collection allowances for electronic filing
- CSV export of results
- Input validation and compliance warnings

Built using Florida Department of Revenue guidelines from Forms DR-15EZN and DR-15EZ.

---

## ✨ Features
- **Tax Calculations**
  - 6% state sales tax
  - 1.5% Duval County discretionary surtax
  - Automatic total sales summation (cash + card)
- **Late Payment Handling**
  - 10% penalty (minimum $50)
  - Configurable months-late input
- **Collection Allowance**
  - 2.5% discount on first $1,200 of tax (max $30)
  - Donation option to Educational Enhancement Trust Fund
- **CSV Export**  
  - Generate audit-ready reports
- **Input Validation**  
  - Prevents negative/non-numeric entries
- **Surtax Compliance Warnings**  
  - Alerts for potential $5,000 item limitations

---

## ⚙️ Installation
1. **Prerequisites**  
   - Python 3.x ([Download](https://www.python.org/downloads/))
   - Tkinter (usually included with Python)

2. **Clone Repository**
   ```bash
   git clone https://github.com/your-username/florida-sales-tax-calculator.git
   cd florida-sales-tax-calculator
Run Application
python tax_calculator.py
🖥️ Usage
Enter Cash Sales and Card Sales amounts.

Toggle options:

🟦 Late Filing: Enable penalty/interest calculations

🟩 E-Filed On Time: Apply collection allowance

❤️ Donate Allowance: Redirect discount to education fund

Click Calculate Tax to view results.

Export calculations to CSV with Export to CSV.

📊 Technical Requirements
Python 3.8+

Tkinter (built-in)

CSV module (built-in)

⚠️ Limitations
Interest Rate: Uses placeholder 1% monthly rate (not linked to FL DOR's floating rate).

Surtax Compliance: Assumes no single item > $5,000. For accurate itemized calculations, manual adjustments are required.

Eligibility Checks: Does not validate DR-15EZ eligibility criteria.

🤝 Contributing
Pull requests are welcome! For major changes, open an issue first to discuss proposed changes.

📜 License
MIT
License: MIT

📧 Contact
For questions or support:

GitHub: @awesomerrol

Disclaimer: This tool is for educational/demonstration purposes only. Consult a tax professional for official filings.
