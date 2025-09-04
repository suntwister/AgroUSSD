from abc import ABC, abstractmethod
class Product(ABC):
    def __init__(self, name, quantity, price)
        self.name = name
        self.quantity = quantity
        self.price = price

    @abstractmethod
    def get_info(self):
        pass