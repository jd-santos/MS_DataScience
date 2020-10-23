# Readme.md
```
Authors: Juan Coy (jucoy@ttu.edu), Jonathan De Los Santos (jonathan@jdsantos.com) 
Date: 10/08/20
Descr: file "Covid_Final_ETL" contains one support function, three ETL get functions, and a main function to execute the merge and export
```
## Function Overview
- Support function
	- divide_this(): divide, otherwise return 0
		- used for constructing the ratios in the health rankings data
- Get functions
	- `get_health_ranking_data()`
		- ETL function for health rankings
	- `get_texas_covid19_data()`
		- ETL function for Texas covid-19 data
	- `get_cdc_svi_data()`
		- ETL function for CDC Social Vulnerability Index (SVI)
- Main function `main()`
	- App entry point handling the merge and creation of final csv
	- Final CSV is named final_merged_datasets.csv and is saved to the same directory as the file
## Requirements
- Can be found in the Files and Paths section after library import
- CDC SVI Data
	- The CDC SVI data is a local CSV in the same directory as this python file
	- ==If the CSV name is changed from SVI2018.csv, update the argument to os.path.join==
- Python file name
	- The name of the python file is an input to finding the local csv and performing the final export
	- ==If file name is changed from "Covid_Final_ETL.py, update the argument to os.path.abspath==
## Misc
- This file uses `#region` and `#endregion` markers used by VS Code if they are supported by your IDE