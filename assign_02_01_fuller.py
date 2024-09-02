# Elliot Fuller
# MMIS 6391
# Assignment 2
# 8/28/2024

# Calculate employee salary after tax
def calculate_net_salary(gross_salary, tax_rate):
    # Calculate the tax amount
    tax_amount = gross_salary * (tax_rate / 100)
    # Subtract the tax amount from the gross salary to get the net salary
    net_salary = gross_salary - tax_amount
    return net_salary

def main():
    # Example data
    gross_salary = 9000
    tax_rate = 7
    net_salary = calculate_net_salary(gross_salary, tax_rate)
    print(f"The net salary is: ${net_salary:.2f}")

if __name__ == "__main__":
    main()