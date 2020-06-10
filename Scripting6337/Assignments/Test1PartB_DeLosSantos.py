# Define main function
# Declare local varaibles and get amounts
def main():
    monthly_loan = float(input('Enter the monthly loan amount: '))
    monthly_ins = float(input('Enter the monthly insurance amount: '))
    monthly_gas = float(input('Enter the monthly gas amount: '))
    monthly_oil = float(input('Enter the monthly oil amount: '))
    monthly_tires = float(input('Enter the monthly tires amount: '))
    monthly_maint = float(input('Enter the monthly maintenance amount: '))
    expenses(monthly_loan, monthly_ins, monthly_gas, monthly_oil, monthly_tires, monthly_maint)

# Function to print info
# Should accept parameters from function call
# Compute total expense
def expenses(loan, ins, gas, oil, tires, maint):
    monthly_expense = loan + gas + ins + oil + tires + maint
    annual_expense = monthly_expense * 12
    print('Total monthly expense: ', '$' + format(monthly_expense, ',.2f'))
    print('Total annual expense: ', '$' + format(annual_expense, ',.2f'))




# Call main function
main()