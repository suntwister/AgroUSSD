from .product import Product

class Crop(Product):
    def __init__(self, name, quantity, price, harvest_date, farmer_id):
        super().__init__(name, quantity, price)
        self.harvest_date = harvest_date
        self.farmer_id = farmer_id

    def get_info(self):
        return {
            "Name": self.name,
            "Quantity": self.quantity, 
            "Price": self.price, 
            "Harvest_date": self.harvest_date
            "Farmer_id": self.farmer_id
        }