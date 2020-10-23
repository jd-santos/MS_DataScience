#Example:  2.1.2 slide 8


#reference examples from slide 4 and use apply
#use examples from 4370 missing values for group by analysis

import io
import pandas as pd
import requests as r

#variables needed for ease of file access
url = 'http://drd.ba.ttu.edu/isqs6339/ex/L2.1/'
file_1 = 'test_data.csv'

res = r.get(url + file_1)
res.status_code
df = pd.read_csv(io.StringIO(res.text)) 

###############################################################################
#                Let's look at our prior example of adding encoded fields     #
###############################################################################

#Recall this doesn't work
#for index, row in df.iterrows():
#    row['iterval'] = row['Ordinal_7pt'] + row['Ordinal_5pt'] + index

#Let's make a function

def ComputeVals(row):
    return row['Ordinal_7pt'] + row['Ordinal_5pt']


#Now, run the update using apply
df['encoded_likert'] = df.apply(ComputeVals, axis=1)
df


###############################################################################
#               Now let's look at doing a grouping                            #
###############################################################################


#Let's mean all columns by the Nominal value
df.groupby('Nominal').mean()

#Interesting, but let's do a bit more
#let's encode a high/low variable
df['7highlow'] = 'low'
#set the other value
df['7highlow'][df['Ordinal_7pt'] > 4] = 'high'

#Now, let's group by multiple values
df.groupby(['Nominal', '7highlow']).mean()


