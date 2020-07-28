# 8 DML Subqueries, Joins, and Combining Queries
## Multi-Table Queries
- Allow us to explore relationships
- Normalization doesn't allow different types of data in one table, we need to pull from several
## Subqueries
- Query nested within another query
	- More specifically, a SELECT statement inside of another SELECT statement
- Always enclosed in parenthesis
- Allows you to get data from table A, conditional on data from table B
	- Only use if the data are in a single table, the subquery is only for filtering
	- If you need more than one table's worth of data, use a join
- Can be used in SELECT, FROM, WHERE, or HAVING
				
## Join
- Combines rows from two or more tables
- INNER JOIN
	- Subset of records are returned that have matching values in **both** tables
	- In MySQL by JOIN or INNER JOIN are interchangeable
- OUTER JOIN (in MySQL)
	- LEFT JOIN or LEFT OUTER JOIN
		- All records from the left table and matching records from the right table are returned
		- *The left table is the table listed **first** in the FROM clause*
		- If there is no matching record on the right table, the result is null
	- RIGHT JOIN or RIGHT OUTER JOIN
		- Same as left join but vice-versa
		- *The right table is the table listed **second** in the FROM clause*
	- FULL JOIN is not supported in MySQL
		- All records are returned if there is a match in left or right table
		- To simulate, use a LEFT and RIGHT JOIN with a UNION
/Images/8_joins.png
## Combining Queries
- UNION
	- Returns all row values in one or both tables
	- Equivalent to an OR logical operation (A OR B)
- INTERSECT
	- Not supported in MySQL
	- All row values common to both tables
	- Equivalent to an AND logical operation (A AND B)
	- Can be accomplished with an INNER JOIN
- EXCEPT
	- Not supported in MySQL
	- All row values in the first table but not the second
	- Equivalent to NOT logical operator 
	- Can be accomplished with OUTER JOIN and IS NULL
- Rules for Set Operators
	- The fields involved in the operation must be the same number in each SELECT statement
	- The fields in each SELECT statement must be listed in the same order
	- The corresponding fields in each SELECT statement must have the same or compatible data types
- Fully-Qualified Names
	- An unambiguous name that specifies which object, function, or variable a call refers to without regard to the context of the call
		- Similar to a 'full path' to a file
	- Format for databases
		- `server_name.database_name.schema_name.object_name`
	- Use in tables
		- Fields/attributes need to be qualified with the name of the table 
		- Especially important because several tables might use similar names
		- E.g. `SELECT Vendors.vend_name` not just `SELECT vend_name`
	- Aliases
		- Use a table alias to shorten qualified names
		- Tables are aliased in the FROM statement:
			```
			SELECT v.vend_name
			FROM Vendors AS v
			```
		- Convention is to use the AS keyword when aliasing fields, but it is not needed or used for tables:
			```
			SELECT v.vend_name
			FROM Vendors v
			```
## Exercises
Sample data:
/Images/8_exercises.png

- What are the vendors of the product we currently stock? List the vendor name.
	- Use Subquery:
	```
	SELECT v.vend_name
	FROM Vendors v
	# Returns only vend_id present in Products vend_id 
	WHERE v.vend_id IN (SELECT p.vend_id
												FROM Products p)
	```
- What products do we carry? Which vendors supply these? List both vendor and product name.
	- Use Join
	- Two ways, implicit and explicit
		- Implicit adds the join condition in the WHERE clause
		- Explicit is preferred, the join condition is in the FROM clause
		- Implicit:
			```
			SELECT v.vend_name, p.prod_name
			FROM Vendors v, Products p
			# Join condition in WHERE clause
			WHERE v.vend_id = p.vend_id
			```
		- Explicit:
			```
			SELECT p.prod_name, v.vend_name
			FROM Vendors v
				JOIN Products p ON p.vend_id = v.vend_id
			```
- What vendors are in our database and what products do they supply (if any)?
	- Notice we want all vendors, this implies we need a left join:
		- Remember the left join is the *first* table listed in the FROM clause
		```
		SELECT v.vend_name, p.prod_name
		FROM Vendors v
			LEFT JOIN Products p ON p.vend_id = v.vend_id
		```