def main():
    # Open a file named professors.txt with write mode
    # Write mode creates file if it doesn't exist
    outfile = open(r'Datasets/professors.txt', 'w')

    # Write the names of professors to the file
    outfile.write('Jaeki Song\n')
    outfile.write('Eric Walden\n')
    outfile.write('David Lucus\n')

    # Close the file
    outfile.close()

# Call our function
main()

#---------------------------
# Practice reading contents of file

# Read the contents of professors.txt
def main():
    # Open professors.txt in read mode
    infile = open(r'Datasets/professors.txt', 'r')
    # Read three lines from a file seperately
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    # Close the file
    infile.close()
    # Print lines individually
    print(line1)
    print(line2)
    print(line3)

# Call main
main()

#---------------------------
# Practicing Append

# Read the contents of professors.txt
def main():
    # Open professors.txt in read mode
    myfile = open(r'Datasets/professors.txt', 'a')

    # Append new data
    myfile.write('Benjamin Mitchell\n')
    myfile.write('Glenn Browne\n')

    # Close the file
    myfile.close()

# Call main
main()

#-----------------------------
# Practice using loops 

def main():
    # Open sales.txt file
    sales_file = open('/Users/jdmini/Repos/MS_DataScience/Scripting6337/Datasets/05_sales.txt', 'r')
    
    # Read line and save it into "line"
    # Even though this is numeric data, it still reads in as a string
    line = sales_file.readline()

# Create loop
# readline() returns empty string after all lines are read
# Use empty string as loop condition
    while line != '':
        # line is read in as a string, convert to float
        amount = float(line)
        # Format
        print(format(amount, '.2f'))
        # Read the next line
        line = sales_file.readline()
    # Close the file
    sales_file.close()
# Call your new shiny function
main()


#-------------------------------
# Read lines with for loop

def main():
    # Open sales.txt file
    sales_file = open('/Users/jdmini/Repos/MS_DataScience/Scripting6337/Datasets/05_sales.txt', 'r')
    
    # Read all the lines in from the file
    for line in sales_file:
        # Convert line to float
        amount = float(line)
        print(format(amount, '.2f'))
        
        # Close file
    sales_file.close()
# Call your new shiny function
main()


#---------------------------------------
# This program adds coffee inventory records to the coffee.txt file

def main():
    # Create a variable to control the loop.
    another = 'y'

    # Open the coffee.txt file in append mode.
     # Append mode: file will be created if it doesn't exist
    coffee_file = open('ZZ_05_coffee.txt', 'a')

    # Add records to the file.
    while another == 'y' or another == 'Y':
        # Get the coffee record data.
        print('Enter the following coffee data:')
        descr = input('Description: ')
        qty = int(input('Quantity (in pounds): '))

        # Append the data to the file.
        coffee_file.write(descr + '\n')
        coffee_file.write(str(qty) + '\n')

        # Determine whether the user wants to add
        # another record to the file.
        print('Do you want to add another record?')
        another = input('Y = yes, anything else = no: ')

    # Close the file.
    coffee_file.close()
    print('Data appended to coffee.txt.')

# Call the main function.
main()

#-----------------------------------------
# Search file for records matching user input

def main():
    # Create a bool variable to use as a flag.
    found = False

    # Get the search value.
    search = input('Enter a description to search for: ')

    # Open the coffee.txt file.
    coffee_file = open('coffee.txt', 'r')

    # Read the first record's description field.
    descr = coffee_file.readline()

    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        # We've read the first line above so this reads next line
        qty = float(coffee_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # Determine whether this record matches
        # the search value.
        if descr == search:
            # Display the record.
            print('Description:', descr)
            print('Quantity:', qty)
            print()
            # Set the found flag to True.
            found = True

        # Read the next description.
        descr = coffee_file.readline()

    # Close the file.
    coffee_file.close()

    # If the search value was not found in the file
    # display a message.
    if not found:
        print('That item was not found in the file.')

# Call the main function.
main()


#---------------------------------------
# Display records in file

def main():
    # Open the coffee.txt file.
    coffee_file = open('coffee.txt', 'r')

    # Read the first record's description field.
    descr = coffee_file.readline()

    # Read the rest of the file.
    while descr != '':
        # Read the quantity field.
        qty = float(coffee_file.readline())

        # Strip the \n from the description.
        descr = descr.rstrip('\n')

        # Display the record.
        print('Description:', descr)
        print('Quantity:', qty)

        # Read the next description.
        descr = coffee_file.readline()

    # Close the file.
    coffee_file.close()

# Call the main function.
main()



