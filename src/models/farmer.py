
from .user import User
# Inheritance - Farmer inherits from User
class Farmer(User): 
    def __init__(self, name, phone, location, farm_size, primary_crops):
        super().__init__(self, name, phone, location)
        self.farm_size = farm_size
        self.primary_crops = primary_crops

    def authenticate(self, entered_pin):
        return entered_pin == self._pin

    
    def update_contact_details(self, new_name="", new_phone="", new_location=""):
        if new_name:
            self.name = new_name
        if new_phone:
            self.phone = new_phone
        if new_location:
            self.location = new_location
        return "Contact updated!"
    
    def update_farm_details(self, new_location = "", new_farm_size = "", new_primary_crops = ""):
        if new_location:
            self.location = new_location
        if new_farm_size:
            self.farm_size = new_farm_size
        if new_primary_crops:
            self.primary_crops =  new_primary_crops
        return "farm details updated!"
    
        


    


