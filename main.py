from pathlib import Path

from Restaurant_app.menuItem import MenuItem
from Restaurant_app.menu import Menu
from Restaurant_app.order import Order
from Restaurant_app.restaurant import Restaurant
from storage.json_storage import JSONStorage


def build_menu():
    """Create a default menu"""
    menu = Menu("Main Menu")
    menu.add_item(MenuItem("Burger", 8.99, "Main"))
    menu.add_item(MenuItem("Fries", 3.49, "Side"))
    menu.add_item(MenuItem("Coke", 1.99, "Drink"))
    menu.add_item(MenuItem("Salad", 5.99, "Side"))
    menu.add_item(MenuItem("Pizza", 10.99, "Main"))
    return menu

def save_menu(storage, menu):
    """Serialize and save menu to storage"""
    menu_data = [item.to_dict() for item in menu.list_items()]
    storage.save("menu", menu_data)
    print("Menu saved successfully!")

def load_menu(storage):
    """Load menu from storage and rebuild Menu object"""
    loaded_data = storage.load("menu")
    menu = Menu("Main Menu")
    if loaded_data:
        for item_dict in loaded_data:
            item = MenuItem.from_dict(item_dict)
            menu.add_item(item)
        print("Menu loaded successfully!")
    else:
        print("No menu found, building default menu...")
        menu = build_menu()
        save_menu(storage, menu)
    return menu

def cli(restaurant):
    """Command-line interface for the restaurant"""
    while True:
        print("\n--- Welcome to", restaurant._name, "---")
        print("1. Show Menu")
        print("2. Create Order")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            print("\n--- Menu ---")
            for item in restaurant.get_menu().list_items():
                availability = "Available" if item.is_available() else "Unavailable"
                print(f"{item} | {availability}")
        elif choice == "2":
            order = Order()
            while True:
                item_name = input("\nEnter item name (or 'done' to finish): ")
                if item_name.lower() == "done":
                    break
                quantity_input = input("Quantity: ")
                if not quantity_input.isdigit():
                    print("Please enter a valid number")
                    continue
                quantity = int(quantity_input)
                item = restaurant.get_menu().get_item(item_name)
                if item and item.is_available():
                    order.add_item(item, quantity)
                    print(f"Added {quantity} x {item.name}")
                else:
                    print("Item not found or unavailable")
            print("\n--- Order Summary ---")
            for i in order.list_items():
                print(f"{i._menu_item.name} x {i._quantity} = ${i.subtotal():.2f}")
            print(f"Total: ${order.calculate_total():.2f}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def main():
    storage = JSONStorage("restaurant_data.json")
    restaurant = Restaurant("Lovely Eats", storage)

    # Load menu from storage (or build default menu)
    menu = load_menu(storage)
    restaurant.set_menu(menu)

    # Launch CLI
    cli(restaurant)

if __name__ == "__main__":
    main()