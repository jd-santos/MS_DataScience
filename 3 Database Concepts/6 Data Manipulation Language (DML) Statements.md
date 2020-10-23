# 6 Data Manipulation Language (DML) Statements
## Review

- Relational databases primarily comprise a collection of tables that store a set of structured data
	- They represent a part of reality that we are interested in storing
- Tables also referred to as relations, hence relational databases
	- Tables contain:
		- Columns, also called attributes or fields
		- Rows, also called tuples or records
- Datatype
	- Type of allowed data
	- Every column has an associated datatype that restricts (or allows) specific data in that column
## Select/From/Where Framework
- SELECT clause
	- Specifies which columns are to be listed in the query results
- FROM clause
	- Species which tables are to be used in the query
- WHERE clause
	- Specifies with conditions or filters which rows are to be listed in the query results
	- Optional, if we want to return every record we can omit the WHERE clause
- Structure
	- `SELECT column(s) FROM table WHERE conditions`
- Operators
	- Reserved keyword or character used in a WHERE clause to perform an operation, such as comparisons or arithmetic operation
	- Often return TRUE or FALSE 
	- Use parentheses in the WHERE clause to direct the order of operations

| Operator | Meaning                                         |
|----------|-------------------------------------------------|
| =        | is equal to                                     |
| != or <> | is not equal to                                 |
| <        | less than                                       |
| >        | greater than                                    |
| <= or >= | less/greater than or equal to                   |
| !<       | not less than                                   |
| !>       | not greater than                                |
| AND      | returns true when both expressions are TRUE     |
| OR       | returns true if at least one is TRUE            |
| NOT      | negates the associated operator                 |
| IN       | is equal to one of a set of values              |
| BETWEEN  | within a range of values (including end points) |
| LIKE     | matches a set of characteristics                |
| IS NULL  | equal to NULL                                   |
### Additional Functions
- Sorting
	- Uses the ORDER BY clause
	- Default is (ASC)ending, you can change this to (DESC)ending order
		- e.g. `SELECT column FROM table ORDER BY column DESC`
- Retrieving unique rows
	- Uses the DISTINCT keyword after the SELECT statement
	- e.g. `SELECT DISTINCT column...`
- Wildcards
	- Used in the WHERE clause with the LIKE operator 
	- Only used with String datatypes
	- Inserted into a string query to represent that any character could be filled where the wildcard operators are
		- For any number of characters use %
		- For just a single character use _
	- e.g. `SELECT column FROM table WHERE column_x LIKE 'S%'`
		- Would return any row where column_x contains an S followed by any number of characters
		- If instead of % we used an underscore _ then return any row where column_x contains S followed by a single character
	
	