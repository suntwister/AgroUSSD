from abc import ABC, abrstractmethod

class User(ABC):
    def __init(self, name, phone, location):
        self.name = name
        self.phone = phone
        self.location = location

    def get_profiles(self):
        pass