# Example 1: Creating a class
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
# Example 2: Create and Call a Coin Flipping Class

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

#-------------------------------------------
# Example 3: Create bank class that allows depositing and withdrawing 
#...an amount from a bank balance

class BanksAccount:
    # Adding arguments to init means method expects something to...
    #... be passed when any method of BanksAccount is called
    def __init__(self,bal):
        # Amount passed to bal will be assigned to this variable
        self.__balance = bal

    # deposit method will expect amount to be passed
    # Assign amount to self.__balance
    def deposit(self, amount):

        # Short way to write self.__balance = balance + amt
        self.__balance += amount
    
    # Create withdraw method
    # Can use same variable amount because it is local to each method
    def withdraw(self, amount):
        # Validate that user can't withdraw more than curent amount
        if self.__balance >= amount:
            self.__balance -= amount 
        else:
            print('Error: Insufficient funds')
    
    # Show current balance
    def get_balance(self):
        return self.__balance
    
    # The __str__ method
    # Returns a string variable of the object's state
    def __str__
        return 'The balance is $' + format(self.__balance, '.2f')

#-------------------------------------------
# Example 4: Interacting with a separate class (Example 3)

import BankAccount:

def main():
    # Get starting balance from user
    start_bal=float(input('Enter your starting balance: '))

    # Note that BankAccount expects an argument passed due to
    #...init definition above
    # We will pass in our start_bal float the user gave us
    savings = bankaccount.BankAccount(start_bal)

    # Deposit user's savings contribution
    contribution = float(input('How much would you like to save? '))
    savings.deposit(contribution)
    # Print savings balance, format to two decimals with comma separator
    print('Your savings account balance is $', format(savings.get_balance(), ',.2f')
    

    # Use withdraw method to let user deduct cash
    cash = float(input('How much would you like to withdraw? '))
    savings.withdraw(cash)
     # Print savings balance, format to two decimals with comma separator
    print('Your savings account balance is $', format(savings.get_balance(), ',.2f')

    # For the last two chunks you can also use:
    # print(savings)
    # Savings is defined above as an instance of BankAccount
    # Calling it with no argument invokes the __str__ method from Ex. 3

main()