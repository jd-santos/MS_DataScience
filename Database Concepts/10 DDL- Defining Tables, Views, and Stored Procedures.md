# 10 DDL: Defining Tables, Views, and Stored Procedures
## Data Definition Language
- DDL statements are used for creating tables, relationships, and other database structures
	- e.g. Views, stored procedures, triggers, indexes, etc
## Tables
### Creating Tables Overview
- Within the same database, table names must be unique
	- Important for creating fully qualified value names
- Identify column properties
	- Primary Key (PK) and Foreign Key (FK) fields
		- Resolve many-to-many relationships if needed
	- Datatypes
	- Not Null fields
		- PKs can't be null
		- Mandatory minimum relationships
	- Other column properties, including default values and autoincrements
- Identify the order in which tables are created
	- Parent tables before children tables (PK table before FK table)
### Creating Exercise
/Images/10_table_exercise.png
- Use CREATE TABLE keyword 
	- Backticks rather than quotes are used for table and column identifiers
- roomy table
	- rmy_id is created as an INT that is NOT NULL and is auto-incremented to be a surrogate key
		- At the bottom it is specified as the PRIMARY KEY 
	```
	CREATE TABLE `M09_LE`.`roomy` (
		`rmy_id` INT NOT NULL AUTO_INCREMENT,
		`rmy_name` VARCHAR(75) NOT NULL,
		`rmy_birthdate` DATE NULL,
	# Identify PK, for composite key add other fields
	#..separated by a comma
		PRIMARY KEY (`rmy_id`));
	```
- pet_type table
	```
	CREATE TABLE `M09_LE`.`pet_type` (
		`pt_id` INT NOT NULL AUTO_INCREMENT,
		`pet_type` VARCHAR(75) NOT NULL,
		PRIMARY KEY (`pt_id`))
	```
#### Referential Integrity Constraints
- pets table
	- The lines after PK are the referential integrity constraints
		- Identify the fields roomy_fk and pet_type_fk as FKs
		- References identifies the source or parent field name of the FK
	- ON DELETE/ON UPDATE
		- What to do if a record in the parent or primary key table is deleted
		- NO ACTION (or RESTRICT)
			- The DBMS will reject attempts to delete/update a record in the parent table that will affect a FK/child (or 'orphan' the child)
		- CASCADE
			- Delete/update is propagated to FK/child record(s)
		- SENTINEL
			- Set to NULL if the PK/Parent is updated or deleted
			- FK must be allowed to be null
	- Format
		```
		CONSTRAINT `field_name` FOREIGN KEY (`source_field_name`)
			REFERENCES `schema`.`table` (`source_field_name`)
		```
		
	```
	CREATE TABLE `M09_LE`.`pets` (
		`pet_id` INT NOT NULL AUTO_INCREMENT,
		`pet_name` VARCHAR(75) NULL,
		`pet_birthdate` DATE NULL,
		`rmy_id` INT NOT NULL,
		`pt_id` INT NOT NULL,
		PRIMARY KEY (`pet_id`),
		CONSTRAINT `roomy_fk` FOREIGN KEY (`rmy_id`)
			REFERENCES `M09_LE`.`roomy` (`rmy_id`)
			ON DELETE NO ACTION ON UPDATE NO ACTION,
		CONSTRAINT `pet_type_fk` FOREIGN KEY (`pt_id`)
			REFERENCES `M09_LE`.`pet_type` (`pt_id`)
			ON DELETE NO ACTION ON UPDATE NO ACTION)
	```
### Changing Tables
- `ALTER TABLES` allows you to make changes to tables that have already been created
- Operations are DBMS specific
	- MySQL allows you to change datatypes, add columns, change column names, and others
- Best practice is to not alter a table if it contains data
	- Usually it is easier to create a new table with the desired structure and manually move it there
- Example
	- This will insert `pet_nickname` into our pets table after `pet_id`**‌**
	```
	ALTER TABLE `M08_LE`.`pets`
		ADD COLUMN `pet_nickname` VARCHAR(75) NULL AFTER `pt_id`
	```
### Deleting Tables
- Requires correct database privileges (along with create/alter)
- Use the `DROP TABLE` statement
	```
	DROP TABLE `m08_LE`.`roomy`;
	```
## Views
- Virtual tables that are created (via queries) on-the-fly
	- They dynamically retrieve data when used
- Use `CREATE VIEW`
- You can join with `USING` when the PK/FKs are named the same in both tables
- Creating a view
	```
	CREATE VIEW M10_LE.my_view AS
		SELECT *
		FROM sql_practice.customers JOIN sql_practice.orders USING (CustomerID)
	```
## Stored Procedures
- Collections of one or more SQL statements saved for future use
- Similar to a function
- Created with `CREATE PROCEDURE` and invoked with `CALL`
	```
	DELIMITER $$

	CREATE PROCEDURE GetCustomers()
	BEGIN
		SELECT 
			customerName, 
			city, 
			state, 
			postalCode, 
			country
		FROM
			customers
		ORDER BY customerName;    
	END$$
	DELIMITER ;
	```
Call the procedure:
`CALL GetCustomers();`