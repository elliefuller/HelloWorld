# Elliot Fuller
# MMIS 6391
# Assignment 2
# 8/28/2024

# Calculate the percent change between two prices
def calculate_percent_change(old_price, new_price):
    if old_price == 0:
        return "Old price cannot be zero"
    percent_change = ((new_price - old_price) / old_price) * 100
    return percent_change

# Example data
old_price = 280.40
new_price = 306.00
change = calculate_percent_change(old_price, new_price)
print(f"Percent change: {change:.2f}%")