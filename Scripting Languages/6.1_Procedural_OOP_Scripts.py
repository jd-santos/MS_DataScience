# Creating a class
class Rectangle: # Convention: class name starts with capital
    count = 0 #class variable
    # Initializer
    # Can be used to assign default variables when initalized
    def __init__(self): # self not necessary but good practice
        # Instance variable self.#
        self.width = width
        self.height = height
        Rectangle.count += 1

#-------------------------------------
# Create and Call a Coin Flipping Class

import random

class Coin:
    # Define the initialize method 
    # Initialize sideup data attribute
    # __init__ will be executed when class is initialized
    def __init__(self):
        self.sideup = 'Heads'
    def toss(self):
        # From random module (class), use randint method
        # Randint returns random int between (a,b)
        if random.randint(0,1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'
    # As opposed to procedural, in OOP it's better for each...
    #...method to perform a single class
    def get_sideup(self):
        return self.sideup

# This function is outside of the Coin class
# It cannot communicate with the code above unless we call the class
# Normally this would be in separate code, in which case you need...
#... to call import Coin at the beginning

# import coin
def main():

    # Create an object from Coin class
    # Empty parenthesis will call the __init__ method from class
    # my_coin now becomes an instance of Coin
    # If this is separate code, you need to call with coin.Coin()
    my_coin  = Coin()

    # my_coin being an instance of Coin can now use Coin methods
    # Display side of coin facing up by using .get_sideup method
    print('This side is up: ', my_coin.get_sideup())
    my_coin.toss()
    print('Now this side is up: ', my_coin.get_sideup())

# Call main method
main()