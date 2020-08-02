# 11 Intro to Dimensional Modeling
## ER vs Dimensional Modeling
- Entity-Relationship models
	- OLTP systems designed for transaction throughput and updateability
	- Normalized to reduce redundancy and increase integrity
	- Bad for query performance because there are a lot more tables and relationships to crawl through with joins
	- Limited index use
	- Efficient storage
	- Eliminate inconsistencies
	- Easier maintenance
- Dimensional models
	- Designed to enable BI reporting, query, and analysis 
	- Usually not updated frequently
	- Data- and subject area-driven design
		- Only contain a subset of data so they are generally simpler
	- More data redundancy (denormalized)
	- More index use
	- Increased storage needs
	- Consolidates inconsistent data
	- More difficult maintenance
## Dimensional Modeling Concepts
- Two main entity (table) types: Facts and Dimensions
### Facts
- A measurement of a business activity, such as a business event or transaction
	- Provide specific measures of interest
	- Generally numeric
- Can be calculated and aggregated
	- E.g. sales numbers, any other KPIs
- Normalized and contain little redundancy
- The primary key is often a composite key, but can be a surrogate
- Two types of columns: Keys and Measures
#### Keys
- A group of foreign keys that point to the primary keys of dimensional tables
- Fact to dimensional tables are always many to one relationships
	- Many on the fact side, one on the dimension side
- There should be no NULL key values
	- This would mean there is no context for that dimension
#### Measures
- The 'facts' of a fact table
- Generally numeric
- Records of business activity
	- E.g. sales revenue, order qty
- Each measurement has a level of grain, or granularity
- **Granularity** 
	- The level of detail in the measurement of an event
	- Describes what an individual fact table row represents
	- The lowest (most detailed) grain captured in a business process
		- Determined by the data source
	- Best practice is to ensure all rows have a single, uniform grain
### Dimensions
- An entity that establishes the business context for the measures (facts) 
	- Generally descriptive in nature
	- E.g. dates, customers
- Represent the who, what, when, where, why, and how of the dimensional model
- The purpose of a dimension is using its attributes to filter and analyze data based on performance measures
- Often denormalized
- Often hierarchical
	- Permits drilling up, down, and across data
	- Example: DimGeography
		- Attributes: Zipcode, City, StateName, CountryCode
- Each row in a dimensional table is unique
- PK is a single field, no composite key
	- Best practice is to use surrogate key (except date/time dims)
	- This provides independence from source systems and makes them more indexable to help with joins
		- Since Dimensional tables come from source systems, we want to separate this PK from the source PK
		- Source system PKs may change
	- **Natural key**
		- A best practice of keep the source system PK as an alternate key (attribute) in the dimension table
		- Allows us to trace data back to the source if needed
- Attributes need to be
	- Descriptive: so others can understand it
	- Complete: no missing values
	- Unique: values can be identified
	- Valid: so it's useful to the business
### Schemas
- Ways to represent the entities and their relationships in a database
- OLTP uses relational schemas (ER)
- OLAP dimensional schemas include star, snowflake, and multidimensional
#### Star schema
- Most common for dimensional models
- Represented as a fact table surrounded by multiple dimension tables
	- Facts are normalized, dimensions are denormalized
- Traditionally instantiated within a relational database
/Images/11.1_Star.png 
#### Snowflake schema\
- Similar to star with a fact table surrounded by multiple dims
- The hierarchies within one or more dimensions are normalized
	- This results in multiple dimension tables per dimensions
	- Each level in the dimensional hierarchy is a table
	- The fact table stores the FK to the lowest level of dimensional hierarchy
- Traditionally instantiated within a relational database
/Images/11.2_Snowflake.png 
#### Multidimensional schema (OLAP cube)
- Hierarchical database with a multidimensional array
- Instantiated within a multidimensional database
- Data is stored and aggregated at various levels in the hierarchy
	- Dimensions form the 'axis'
	- Facts are the 'cells'
	- Aggregated data are the sides, edges, and corners
- Enables drilling up and down
/Images/11.3_Cube.png