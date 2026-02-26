import unittest
from Restaurant_app.menuItem import MenuItem
from Restaurant_app.order import Order




class TestOrder(unittest.TestCase):

    def setUp(self):
        self.order = Order()
        self.item = MenuItem("Burger", 5.0, "Main")

    def test_add_item(self):
        self.order.add_item(self.item, 2)
        self.assertEqual(len(self.order.list_items()), 1)

    def test_total(self):
        self.order.add_item(self.item, 3)
        self.assertEqual(self.order.calculate_total(), 15.0)


if __name__ == "__main__":
    unittest.main()
