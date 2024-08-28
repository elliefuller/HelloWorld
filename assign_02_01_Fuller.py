# Elliot Fuller
# MMIS 6391
# Assignment 2
# 8/28/2024

# Calculate employee salary after tax
def calculate_net_salary(gross_salary, tax_rate):
    tax = gross_salary * tax_rate / 100
    net_salary = gross_salary - tax
    return net_salary

# Example data
gross_salary = 9000
tax_rate = 7
net_salary = calculate_net_salary(gross_salary, tax_rate)
print(f"The net salary is: ${net_salary:.2f}")
