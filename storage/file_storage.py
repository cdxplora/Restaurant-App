import pickle
from .storage import Storage

class FileStorage(Storage):

    def __init__(self, filename):
        self._filename = filename

    def save(self, key, data):
        with open(self._filename, "wb") as f:
            pickle.dump({key: data}, f)

    def load(self, key):
        try:
            with open(self._filename, "rb") as f:
                data = pickle.load(f)
                return data.get(key)
        except FileNotFoundError:
            return None
