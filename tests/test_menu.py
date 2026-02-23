import unittest
from Restaurant_app.menu import Menu
from Restaurant_app.menuItem import MenuItem

class TestMenu(unittest.TestCase):

    def setUp(self):
        self.menu = Menu("Test Menu")
        self.burger = MenuItem("Burger", 10.0, "Main")
        self.menu.add_item(self.burger)

    def test_add_item(self):
        self.assertEqual(len(self.menu.list_items()), 1)

    def test_get_item(self):
        item = self.menu.get_item("Burger")
        self.assertIsNotNone(item)
        self.assertEqual(item.name, "Burger")

    def test_get_non_existent_item(self):
        item = self.menu.get_item("Pizza")
        self.assertIsNone(item)

if __name__ == '__main__':
    unittest.main()