import datetime

def get_item_details():
    try:
        name = input("Enter item name (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            return None
        # Loop until a valid quantity is entered
        while True:
            try:
                quantity = int(input(f"Enter quantity for {name}: "))
                if quantity <= 0:
                    print("Quantity must be a positive integer.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a whole number for quantity.")
        # Loop until a valid price is entered
        while True:
            try:
                price = float(input(f"Enter unit price for {name}: $"))
                if price <= 0:
                    print("Price must be a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numerical value for price.")
        return {
            'name': name.capitalize(),
            'quantity': quantity,
            'price': price,
            'subtotal': quantity * price
        }
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
def generate_bill(items):
    if not items:
        print("\n--- Billing System ---")
        print("No items added to the bill.")
        return
    TAX_RATE = 0.08  # 8% sales tax
    # Header
    print("\n" + "="*50)
    print(" " * 15 + "SIMPLE RETAIL BILL")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    print(f"{'Item':<20} {'Qty':>5} {'Price':>10} {'Total':>10}")
    print("-" * 50)
    total_amount = 0
    # Items
    for item in items:
        print(
            f"{item['name'][:18]:<20} "
            f"{item['quantity']:>5} "
            f"${item['price']:>9.2f} "
            f"${item['subtotal']:>9.2f}"
        )
        total_amount += item['subtotal']
    # Calculations
    tax_amount = total_amount * TAX_RATE
    grand_total = total_amount + tax_amount
    # Summary
    print("-" * 50)
    print(f"{'Subtotal:':<40} ${total_amount:>9.2f}")
    print(f"{f'Tax ({TAX_RATE*100:.0f}%):':<40} ${tax_amount:>9.2f}")
    print("=" * 50)
    print(f"{'GRAND TOTAL:':<40} ${grand_total:>9.2f}")
    print("=" * 50)
    print("\nThank you for your business!\n")
def main():
    print("--- Welcome to the Simple Billing System ---")
    print("Enter item details one by one. Type 'done' for the item name to finish.")
    billing_items = []
    while True:
        item = get_item_details()
        if item is None:
            break
        if item:
            billing_items.append(item)
            print(f"Added: {item['name']} x {item['quantity']} (${item['subtotal']:.2f})\n")
    generate_bill(billing_items)
if __name__ == "__main__":
    main()