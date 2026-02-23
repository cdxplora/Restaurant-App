from .storage import Storage

class MemoryStorage(Storage):

    def __init__(self):
        self._data = {}

    def save(self, key, data):
        self._data[key] = data

    def load(self, key):
        return self._data.get(key)
