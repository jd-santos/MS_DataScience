# Control Statements

## Decision Structures
### Single Alternative Decision Structure (IF)
- Only one path of execution
- E.g. "Is it cold outside?"
	- Yes, wear a coat
	- No, don't wear a coat
- **if statement**
	- Decides whether a section of code executs or note
	- Uses a boolean to decide whether the next statement or block of statements executes 
	- Format:
	```
	if boolean expression is true:
		execute statement
	```
	- Insert colon (:) after if statement
	- Statements must be indented
- **Boolean expression**
	- Expression tested by if statement to determine if it is true or false
	- Relational operator
		- Determines whether a specific relationship exists between two values
		- E.g. greater than (>)
### Dual Alternative Decision Structure (IF-ELSE)
- Two possible paths of execution 
- One is taken if condition is true, the other if the condition is false
- Format:
```
if condition:
	statements
else:
	other statements
```
### Nested Decision Structure 
- Decisions structures can be nested within each other
- Used when multiple conditions need to be assessed sequentially
- **elif**
	- Used to test a series of conditions 
- Logical operators
	- Can be used to create complex Boolean expressions
	- Binary operators
		- `and` and `or` 
		- Connect two Boolean expressions into a compound Boolean expression
	- Unary operator
		- `not`
		- Reverses the truth of its Boolean operand
## Repetition
- Often we have to write code that performs the same task multiple times
- **Repetition structure** 
	- Makes the computer repeat included code as necessary
	- Includes condition-controlled loops and count-controlled loops
### Condition-Controlled (While) Loop
- While condition is true, due something
- Two parts
	- Condition tested for true or false value
	- Statement repeated as long as condition is true
- Format:
```
while [condition]
statement
```

While Example:
```
keep_going = 'y'
while keep_going == 'y':
	# Calculate commission
	sales = float(input('Enter the amount of sales: '))
	comm_rate = float(input('Enter the commission rate: '))
	commission = sales * comm_rate
	# Print commission and ask whether to repeat the process
	print ('The commission is $ ' +
				format(commission, '.2f'))
	keep_going = input('Calculate another +
		' commission? (Enter y for yes)')
```

- The question at the end will assign keep_going to user input
	- If user enters y, the while condition is true and it will loop

- Infinite loop
	- Loop that has no way of stopping
	- Repeats until program is interrupted
	- Occurs when programmer forgets to include stopping code
- Loops must contain a way to terminate or you will get an infinite loop
	- Something inside a while loop must eventually make the condition false

### Count-Controlled (For) Loop
- Iterate a specific number of times 
- For loops are designed to work with sequence of data items
	- Iterates once for each item in the sequence
- General format:
```
	for [variable] in [value 1, value 2...]`
		 statements
```
- **Target variable**
	- The variable which is the target of the assignment at the beginning of each iteration
	- Can be used in calculations or tasks in the body of the loop
	- Use `[variable] in [list]` to have the variable be reassigned to the next value in the list after an iteration
/Images/6337-03 For Loop.png
- The **range** function
	- Returns an iterable object
		- Iterable: contains a sequence of values that can be iterated over
	- Simplifies for loops
	- Arguments
		- One: [ending limit]
		- Two: [starting limit, ending limit]
		- Three: [starting limit, ending limit, step value]
Example:
```
# Print JD 5 times
for num in range(5):
	print('JD')
```
```
# Create table with number and its square
# Use escape operator (\) and 't' to create a tab
print("Number\tSquare")
print('----------------------')
# Create loop for numbers 1-10
# Two arguments means start and stop value
# Use exponent (**) for square
for number in range(1,10):
	square = number**2
	print(number,'\t', square)
```

Number	    Square
----------------------
1    	 1
2    	 4
3    	 9
4    	 16
5 	     25
6 	     36
7 	     49
8 	     64
9    	 81

Notice the loop only went to 9 because this is the ending *limit* not the ending *value* 

Tweak the code to allow users to input the range:
```
start = int(input("Enter the starting number: ")
end = int(input("How high do you want to go? ")
# User will give you the ending value, not the ending limit
# Add one to the ending value to get the correct limit
for number in range(start, end+1):
	...
```