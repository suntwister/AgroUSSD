
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, phone, location, pin):
        self.name = name
        self.phone = phone
        self.location = location
        self._pin = pin

    @abstractmethod
    def authenticate(self, entered_pin):
        pass

    @abstractmethod
    def update_contact_details(self, new_name = "", new_phone = "", new_location = ""):
        pass

    
   
