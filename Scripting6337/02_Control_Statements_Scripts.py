# Create table with number and it's square
# Use escape operator (\) and 't' to create a tab
print("Number\tSquare")
print('----------------------')
# Create loop for numbers 1-10
# Two arguments means start and stop value
# Use exponent (**) for square
for number in range(1,10):
	square = number**2
	print(number,'\t', square)
