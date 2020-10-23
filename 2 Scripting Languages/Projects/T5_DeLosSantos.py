# Write a program that calculated the average of all numbers from a file
# Store that result in a different file

# Student note: file names are changed for my file organization

def main():
    # Open text file containing some integers
    numfile = open('ZZ_ExampleData_Tnumbers.txt', 'r')
    # Open result file as write
    resultfile = open('ZZ_ExampleData_resultDeLosSantos.txt', 'w')
    # Create variables to calculate average
    running_total = 0.0
    count = 0.0
    avg = 0.0

    for line in numfile:
        # Convert numbers to float
        amount = float(line)
        # Add each line to variable to create cumulative sum
        running_total += amount

        # Increment count to calculate average
        # I don't remember learning this in lecture so I got creative
        count += 1.0
        avg = running_total / count

        # This will display the average for every iteration
         # Directions were unclear about whether to print final average once
         # or print the running average for every loop
        print('Current average: ', format(avg, '.2f'))
    
    # Write final average to result file
    resultfile.write(str(avg))
    
    # Close the files
    numfile.close()
    resultfile.close()

# Call main
main()
