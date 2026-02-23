import unittest
import os
from storage.json_storage import JSONStorage


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.filename = "test_data.json"
        self.storage = JSONStorage(self.filename)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_and_load(self):
        data = {"key": "value"}
        self.storage.save("test", data)
        loaded = self.storage.load("test")
        self.assertEqual(loaded, data)


if __name__ == "__main__":
    unittest.main()
