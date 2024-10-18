items = {
    "12345": {"name": "Item1", "price": 10.0},
    "67890": {"name": "Item2", "price": 5.0},
    "11121": {"name": "Item3", "price": 7.5},
}

def start_receipt():
    receipt = []
    total = 0

    while True:
        barcode = input("Enter item barcode: ")
        if barcode not in items:
            print("Invalid barcode.")
            continue
        quantity = int(input("Enter quantity: "))
        item = items[barcode]
        cost = item["price"] * quantity
        receipt.append((item["name"], quantity, cost))
        total += cost

        more_items = input("Would you like to add another item? (yes/no): ").lower()
        if more_items != "yes":
            break

    print_receipt(receipt, total)

def print_receipt(receipt, total):
    print("\nReceipt:")
    for name, quantity, cost in receipt:
        print(f"{name} (x{quantity}): {cost:.2f}")
    print(f"Total: {total:.2f}\n")

def pos_system():
    while True:
        new_receipt = input("Start a new receipt? (yes/no): ").lower()
        if new_receipt == "yes":
            start_receipt()
        elif new_receipt == "no":
            break

pos_system()
