from abc import ABC, abstractmethod

class Storage(ABC):

    @abstractmethod
    def save(self, key, data):
        pass

    @abstractmethod
    def load(self, key):
        pass
