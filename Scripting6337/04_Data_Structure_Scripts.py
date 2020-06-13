# Simple search within list

# Create list 
prod_num = ['d3', 'r5', 't6']

# Get a product to search for
search = input("Enter product number: ")

# Determine if it's in the list
if search in prod_num:
        print(search, ' was found in the list')

# -----------
# Using lists in functions
def main():
    # Create empty list
    name_list=[]
    # Create control variable for loop
    again = 'y'
    # Add names from user
    while again == 'y':
        name = input('Enter name: ')
        # Append name to list
        name_list.append(name)
        # Give user chance to add another or quit loop
        print('Add another name?')
        again = input ('y = yes, anything else = no: ')
        # Empty space
        print()
    # Display names that were entered
    print('Names you entered:')

    for name in name_list:
        print(name)

# Call the main function
main()

#-----------------------

# Dictionary Example

# Create dictionary
office={'Eric':'E312', 'John':'E322','Aaron':'E332'}
# Call dictionary
office

# Call specific key
office['John']

# Use in loop
if 'John' in office:
        print(office['John'])

# Use list as a dictionary value
scores = {'student_A':[93, 92, 95], 'student_B':[84,89,82]}