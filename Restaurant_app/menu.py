class Menu:
    def __init__(self, name: str):
        self._name = name
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item_name: str):
        self._items = [i for i in self._items if i.name != item_name]

    def get_item(self, item_name: str):
        for item in self._items:
            if item.name == item_name:
                return item
        return None

    def list_items(self):
        return [item for item in self._items if item.is_available()]

    def __repr__(self):
        return f"Menu({self._name})"