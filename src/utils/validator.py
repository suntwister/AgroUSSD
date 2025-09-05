

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 11

def validate_crop_input(input):
    try:
        name, yield_per_acre = input.split(",")
        if name.strip() == "" or int(yield_per_acre.strip() <= 0):
            return False
    except:
        return False
    
def validate_livestock_input(input):
    try:
        name, animal_type = input.split(",")
        if name.strip() =="" or animal_type.strip =="":
            return False 
    except:
        return False
    

def validate_processed_good_input(input):
    try:
        name, method = input.split(",")
        if name.strip() =="" or method.strip() == "":
            return False
    except:
        return False

def validate_harvest_input(input):
    try:
        product, quantity, quality, price = input.split(",")
        if product.strip() == "" or float(quantity.strip() < 0) or quality.strip() == "" or float(price.strip() < 0):
            return False
    except:
        return False

def validate_market_entry_input(input):
    try:
        product, quantity, price, loc = input.split(",")
        if product.strip() == "" or float(quantity.strip() < 0) or float(price.strip() < 0) or loc.strip() =="":
            return False
    except:
        return False