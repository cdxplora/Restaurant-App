from Restaurant_app.orderItem import OrderItem


class Order:
    def __init__(self):     # The Order class manages a customer's order, allowing items to be added and calculating the total cost. 
        self._items = []    # It uses the OrderItem class to represent each item in the order, which includes the menu item and its quantity.
                            # The calculate_total method sums up the subtotals of all items in the order to get the final total cost. 
    def add_item(self, menu_item, quantity: int):       # This class is essential for processing customer orders and calculating the bill.
        self._items.append(OrderItem(menu_item, quantity))      

    def calculate_total(self):
        return sum(item.subtotal() for item in self._items)

    def list_items(self):
        return self._items