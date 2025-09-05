
class harvest:
    def __init__(self, farmer_name, product, quantity, quality, asking_price):
        self.farmer_name = farmer_name
        self.product = product
        self.quantity = quantity
        self.quality = quality
        self.asking_price = asking_price

    def farm_output(self):
        return f"Farmer name: {self.farmer_name}\nProduct: {self.product}\nQuantity: {self.quantity}\nQuality: {self.quality}\nAsking Price: {self.asking_price}"

