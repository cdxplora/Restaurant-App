class OrderItem:
    def __init__(self, menu_item, quantity: int): # This class demonstrates aggregation by containing a reference to a MenuItem object. Each OrderItem represents a specific menu item and the quantity ordered.
        self._menu_item = menu_item                 # It also uses encapsulation and abstraction to manage the details of the menu item and quantity, providing a method to calculate the subtotal for that item in the order.
        self._quantity = quantity

    def subtotal(self):
        return self._menu_item.price * self._quantity
