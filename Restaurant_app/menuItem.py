class MenuItem:
    def __init__(self, name: str, price: float, category: str):
        self._name = name
        self._price = price
        self._category = category
        self._available = True

    
    def to_dict(self):
        return {
            "name": self._name,
            "price": self._price,
            "category": self._category,
            "available": self._available
        }

    @staticmethod
    def from_dict(data):
        item = MenuItem(
            data["name"],
            data["price"],
            data["category"]
        )
        item._available = data["available"]
        return item

    @property
    def name(self):             # I controlled access using properties.
        return self._name       # I Used encapsulation to protect the name, prce and category attributes from being modified directly outside the class. 
                                # This allows for better control over how these attributes are accessed and modified, ensuring data integrity and consistency.
        
    @property
    def price(self):
        return self._price
    
    @property
    def category(self):
        return self._category
    
    def is_available(self):
        return self._available
    
    def set_availability(self, status: bool):
        if not isinstance(status, bool):
            raise ValueError("Availability must be True or False")
        self._available = status

    def __repr__(self):
        return f"{self._name} - ${self._price:.2f}"
    


