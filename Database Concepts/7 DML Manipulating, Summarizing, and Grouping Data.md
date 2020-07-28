# 7 DML Manipulating, Summarizing, and Grouping Data
## Manipulating Data
- We often do not want the data returned in a SQL statement exactly as it is represented in a database
- Uses
	- Formatting
		- Application needs
			- Data needs to be in a specific format
			- Often much faster to do this on DBMS
		- User needs
			- Data needs to be in a specific format (e.g. for a report)
	- Data redundancy 
		- Often we don't store values that can be calculated from existing database values
### Calculated fields
- Fields created on the fly with the SELECT statement
- Do not exist in the database
- Broadly refers to converting, calculating, and reformatting data using SQL
- Numeric datatypes
	- Mathematical calculations using arithmetic operators
	- E.g.
		```
		SELECT prod_id, quantity, price, quantity*price
		FROM Orders
		ORDER BY prod_id
		```
		- This would produce four columns, with the last one being the product of the quantity and price columns
- Strings
	- Used for combining columns into a single field (concatenation)
	- Can include other string characters that aren't in the table by surrounding them with single quotes
	- In MySQL use `CONCAT()` or `CONCAT_WS()` functions 
	```
	SELECT CONCAT(firstName, '', lastName) FROM Customers
	```
- Concatenates the firstName column, a space, then the lastName column
- If concatenating different datatypes you may need to use a function to convert values to correct datatype
### Functions
- Operations performed on data
- Usually specific to the DBMS 
	- MySQL functions may differ from TSQL, etc
	- Use the reference library for your DBMS
- Facilitate the manipulation or conversation of data
- Types
	- String
	- Numeric
	- Datetime
	- System
### Aliases
- Renaming column output, especially for calculated fields
- Optional but a best practice
- Use the **AS** keyword
- `SELECT ... , quantity*price AS item_total`
	- The quantity*price column will be renamed to item_total
## Summarizing Data
### Aggregate functions
- Used to summarize data
- Returns summary, not the data themselves
- Operate on a set of rows to calculate and return a single value
/Images/7_Agg_Functions.png 
- Examples
	- Select total number of records from an Orders table
	```
	SELECT COUNT(*)
	FROM Orders
	```
	- Select average from Orders
	```
	SELECT AVG(total_price)
	FROM Orders
	```
- Using `Distinct()` with aggregate functions
	- Can be used with most aggregate functions except COUNT(*)
		- You can, however, use COUNT(column)
## Grouping Data
### Using `GROUP BY` 
- Divides data into logical sets so that you can perform aggregate calculations on each group
- Example:
	```
	SELECT vend_id, COUNT(*) AS num_prods
	FROM Products
	GROUP BY vend_id
	```
	- This statement creates a group for each vend_id, then COUNT(*) counts the number of records in each group
	- The resulting output will be each vend_id and the count of records they contain
- *If you are aggregating, you need a GROUP BY clause on non-aggregated fields*
- If you are aggregating *or grouping*, any field that is chosen in the SELECT statement needs to be in the GROUP BY clause *unless* the field is aggregated 
### Using HAVING
- Used with GROUP BY to filter grouped data
- Supports all WHERE operators mentioned before
- Example
	```
	SELECT vend_id, COUNT(*) AS num_prods
	FROM Products
	GROUP BY vend_id
	HAVING COUNT(*) >= 2
	```
	- Filters to vend_id's with two or more rows
- Difference between WHERE and HAVING
	- WHERE filters before data is grouped
	- HAVING filters after data is grouped
	- Both can be used in one query:
		```
		SELECT vend_id, COUNT(*) AS num_prods
		FROM Products
		WHERE prod_price >= 4
		GROUP BY vend_id
		HAVING COUNT(*)>= 2
		```
		- WHERE applies before the group, this filters which rows will be aggregated/grouped
## Building Queries
Recommended order:
- FROM
	- Tables that are needed
- SELECT
	- Columns/fields you are selecting
- WHERE
	- To specify conditions for query
- GROUP BY (if aggregating)
	- Aggregate statements in SELECT clause
- HAVING
	- If filtering at the group level
- ORDER BY 