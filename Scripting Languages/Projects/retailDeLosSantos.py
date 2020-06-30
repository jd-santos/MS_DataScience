# Write a class named RetailItem that holds data about an item in a retail store
# The class should store the following data in attributes:
    # items description, units in inventory, and price

# Define a class named RetailItem
class RetailItem:
    # Define the _init_ to start the attributes
    def __init__(self, desc, units, price):
        self.description = desc
        self.units = units 
        self.price = price

# Define several set- methods to assign attributes
    def set_description(self):
        self.description = desc

    def set_units(self):
        self.set_units = units

    def set_price(self, price):
        self.set_price = price


# Define get- related methods, each func should return args

    def get_description(self):
        return self.description

    def get_units(self):
        return self.units

    def get_price(self):
        return self.price
