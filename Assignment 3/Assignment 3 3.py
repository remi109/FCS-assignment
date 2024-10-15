#ex 3
# Sample dictionary for available items in the shop
inventory = {
    "123": {"name": "Milk", "price": 1.50},
    "124": {"name": "Bread", "price": 2.00},
    "125": {"name": "Eggs", "price": 3.00},
}

# Function to start a new receipt
def start_new_receipt():
    print("Do you want to start a new receipt? (yes/no)")
    response = input().lower()
    if response == "yes":
        create_receipt()
    else:
        print("Goodbye!")

# Function to create and manage the receipt
def create_receipt():
    total = 0
    receipt = []

    while True:
        barcode = input("Enter item barcode: ")
        if barcode not in inventory:
            print("Item not found. Try again.")
            continue

        quantity = int(input(f"Enter quantity of {inventory[barcode]['name']}: "))

        # Add item to receipt
        item_total = quantity * inventory[barcode]['price']
        receipt.append({"name": inventory[barcode]['name'], "quantity": quantity, "price": inventory[barcode]['price'], "item_total": item_total})
        total += item_total

        print("Do you want to add another item? (yes/no)")
        response = input().lower()
        if response != "yes":
            break

    # Print the final receipt
    print("\nReceipt:")
    for item in receipt:
        print(f"{item['quantity']}x {item['name']} @ ${item['price']:.2f} each: ${item['item_total']:.2f}")
    print(f"Total: ${total:.2f}")
   
    print("Receipt printed.")
    start_new_receipt()

# Start the POS system
start_new_receipt()

