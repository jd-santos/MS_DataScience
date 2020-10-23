import pandas as pd 
import numpy as np 

# Read in Olympic Athlete file
athlete = pd.read_csv('../Datasets/07_Athletes.csv')

# Read into dataframe
df_athlete = pd.DataFrame(athlete)

# Display the first 5 rows of data, including headers
# No need to pass argument, 5 is default :) 
df_athlete.head()

# Create a NumPy array 
arr_athlete = np.array(df_athlete)

# Show number of rows and columns in array
print("Number of rows: ", np.size(arr_athlete, 0))
print("Number of columns: ", np.size(arr_athlete, 1))

# Overwrite the year value of the first athlete (ID 1) with 1993
arr_athlete[0,4] = 1993

# Print just year to check value change
arr_athlete[:,4]

# Deduct 10 rom all athletes' weights
arr_athlete[:,3] = arr_athlete[:,3] - 10

# Show results
arr_athlete[:,3]

# Add new column to show ratio of weight to height of each athlete
# Append to arr_athlete
df_athlete['Ratio'] = (df_athlete['Weight'] / df_athlete['Height'])
df_athlete