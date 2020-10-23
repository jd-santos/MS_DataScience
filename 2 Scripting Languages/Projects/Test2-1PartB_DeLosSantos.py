# Design a program that asks user to enter a series of 10 numbers
# Store numbers in a list and display the low, high, total, and average of the list

# Define main function
def main():
    # Declare list of numbers and variable to store user input
    our_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    their_list = []
    current_number = 0


    # Create loop to iterate through list of numbers asking user for entry
    # Append number to list
    for i in our_list:
        current_number = float(input('Enter number ' + str(i) + ' of 10: '))
        their_list.append(current_number)
    
    # Calculate min, max, sum, and average and store in variables 
    low = min(their_list)
    high = max(their_list)
    total = sum(their_list)
    # Compute avg as the total divided by number of items in list
    avg = total / len(their_list)

    # Print the values
    print('Low: ', format(low, '.2f'))
    print('High: ', format(high, '.2f'))
    print('Total: ', format(total, '.2f'))
    print('Average: ', format(avg, '.2f'))

# Call our function
main()