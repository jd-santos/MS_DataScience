#Constant for assessment percentage
assessment_rate = .6
tax_rate = .0072

# Define main, declare and initialize variables
# Get actual value from user
# Compute assessment and property tax
# Pass data to showPropertytax
def main():
    actual_value = float(input('Enter your actual value: '))
    assessment_value = assessment_rate * actual_value
    property_tax = assessment_value * tax_rate
    showPropertytax(assessment_value, property_tax)

# Create function to display tax information
# Accept function arguments
def showPropertytax(value, tax):
    print('Assessed value: ', '$' + format(value, ',.2f'))
    print('Property Tax: ', '$' + format(tax, ',.2f'))

# Call main
main()