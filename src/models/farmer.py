
from .user import User
# Inheritance - Farmer inherits from User
class Farmer(User): 
    def __init__(self, name, phone, location, farm_size, primary_crops):
        super().__init__(self, name, phone, location)
        self.farm_size = farm_size
        self.primary_crops = primary_crops

    def authentication(self, entered_pin):
        if entered_pin == self._pin:
            return f"log in successfully"
        return f"Invalid PIN"
    def update_contact_details(self, new_name, new_phone, new_location):
        if self.name:
            self.name = new_name
            if self.phone:
                self.phone = new_phone 
                if self.location:
                    self.location = new_location
        return f"Name :{new_name}, Phone: {new_phone}, Location:{new_location}"
    

    def update_farm_details(self, new_farm_size, new_primary_crops):
        if self.farm_size:
            self.farm_size = new_farm_size
            if self.primary_crops:
                self.primary_crops = new_primary_crops 
        return f"New Farm_size :{new_farm_size}, New Primary crops: {new_primary_crops}"
        
    
        


    


