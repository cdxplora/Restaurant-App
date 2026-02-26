from Restaurant_app.menu import Menu
from Restaurant_app.menuItem import MenuItem

class MenuService:
    def __init__(self, storage):
        self._storage = storage 

    def save_menu(self, menu):
        menu_data = [item.to_dict() for item in menu.list_items()]
        self._storage.save("menu", menu_data)

    def load_menu(self):
        loaded_data = self._storage.load("menu")
        
        menu = Menu("Main Menu")

        if loaded_data:
            for item_dict in loaded_data:                            
                 menu.add_item(MenuItem.from_dict(item_dict))
        return menu
        
