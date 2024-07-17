# Step 1: Input wages, taxable interest, unemployment compensation, status, and taxes withheld
wages = int(input())
taxable_interest = int(input())
unemployment_compensation = int(input())
status = int(input())
taxes_withheld = int(input())

# Calculate Adjusted Gross Income (AGI)
AGI = wages + taxable_interest + unemployment_compensation

# Output AGI formatted with comma separators
print(f"AGI: ${AGI:,}")

# Check if AGI is above $120,000
if AGI > 120000:
    print("Error: Income too high to use this form")
    exit()

# Step 2: Determine deduction amount based on status
if status == 1:  # Single
    deduction = 12000
elif status == 2:  # Married
    deduction = 24000
else:
    print("Invalid status provided. Assuming single.")
    deduction = 12000

# Calculate taxable income
taxable_income = AGI - deduction
if taxable_income < 0:
    taxable_income = 0

# Output deduction and taxable income formatted with comma separators
print(f"Deduction: ${deduction:,}")
print(f"Taxable income: ${taxable_income:,}")

# Step 3: Calculate federal tax based on tax brackets
if status == 1:  # Single filers
    if taxable_income <= 10000:
        federal_tax = round(0.1 * taxable_income)
    elif taxable_income <= 40000:
        federal_tax = round(1000 + 0.12 * (taxable_income - 10000))
    elif taxable_income <= 85000:
        federal_tax = round(4600 + 0.22 * (taxable_income - 40000))
    else:
        federal_tax = round(14500 + 0.24 * (taxable_income - 85000))
elif status == 2:  # Married filers
    if taxable_income <= 20000:
        federal_tax = round(0.1 * taxable_income)
    elif taxable_income <= 80000:
        federal_tax = round(2000 + 0.12 * (taxable_income - 20000))
    else:
        federal_tax = round(9200 + 0.22 * (taxable_income - 80000))
else:
    federal_tax = 0  # Default case

# Output federal tax formatted with comma separators
print(f"Federal tax: ${federal_tax:,}")

# Step 4: Calculate tax due or refund
tax_due_or_refund = federal_tax - taxes_withheld

# Output tax due or refund formatted with comma separators
if tax_due_or_refund >= 0:
    print(f"Tax due: ${tax_due_or_refund:,}")
else:
    print(f"Tax refund: ${-tax_due_or_refund:,}")
