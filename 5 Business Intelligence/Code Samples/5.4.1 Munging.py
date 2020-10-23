#Example:  2.2.1 slide 4


import io
import pandas as pd
import requests as r

#variables needed for ease of file access
url = 'http://drd.ba.ttu.edu/isqs6339/ex/L2.2/'
file_1 = 'scifi_characters.csv'

#pull employment
res = r.get(url + file_1)
res.status_code
df = pd.read_csv(io.StringIO(res.text)) 

###############################################################################
#                     Data Munging                                            #
###############################################################################

#Many of these methods we have done in several other examples.  This example
#is to put them all in 1 place for your reference.

#Let's see the data
df

#Let's encode a column to categorize age.  Over 80 will be wise
#Otherwise gaining wisdom
df['Age_Category'] = 'Gaining Wisdom'
df['Age_Category'][df['Age'] > 80] = 'Wise'

#Let's caps all the last names
df['lname_upper'] = df['lname'].str.upper()
df

#Let's drop that column
df.drop('lname_upper', inplace=True, axis=1)
df

#Let's grab the first character of the last name
df['lname_1stchar'] = df['lname'].str[0]
df
df.drop('lname_1stchar', inplace=True, axis=1)

#Let's extract year from the date
#Note the datatype
df.dtypes

#Need to get it to datetime first, then extract
df['yr'] = pd.to_datetime(df['birthdate']).dt.year
df

#similar steps for any date operation