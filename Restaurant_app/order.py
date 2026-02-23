from Restaurant_app.orderItem import OrderItem


class Order:
    def __init__(self):
        self._items = []

    def add_item(self, menu_item, quantity: int):
        self._items.append(OrderItem(menu_item, quantity))

    def calculate_total(self):
        return sum(item.subtotal() for item in self._items)

    def list_items(self):
        return self._items