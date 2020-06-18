# Python Fundamentals
## Data Science
- Study of the collection, organization, analysis, interpretation, and presentation of data 
	- Deals with all aspects of data including the planning of data collection in terms of survey/experiment design
- We will be using Python to collect and manipulate data

## What is Python?
- High-level programming language that is widely used in a variety of settings
- Very readable with a wide range of libraries 
- Interpreter has two modes:
	- Script mode
		- Save a set of Python statements in a .py file
		- Run the file with `python filename` at the command line
	- Interactive mode
		- Typing Python statements into a prompt
		- Also called "Python Shell"
-IDLE Programming Environment
	- "Integrated Development Program"
	- Single program that provides tools to write, execute, and test a program
	- Installed with Python and runs in interactive mode
	- Built-in text editor with syntax highlighting and other features for Python

## Designing a Program

### Displaying Output
- **Function**
	- Piece of prewritten code that performs an operation
	- Statements execute in the order they appear
		- Top to bottom
- **Argument**
	- Data given to the function to do stuff with
- *print* function
	- Displays output on screen
- **String**
	- Sequences of characters
	- String literal
		- When string appears in the actual code
		- In python can be enclosed in double or single quotes
- **Variable**
	- Name that represents a value stored in the computer memory
	- **Assignment statement**
		- Used to create a variable make it reference data
	- `variable = expression`
	- `print(age)` -> expression

### Reading Input
- Programs sometimes need to read input typed by user on keyboard
- Use the built-in `input` function
	- Returns data as a string
	- Format: `variable = input("Enter some value: ")`
	- Assigns keyboard input to variable `variable`
	- Probably shouldn't name variables `variable`
- The `input` function always returns a string, but often you need other data types like numbers
	- Use built-in function to convert data between types 
	- `int(item)` converts `item` to an int
	- `float(item)` converts `item` to a float
- Use a **nested function**
```
	function1(function2(argument))
	age = int(input("Enter your age: "))
	income = float(input("Enter your income: ")
```

### Performing Calculations
- Math expression
	- Performs calculation and gives a value
- Most expressions are standard math operators but division works differently 
- Division
	- / operator performs floating point division
		-`>>> 5/2` -> 2.5
	- // operator performs integer division
		- Positive results truncated
			- `>>> 5//2` -> 2
		- Negative rounded away from zero
			- `>>> -5//2` -> -3 
- Operator precedence
	- 	Higher precedence first, same precedence from left to right
	1. Operations enclosed in parentheses 
	2. Exponents (**)
	3. Multiplication (*), division (/ and //), remainder (%)
	4. Addition (+) and subtraction (-)

## Data Output
### Manipulating String Literals
- Escape(\)
	- Allows you to escape from string
	- E.g.: `\n` mid-string will insert newline
- Combine (+)
	- Concatenates strings
- Duplicate (*)
	- `Hey3 ='Hey ' * 3`
	- `print(Hey3)
	- `>>> Hey Hey Hey `
- Multiline continuation character (\)
	- Allows breaking statement into multiple line
	- E.g.
		`print('my first name is',\ `
		`first_name)`
		
### Formatting Numbers
- Two arguments:
	- Numeric value to be formatted
	- Format specifier 
- Returns string containing formatted number 
- Format specifier typically includes precision and data type
- Floating point number
	- `format(123.4567, ',2f')`
	- .2 -> specifies precision
	- f -> specifies data type as floating point
- Integers
	- Type designator: `d` 
	- Cannot specify precision because it's an integer
	- `format(12345.4567, 'd')`	-> 12345
	- `format(12345.4567, ',d')`	-> 12,345
