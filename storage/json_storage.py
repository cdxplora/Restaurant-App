import json
import os
from .storage import Storage

class JSONStorage(Storage):

    def __init__(self, filename):
        self._filename = filename

    def save(self, key, data):
        all_data = self._read_file()
        all_data[key] = data
        with open(self._filename, "w") as f:
            json.dump(all_data, f, indent=4)

    def load(self, key):
        all_data = self._read_file()
        return all_data.get(key)

    def _read_file(self):
        if not os.path.exists(self._filename):
            return {}
        with open(self._filename, "r") as f:
            return json.load(f)
