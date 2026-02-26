class Restaurant:
    def __init__(self, name: str, storage): # This class is the mother class that 
        self._name = name                   # represents the restaurant itself, holding its name, menu, and storage mechanism. 
        self._menu = None                   # It provides methods to set and get the menu, as well as to save and load the menu using the specified storage. This design allows for flexibility in how the restaurant's data is stored and retrieved.
        self._storage = storage 

    @property
    def name(self):
        return self._name

    def set_menu(self, menu):
        self._menu = menu

    def get_menu(self):
        return self._menu

    def add_order_item(self, order, item_name, quantity):
        item = self._menu.get_item(item_name)

        if item and item.is_available():
            order.add_item(item, quantity)
            return True

        return False