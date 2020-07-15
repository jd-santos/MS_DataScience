# 4 NoSQL Databases
## Overview
- NoSQL Database
	- A database technology that does not use tabular schema found in relational databases to model and represent reality
	- "Non-relational"
	- Flexible schemas, don't have to be defined ahead of time
	- Better at storing unstructured or semi-structured data 
## Data Models
/Images/4_All_NoSQL.png
### Document
- Stores semi-structured data in document format
- Uses JSON, BSON, XML, YAML or similar encodings
- All based on key-value pairs
	- The value is the "document" that provides the structure of the data
- Documents (values) can be embedded or nested in other documents
/Images/4_document_model.png
### Graph
- Stores and organizes data as nodes and relationships (called edges)
- Nodes
	- The entities in the graph
	- Can be tagged with labels that provide context and metadata
- Edges
	- Store the relationships between nodes
		- Parent/Child
		- Actions
		- Ownership
		- Etc
	- Each edge has
		- Direction
		- Type
		- Start and end node
	- There can be more than one edge between two nodes
- Useful for applications where there is a need to query the relationship between entities and their properties
	- E.g. social media
/Images/4_graph_example.png
### Key-Value Databases
- Uses a hash table to store unique keys along with pointers to corresponding data values 
- Key is usually a string of characters and the value is a series of uninterrupted bytes
- Value is opaque to the database
- Values do not have to be consistent data types
### Wide-Column/Columnar Store Database
- Organizes data as columns instead of rows
- Data stored in cells of columns and grouped into column families
	- Column families consist of multiple rows
- Enables quick data access using a row key, column name, and cell timestamp 
	- Timestamp uses Unix/Epoch time
	- Timestamps used to determine the most recent version of the data
- Columns are contained to their records and don't have to span the entire database
- Rows can contain different number of columns to other rows
/Images/4_columnar_example.png