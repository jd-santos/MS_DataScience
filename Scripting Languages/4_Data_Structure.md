# Data Structure
## Lists
Sequence
	- Object that contains multiple items of data
	- Items are stored in sequence on after another
- Python provides different types of sequences like lists and tuples
	- Tuples are immutable, can't be changed once created
- **List**
	- An object that contains multiple data items
		- Those items are called **elements**
	- Format
		`list = [item1, item2, etc]`
	- Examples
		- List of integers [2, 3, 5]
		- List of strings [Batman, Cats, Men in Black]
-  **Index**
	-  A number specifying the position of an element in a list
	-  Enables access to individual element in a list
		-  Index of first element is 0, second is 1, nth element is n-1
		-  Negative indexes identify position relative to the end of a list
			-  -1 identifies the last element, -2 the next to last, etc
		Example
			```
			favorite_letters = [m,x,q,r]
			favorite_letters[1]
			# Output: x 
			```
	- Lists are mutable, program can change its contents
		`list[1] = new_value` will assign a new value to element at index 1
		- Must use a valid index to prevent IndexError Exception
	- **Concatenate**
		- Joining things together
		- The (+) operator can be used to concatenate two lists
		- Cannot concatenate a list with another data type, such as a number
		- Augmented assignment operator (+=) can also concatenate lists
		Example
		```
		list1 = [1,2,3]
		list2 = [4,5,6]
		list3 = list1 + list2
		list3
		# [1,2,3,4,5,6]
		
		#Alternatively:
		list2 += list1
		list2
		# [4,5,6,1,2,3]
		```
	- **len() function**
		- Returns the length of a sequence such as a list
			Example
			`size = len(favorite_letters)`
		- The index of the last element would be `len(list)-1`
			- If number of elements = 10, last element index is 9
	- **Slice**
		- A span of items taken from a sequence
		- Format: `list[start : end]`
		- Produces a list containing elements from start up to, *but not including*, end
			- If start not specified, 0 is used for start
			- If end not specified, len(list) is used for end index
		- Can include a step value and negative indices (relative to end of list)
	- **in** operator
		- Returns `True` if item is in the list or `False` if not
		- Format: `item in list`
		- Similarly, use `not` operator to determine whether an item is not in a list
	- **append**(item)
		- Adds items to the end of an existing list
	- **index**(item)
		- Used to determine where an item is located in a list
		- Returns index of the first element in the list containing item
		- Raises ValueError exception if item isn't found
	- Other useful methods
		- Insert
			- Needs two arguments: (index, element)
			- Format: `list.insert(2, 'Thor')`
				- Adds 'Thor' at index 2
		- Remove
			- Removes item from list
			- Format: `list.remove('Thor')`
		- Reverse
			- Reverses order of elements
			- Format: `list.reverse()`
## Tuple
- Tuple is an immutable sequence
	- Is immutable, cannot be changed once created
	-Otherwise similar to a list
Format: `tuple_name = (item1, item2)`
	- Notice we use parenthesis and not brackets
- Supports same operations as list that don't change items in list
- Faster to process than lists
- If you need to change items, convert to list using `list()` function
- Change list to tuple using `tuple()` function 
## Dictionary
- An object that stores a collection of data
- Each element consists of a *key* and *value*
	- Referred to as mapping a key to value
	- Key must be immutable
- To retrieve a specific value, use the associated key
- Format: `dictionary = {key1:val1, key2:val2...}`
- Uses ==curly braces== 
- `clear` method
	- Deletes all elements in a dictionary leaving it empty
	- Format: `dictionary.clear()`
- Retrieving a value 
	- Elements are unsorted/unordered, not a sequence
		- Can't retrieve using index, we need the key
	- Format: `dictionary[key]
	- Test whether a key is in a dictionary using `in` and `not in` 
- Add key/value to dictionary
		- Format: `office['David']='E320'`
		- Will append to end of `office` dictionary
- Keys must be immutable, but associated values can be any type of object
	- Values in a single dictionary can be different data types 
		- This includes lists and even dictionaries 
- len method
	- Used to obtain number of elements in a dictionary
- `get` method
	- Looks for key, returns value if found or returns a default value
	- dictionary.get('key_name', 'Default message')
- `clear` method
	- Deletes all elements in a dictionary leaving it empty
	- Format: `dictionary.clear()`
