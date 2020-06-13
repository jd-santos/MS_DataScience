def main():
    # Declare sale variable and daily lists
    sale_amount = 0.0
    daily_sales = []
    week_day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    
    # Create loop to iterate through week asking customer for sales
    # Append user sales to daily_sails list
    for i in week_day:
        sale_amount= input('Enter the sales for ' + i + ':')
        daily_sales.append(int(sale_amount))
    
    # Sum the list and store in local variable
    sum_amount = sum(daily_sales)

    # Print and format in dollars
    print('Total sales for the week: ', '$' + format(sum_amount, ',.2f'))
# Call function
# Don't ask me how often I forget to call the function when testing 
main()