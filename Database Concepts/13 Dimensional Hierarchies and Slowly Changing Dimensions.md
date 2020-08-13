# 13 Dimensional Hierarchies and Slowly Changing Dimensions
## Dimensional Hierarchies
- A cascading series of many-to-one relationships
- They document relationships across levels
	- However, they are not always consistent across levels 
	- Vary on number of levels and parent-child relationships
- Different types of hierarchies: balanced, unbalanced, ragged
### Balanced Hierarchies
- Dimensional branches have the same number of levels
- Dimension branches have consistent parent-child relationships
	- Each parent has a child in the level directly blow it and vise versa
/Images/13.1_Balanced_Hierarchy.png
### Ragged Hierarchies
- Dimensional branches have varying number of levels
- Inconsistent parent-child relationships (I.e. skipped levels)
/Images/13.2_Ragged_Hierarchy.png
### Unbalanced Hierarchies
- Dimensional branches have varying number of levels
- Still have consistent parent-child relationships
/Images/13.3_Unbalanced_Hierarchy.png
### Modeling Ragged and Unbalanced Hierarchies
- Recursive pointers
	- Embedding the parent-child relationship in the dimension
/Images/13.4_Recursive_pointer.png 
- Bridge table
	- Create a table that bridges the relationship between the dimension and fact tables
	- Best practice
/Images/13.5_Bridge_Table.png
## Slowly Changing Dimensions (SCD)
- Dealing with attributes that change over time
- Context over time is important
	- Analyzing "as was" and "as is" 
### Eight SCD types
- Type 0: Keep original, never update
- Type 1: Overwrite data
- Type 2: Create new row for new values
- Type 3: Track changes with separate columns
	- e.g. OriginalJobTitle, CurrentJobTitle
- Type 4: Add mini-dimensions
	- Separate dimension for fields that change frequently
- Type 5: Combine types 1 and 4
- Type 6: Combine types 1, 2, and 6
- Type 7: Use both types 1 and 2
### Multivalued Dimensions
- Occur when a fact measurement is associated with multiple values in a dimension table
- Many-to-many (M:N) relationship between fact and dimension that needs to be resolved
- Potential solutions:
	- Use only one value and ignore the others
	- Extend the attributes
		- Make more attributes in the dimension table
	- Use a bridge table (best practice again)
		- Allows analysis of M:N relationships
		- Allows weighting of relationships (which is more important)
