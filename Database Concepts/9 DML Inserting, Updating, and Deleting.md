# 9 DML Inserting, Updating, and Deleting
## Inserting Data
- Use INSERT statement to insert data into database tables
###  Insert a single complete row
- Complete means all fields/columns are accounted for
	- Technically the columns do not need to be specified (the parenthesis after Products in the example), but it is a good practice to avoid insertion errors
		- Allows you to change order of inserted values
- The order of the fields corresponds the order of the values, they need to be the same
	```
	INSERT INTO Products (prod_id, vend_id, prod_name,
		prod_price, prod_desc)
	VALUES ('RYL03', 'FNG01', 'Princess doll', 9.49, NULL)
	```
### Insert a single partial row
- Partial means only some fields in a row are inserted
- Same as above but the fields *must* be specified since you are skipping some
- Any skipped fields must allow NULL values
- Add multiple rows by adding a comma after each set in VALUES
	```
	INSERT INTO Products ( prod_id, vend_id, prod_name, prod_price)
	
	VALUES ('RYL03', 'FNG01', 'Princess doll', 9.49),
				('RYL04', 'FNG01', 'Prince doll', 9.49);
	```
### Insert the results of a query
#### Import into a Table
- Done by including a SELECT statement inside the INSERT statement
- You can use SELECT * for all fields if there are no duplicate values
		- In this case we might assume that ProductsOld contains some of the same prod_id since it's the PK, so there would be duplicates and SELECT * would produce an error
- Include a WHERE clause to filter which records are inserted
	```
	INSERT INTO Products (prod_id, vend_id, prod_name, prod_price)
		SELECT prod_id, vend_id, prod_name, prod_price
		FROM ProductsOld
		WHERE prod_price > 5
	```
#### Export to another Table
- Use SELECT INTO to export the results of a query to a separate table
- Can use WHERE, GroupBy, Having, etc
- This method not supported by MySQL 
	```
	SELECT prod_id, vend_id, prod_name, prod_price
		INTO ProductsCopy
		FROM Products
	```
## Updating Data
- Use the UPDATE statement
- UPDATE the table
- SET the field to a new value
- Use WHERE to specify which row(s) to update
	- **Don't forget this** otherwise you will update the field in every row
	- Generally you want to use the primary key so you know exactly which records you are updating
- Good practice is to test your intended update with a SELECT statement first
	- Allows you to see which fields will be updated
	```
	UPDATE Products
		SET prod_price = 9.99
		WHERE prod_id = 'RYL03'
	```

## Deleting Data
- Use DELETE FROM statement to remove records from database
- Same guidelines as Updates, be sure of what you are deleting
- Make sure referential integrity is enforced
	- You don't want to delete records that are referenced in related tables unless this is your intention
	```
	DELETE FROM Products
		WHERE prod_id = 'RYL03'
	```