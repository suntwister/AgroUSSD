
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, phone, location, pin):
        self.name = name
        self.phone = phone
        self.location = location
        self.__pin = pin

    # Abstract method - each type of user implements differently
    @abstractmethod
    def authentication(self):
        pass

    @abstractmethod
    def update_contact_details(self):
        pass

    @abstractmethod
    def update_farm_details(self):
        pass

   
