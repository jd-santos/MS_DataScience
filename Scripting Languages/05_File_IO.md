# 05_File_IO
## Overview
- For program to retain data between runs, the data must be saved
	- Data is saved to an output file for later retrieval
- "Reading data from" is the process of retrieving data from an input file
- Two types of file
	- Text
		- Contains data encoded as text
	- Binary
		- Contains data not converted to text
		- Intended for a specific type of program to read
			- E.g. image file
- Two ways to access data on file
	- Sequential access
		- File read sequentially from beginning to end without skipping
	- Direct access
		- Jumping directly to any piece of data in a file
- Filenames and file objects
	- Filename extensions
		- Short sequence of characters at the end of a filename preceded by a period
		- Indicates type of data stored on file
	- File object
		- Objects associated with a specific file
		- Provides a way for programs to work with the file, like a file object referenced by a variable
- **open()** function
	- Creates a file object and associates it with a file on the disk
	- Format: `file_object = open(filename,mode)`
	- Mode is a string specifying how the file will be opened
		- (r)ead only
		- (w)rite
		- (a)ppend
- Specifying file location
	- If path not specified, open function assumes file is in the same directory
	- If a file is created while the program is running it will be created in the same directory
	- open function can specify alternate path and/or file name
	- Prefix the path string literal with the letter r
- Writing to file
	- **Method**
		- A function that belongs to an object
		- Performs operations using the object
	- **.write()** method
		- Writes data to file
		- Format: `file_variable.write(string)`
	- File should be closed using the close method file object
		- Format: `file_variable.close()`
	-(a)ppend
		- If file exists, it will not be erased
		- If it does not exist, it will be created
		- Appends data to end of file
	- When data is written to file
		- Record
			- Set of data that describes one item
		- Field
			- Single piece of data in record
	- When working with records it is also important to be able to:
		- Add records
		- Display records
		- Search for a specific record
		- Modify records
		- Delete records

## Reading from Files
- **read()** method
	- file object method that reads entire file contents into memory
	- Only works if the file has been opened for reading
	- Contents returned as string
- **readline()** method
	- File object method that reads a line from the file
	- Line returned as a string, including '\n'
	- Read position
		- Marks location of the next item to be read from a file 
	- Returns an empty string when the end of file is reached
		- You can use that empty string as a sentinel in a loop to know when to end
		- Otherwise you get infinite loops
## Processing with Loops
- Files typically hold large amounts of data
- Loops are typically used to read from and write to a file 
- Often the number of items stored in file is unknown
- `for` loop to read lines
	- Reads lines in a file and stops when end of file is reached
	- Format:
		```
		for line in file_object:
			statements
		```
	- The loop iterates once over each line in the file
