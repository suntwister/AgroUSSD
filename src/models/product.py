from abc import ABC, abstractmethod
class Product(ABC):
    def __init__(self, product_id, name, quantity, price)
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    @abstractmethod
    def get_info(self):
        pass