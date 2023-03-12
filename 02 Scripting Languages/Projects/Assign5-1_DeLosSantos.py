def main():
    # Open numbers.txt from local absolute location
    # For some reason can't open .txt directly even in the same directory
    readfile = open('/Users/jdmini/Repos/MS_DataScience/Scripting6337/Projects/Assign5-1_numbers.txt', 'r')
    # Assign contents to variable
    numbers = readfile.read()
    # Close the file
    readfile.close()
    # Print file contents
    print(numbers)
# Call function
main()