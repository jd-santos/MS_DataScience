# Intro Example
def main():
    print('I have a friend named Ethan')
    get_message
    print('Wow')

def get_message():
    print('JD')
    print('Santos')

get_message()

main()
#----------------------------
# Conversion Example

# Define conversion as constant 
kilometers_to_miles = .6214
def main():
    mykilometer = 0.0
    mykilometer = float(input('Enter number of Kilometers: '))
    # Call function show_miles and pass in mykilometer as argument
    show_miles(mykilometer)

# Local variable distance becomes whatever parameter is passed into it
def show_miles(distance):
    miles = 0.0
    miles = distance * kilometers_to_miles
    print('The conversion of ', format(distance, '.2f'), 'kilometers')
    print(' to miles is', format (miles, '.2f'), ' miles')

# Call function main
main()


#-----------------------
# Passing in multiple parameters

def main():
        first = int(input('Enter the first number:'))
        second = int(input('Enter the second number:'))
        calculate_avg(first,second)

# Define function that accepts two arguments
def calculate_avg(one, two):
    average = (one + two) / 2
    print('The average is',format(average, '.2f'))

main()