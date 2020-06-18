# Define replacement cost global variable
insurance_rate = .8


def main():
    # Obtain replacement cost
    replacement_cost = float(input('What is the replacement cost of your building? '))
    # Calculate insurance amount
    insure_amount = replacement_cost * insurance_rate
    # Call showInsure and pass in parameters
    showInsure(replacement_cost, insure_amount)

# Define print function with two arguments
# Print all statements with arguments and global variable
def showInsure(replacement, minimum):
    print('Replacement cost: $', format(replacement, '.2f'))
    print('Percent insured:', format(insurance_rate, '.0%'))
    print('Minimum insurance: $',format(minimum, '.2f'))

main()