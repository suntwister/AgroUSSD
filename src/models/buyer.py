from .user import User
class buyer(User):
    def __init__(self, name, phone, location, business_type):
        super().__init__(name, phone, location)
        self.business_type = business_type

    def get_profiles(self):
        return {
            "Name": self.name,
            "Phone": self.phone,
            "Location": self.location,
            "Type": self.business_type
        }
        