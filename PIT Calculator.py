initial_gross_income = float(input("Gross Income: "))
pension = 0.08 * initial_gross_income
nhf = 0
nhis = 0
life_assurance_p = 0
gross_income_less_relifs = initial_gross_income - (pension + nhf + nhis + life_assurance_p)
print("Gross Income (Less reliefs) :", gross_income_less_relifs)

if 0.01 * initial_gross_income > 200000:
    cra = 0.01 * initial_gross_income + 0.2 * gross_income_less_relifs
else:
    cra = 200000 + 0.2 * gross_income_less_relifs


taxable_income = initial_gross_income - (cra + pension)
tr = cra + pension + nhf + nhis + life_assurance_p

print("Consolidated Relief Allowance:", cra)
print("Pension:", pension)
print("National Housing Fund:", nhf)
print("National Health Insurance Scheme:", nhis)
print("Life Assurance Premium: ", life_assurance_p)
print(f"Total reliefs: {tr}")
print("Taxable Income:", taxable_income)

if taxable_income < 300000:
    paye = 0.07 * taxable_income
elif 300000 < taxable_income <= 600000:
    paye = 0.07 * 300000 + 0.11 * (taxable_income - 300000)
elif 600000 < taxable_income <= 1100000:
    paye = 0.07 * 300000 + 0.11 * 300000 + 0.15 * (taxable_income - 600000)
elif 1100000 < taxable_income <= 1600000:
    paye = 0.07 * 300000 + 0.11 * 300000 + 0.15 * 500000 + 0.19 * (taxable_income - 1100000)
elif 1600000 < taxable_income <= 3200000:
    paye = 0.07 * 300000 + 0.11 * 300000 + 0.15 * 500000 + 0.19 * 500000 + 0.21 * (taxable_income - 1600000)
else:
    paye = 0.07 * 300000 + 0.11 * 300000 + 0.15 * 500000 + 0.19 * 500000 + 0.21 * 1600000 + 0.24 * (taxable_income - 3200000)

print("PAYE:", paye)
net_income_ap = initial_gross_income - paye
print("Net Income After PAYE:", net_income_ap)
print("NOTE: All figures are in Naira (NGN) \n      as this algorithm is specific to  \n      the Nigerian personal income tax act")
