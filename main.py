
from Restaurant_app.menuItem import MenuItem
from Restaurant_app.menu import Menu
from cli.interface import run_cli as cli
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
    menu.add_item(MenuItem("Water", 0.35, "Drink"))
    menu.add_item(MenuItem("Ice Cream", 4.99, "Dessert"))
    return menu


def load_menu(storage):
    """Load menu from storage and rebuild Menu object"""
    loaded_data = storage.load("menu")
    menu = Menu("Main Menu")

    if loaded_data:
        for item_dict in loaded_data:
            menu.add_item(MenuItem.from_dict(item_dict))
        print("Menu loaded successfully!")
    else:
        print("No menu found, building default menu...")
        menu = build_menu()
        save_menu(storage, menu)
    return menu

def save_menu(storage, menu):
    """Serialize and save menu to storage"""
    menu_data = [item.to_dict() for item in menu.list_items()]
    storage.save("menu", menu_data)
    print("Menu saved successfully!")



def main():
    storage = JSONStorage("restaurant_data.json")       # An example of polymorphism: I can easily switch to a different storage mechanism (like MemoryStorage or FileStorage) without changing the rest of the code, as long as they implement the same interface defined by the Storage base class.
    restaurant = Restaurant("Lovely Eats", storage)  # Example of composition: Restaurant has a Storage object to manage data persistence
               

    # Load menu from storage (or build default menu)
    menu = load_menu(storage)
    restaurant.set_menu(menu)

    # Launch CLI
    try:
        cli(restaurant)
    except KeyboardInterrupt:
        print("\nExiting...Please try again later.") # I added error handler for KeyboardInterrupt to gracefully exit the CLI when user presses Ctrl+C

if __name__ == "__main__":
    main()