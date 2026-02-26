from pathlib import Path

import json
from .storage import Storage

class JSONStorage(Storage):

    def __init__(self, filename):
        self._filepath = Path(filename) # Here i converted filename into a Path object

    def save(self, key, data):
        all_data = self._read_file()
        all_data[key] = data

        with self._filepath.open("w", encoding="utf-8") as f:
            json.dump(all_data, f, indent=4)

    def load(self, key):
        all_data = self._read_file()
        return all_data.get(key)

    def _read_file(self):
        if not self._filepath.exists():
            return {}
        with self._filepath.open("r", encoding="utf-8") as f:
            return json.load(f)
