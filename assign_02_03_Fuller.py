# Elliot Fuller
# MMIS 6391
# Assignment 2
# 8/28/2024

# Calculate the total number of items in inventory
inventory = {
    "Router": 201,
    "Access Point": 81,
    "Monitor": 3720
}

def count_inventory():
    total_items = sum(inventory.values())
    print(f"Total items in inventory: {total_items}")

# Example data
count_inventory()