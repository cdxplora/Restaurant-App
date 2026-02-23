class OrderItem:
    def __init__(self, menu_item, quantity: int):
        self._menu_item = menu_item
        self._quantity = quantity

    def subtotal(self):
        return self._menu_item.price * self._quantity
