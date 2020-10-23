# Declare BMI min/max constants
bmi_min = 18.5
bmi_max = 25.0

# Set weight and height equal to user input
weight = float(input('Enter your weight in pounds: '))
height = float(input('Enter your height in inches: '))

# Declare BMI variable with calculation
# Round and set to float
bmi = float(format(weight * (703/height**2), '.2f'))

#Determine weight category
if bmi < bmi_min:
    print('Your Body Mass Indicator is', bmi)
    print('You are underweight.')
elif bmi > bmi_min and bmi < bmi_max:
    print('Your Body Mass Indicator is', bmi)
    print('Your weight is optimal.')
else:
    print('Your Body Mass Indicator is', bmi)
    print('You are overweight.')

