# 12 Dimensional Modeling Process and Concepts
## The 4-Step Dimensional Design Process
1. Select the business process
	- Something that businesses do that have an associated event
	- Expressed as action verb and represented activities the business performs
	- Measurements that users want to analyze result from business process events
2. Declare the grain
	- How do you describe a single row in the fact table?
	- The level of details associated with fact table measurements
3. Identify the dimensions
	-  How do business people describe the data resulting from the business process measurement events?
	-  'Decorate' fact tables with a robust set of dimensions representing all possible descriptions that take on single values in the context of each measurement
4. Identify the facts
	- What is the process measuring?
	- Must be true to grain defined earlier
	- Facts that belong to a different grain must be in a separate fact table 
	- In an E/R diagram the candidate fact table will generally have numeric measurements
		- Often found in intersection tables that resolve many-to-many relationships
- Considerations:
	- Both user business requirements and realities of your data source inform your design
## Measure Types
- Additive facts
	- Measures that can be added across all dimensions
	- E.g. quantity of items purchased
- Semi-additive facts
	- Measures that can only be added across some dimensions
	- E.g. bank account balances are not additive across time
- Non-additive facts
	- Measures that can't be added across any dimensions
	- E.g. unit prices, you might calculate total cost of sale but that's not the same as adding them as a measure
		- This is a confusing example
## Fact Table Types
- Transaction fact table
	- Record a business event or transaction, one record at a time
	- E.g. sales transaction
- Periodic fact tables
	- Record a snapshot of data for a specific period of time
	- E.g. inventory level at the end of a quarter
- Accumulating fact tables
	- Store a record for the entire lifetime of an event
	- Shows the activity as it progresses
	- E.g. mortgage application process
/Images/12_Fact_types.png
- Factless fact tables
	- Don't have numeric measures associated with them
	- Records a set of dimensional entities coming together at a point in time
		- The only "measure" will be a counter
/Images/12.2_factless_fact.png
## Dimension Table Types
- Date dimensions
	- Best practice is to put any date information in its own dimension
	- Dates have a lot of implied information, this helps analysis of date-related questions
	- Reduces redundant date operations
		- You don't need to calculate the quarter from a date, just store the quarter
	- Mandatory fields
		- Primary key
			- Surrogate key in YYYYMMDD format
		- Full date value with DATE data type
	- Optional fields
		- Enable filtering, aggregating, grouping, and labeling dates in reporting and analytics
		- E.g. MonthName, Quarter, DayOfWeek
- Time Dimensions
	- Requires date dimension
	- Time-of-Day as fact or dimension
		- Use as fact is time analysis is irrelevant or rarely conducted
		- If used, would have two columns related to date/time:
			- A field for the foreign key linked to the Date dimension
			- A DATETIME field that stores the date and time of the fact
		- Use as a dimension if there is a need to do time-of-day analysis
			- Fact table would have:
				- FK to date dim
				- FK to time dim
				- DATETIME field for date and time of fact (still stored here)
			- Determine level of grain (hour, minute, second?)
				- Determines number of rows in the dimension
					- Hour would only have 24 rows
	- Multiple time zones
		- If operations span multiple time zones, store both local date/time and global standard date/time with FKs in fact table and multiple dims
		- Dimension you might want:
			- dim_date_local
			- dim_date_GMT
			- dim_time_local
			- dim_time_GMT
- Role Playing Dimension
	- When a fact table has multiple columns with FKs linking back to the same dimension
	- E.g. billing and shipping address both in Dim_Address table
	- Each of the FKs linked to the same dimension signify a different 'role' played by the dimension
		- The dimension is being used in different business contexts for the same fact
	- Querying is problematic when using multiple filters on the same dimension
		- To filter, there needs to be a database entity associated with each role
		- The best solution is to create a **view** for each role
		- All views are actually the same table, but they have different keys
/Images/12.3_role_playing_views.png
- Degenerative Dimension
	- Foreign key stored in the fact table that does not link to any dimension
	- E.g. CarrierTrackingNumber, CustomerPONumber
	- For dimensions where no other attributes besides the key are needed
	- In OLTP systems these attributes would be foreign keys to other entities 
		- However here they don't need their own dimensions because those attributes are captured in other dimensions
- Outrigger Tables
	- Used when dimension is referenced within another dimension
	- Helps in modeling reality, which can be messy
	- Eliminates the need to redundantly store and update dimensional attributes
/Images/12.4_outriggers.png 

