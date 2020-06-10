# 03 Functions
## Overview
- Function
	- Group of statements within a program that perform a specific task
	- Usually one task of a large program
	- Can be executed in order to perform overall program task
	- Divide and conquer, modularity
- Function types
	- void
		- Executes the statements it contains and terminates
	- value-returning:
		- Executes statements and returns a value back to the statement that called it
		- The input, int, and float functions are value-returning functions
- Function name rules
	- Can't use key words
	- Can't contain spaces
	- First character must be letter or underscore
	- All other characters must be letter, number, or underscore
	- Capitalization matters
- Format
	```
	def function_name(): #Function header 
		statement
		statement
	```
- Calling a function
	- When a function is called:
		- Interpreter jumps to function and executes the statements
		- Afterward, interpreter jumps back to the part of the program that called the function
- Example
	```
	def get_message():
    print('JD')
    print('Santos')

	get_message()
	```
	Output:
		JD
		Santos
- Local variable
	- Variable assigned a value inside a function
	- Belongs to the function in which it was created
	- Only statements inside the function can access it
		- This means different functions can have local variables with the same name
- Passing arguments to functions
	- Argument
		- Piece of data that is sent into a function
		- Functions can use arguments in calculations
		- Arguments are placed in parentheses following the function name
	- Parameter
		- Variable that is assigned the value of an argument when the function is called
		- Format for defining
			```
			def function_name(parameter): 
			```
	Parameter Example:
	```
	# Define conversion as constant 
	kilometers_to_miles = .6214
	def main():
	    mykilometer = 0.0
	    mykilometer = float(input('Enter number of Kilometers: '))
	    # Call function show_miles and pass in mykilometer as argument
	    show_miles(mykilometer)
	
	# Local variable distance becomes whatever parameter is passed into it
	def show_miles(distance):
	    miles = 0.0
	    miles = distance * kilometers_to_miles
	    print('The conversion of ', format(distance, '.2f'), 'kilometers')
	    print(' to miles is', format (miles, '.2f'), ' miles')
	
	# Call function main
	main()
	```
Multiple Parameter Example:
```
def main():
        first = int(input('Enter the first number:'))
        second = int(input('Enter the second number:'))
        calculate_avg(first,second)

# Define function that accepts two arguments
def calculate_avg(one, two):
    average = (one + two) / 2
    print('The average is',format(average, '.2f'))

main()
```

- Standard libraries
	- Packages of functions installed with Python
	- Requires that you `import` modules before using them
	- Functions are called with `module_name.function_name` 
		- Check documentation for any arguments it accepts
## Applying Modules
Create module circle.py
```
import math
# Define area function
def area(radius):
	return math.pi * radius**2
# Define circumference
def circumference(radius):
	return 2*math.pi*radius
```

Create module rectangle.py
```
# Area functions that accept width and length
# Returns the area
def area(width, length):
	return width*length
def perimeter(width, length):
	return 2 * (width + length)
```

- To use a module you created, you import it like any other module
- Be sure the interpreter can find it, only use the file name if its in the same folder 
	- Otherwise specify the full path

Using our modules
```
import circle
import rectangle

radius = float(input(‘Enter the radius: ‘))

# Call our functions from our modules
print(‘The area is ‘, circle.area(radius))
print(‘The circumference is ‘, circle.circumference(radius)

width = float(input(“Enter the rect width: “))
length = float(input(“Enter the rect length: “))
print(‘The area is ‘, rectangle.area(width,length))
print(‘The perimeter is ‘, rectangle.perimeter(width,length))
```
## Value Returning Functions
- Currently we have only used void functions, now we will look at value returning functions
- Instead of printing the result in sum like we have before, we will instead `return` the value back to main() and assign the value to `total`
```
def main():
	# Get the users numbers
	first = int(input('Enter the first number: '))
	second = int(input('Enter the second number: '))
	
	# Return the result of second function to this function
	# Assign the returned value to total
	total = sum(first,second)
	print('The total is: ', total)
	
# The sum function, accepts two arguments
# Returns the sum of those two arguments
def sum(num1, num2)
	result = num1 + num2
	# Instead of printing, return 'result' to main()
	return result
	
	main()