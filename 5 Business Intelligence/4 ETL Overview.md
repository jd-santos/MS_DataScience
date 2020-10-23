# 4 ETL Definition and Overview
## Identifying Value
### IBM’s Stages of Information
- Data -> Information -> Knowledge -> Wisdom
- ETL is concerned with moving data to information
 /Images/4.1 IBM Value Triangle.png
 - Pre-processing, cleaning, format, normalize, filter, and sort level of data triangle 
 ### Value in the Data to Information Transition
 - What value does data have in this process?
	 - Metrics related to data
		 - Amount of cleaning, may be costly
	 - How compatible it is with other sources
	 - Availability of data
	 - Topic relevance
		 - Primary information area
			 - Directly related to our business
		 - Secondary information area 
			 - Distantly related
			 - May have some value but can also require more processing
 - Main question: does the effort likely generate viable value?
	 - Requires you to make an estimation
 - Benefits of good evaluation
	 - Expedited data availability
	 - Efficient usage of labor
		 - There’s too much data in the world
		 - You need to use dev time wisely
 - Detriments of bad evaluation
	 - Excessive time cleaning and massaging data
		 - Waste of labor
	 - Improper mapping
		 - Bad decisions based on poor data mapping (relationships)
	 - Know when to stop an ETL project
## Tools of ETL
### Basic ETL Framework
- Every tool has a paradigm and a nomenclature
- All ETL shares a common structure:
	- Logical flow level
		- Higher level
		- Defines the order in which individual data flows occur
			- Which flows runs and **when** 
	- Data flow level
		- Lowest level
		- Where...data flows :D 
			- Moves from one place to another
		- Sources and destinations are defined
### Custom vs. GUI Tools
- Custom tools
	- Most flexibility, least turnkey
	- Doing the same stuff as GUI tools but coding it yourself 
		- Python, C#, etc
- GUI based
	- Least flexible, but the most turnkey
	- Not really coding, mostly drag and drop
- Not uncommon to mix and match tools with some considerations:
	- Memory needs of the environment
		- Does it write to disk rather than in memory?
	- Format requirements
		- Can mean extra time and processing
	- What environments does my company have available? 
### Benefits and Detriments