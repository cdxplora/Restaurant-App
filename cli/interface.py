from Restaurant_app.order import Order

def run_cli(restaurant):
    """Command-line interface for the restaurant"""
    while True:
        print("\n--- Welcome to", restaurant._name, "---")
        print("1. Show Menu")
        print("2. Create Order")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_menu(restaurant)
        elif choice == "2":
            create_order(restaurant)
           
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def show_menu(restaurant):
    print("\n--- Menu ---")
    for item in restaurant.get_menu().list_items():
        availability = "Available" if item.is_available() else "Unavailable"
        print(f"{item} | {availability}")

def create_order(restaurant):
    order = Order()

    while True:
        item_name = input("\nEnter item name (or 'done' to finish): ")
        if item_name.lower() == "done":
            break

        quantity_input= input("Quantity: ")
        if not quantity_input.isdigit():
            print("Please enter a valid number for quantity.")
            continue

        quantity = int(quantity_input)

        item = restaurant.get_menu().get_item(item_name)

        if item and item.is_available():
            order.add_item(item, quantity)
            print(f"Added {quantity} x {item.name}")
        else:
            print(f"Item '{item_name}' is not available.")

    print_order_summary(order)

def print_order_summary(order):
    print("\n--- Order Summary ---")
    for i in order.list_items():
        print(f"{i._menu_item.name} x {i._quantity} = €{i.subtotal():.2f}")

    print(f"Total: €{order.calculate_total():.2f}")