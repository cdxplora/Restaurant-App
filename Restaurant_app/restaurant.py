class Restaurant:
    def __init__(self, name: str, storage):
        self._name = name
        self._menu = None
        self._storage = storage

    def set_menu(self, menu):
        self._menu = menu

    def get_menu(self):
        return self._menu

    def save_menu(self):
        self._storage.save("menu", self._menu)

    def load_menu(self):
        self._menu = self._storage.load("menu")
