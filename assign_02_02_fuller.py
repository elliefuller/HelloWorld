# Elliot Fuller
# MMIS 6391
# Assignment 2
# 8/28/2024

def calculate_final_price(price, tax_rate):
    tax_amount = price * (tax_rate / 100)
    final_price = price + tax_amount
    return final_price

def main():
    # Example data
    price = 710
    tax_rate = 4.5
    final_price = calculate_final_price(price, tax_rate)
    print(f"Final price after tax: ${final_price:.2f}")

if __name__ == "__main__":
    main()