#Example:  2.2.2 slide 5

import io
import pandas as pd
import requests as r

#variables needed for ease of file access
url = 'http://drd.ba.ttu.edu/isqs6339/ex/L2.2/'
file_1 = 'employment.csv'
file_2 = 'job_title.csv'
file_3 = 'job_title_year.csv'

#pull employment
res = r.get(url + file_1)
res.status_code
df_emp = pd.read_csv(io.StringIO(res.text)) 

#pull job
res = r.get(url + file_2)
res.status_code
df_job = pd.read_csv(io.StringIO(res.text)) 


###############################################################################
#                  Let's inspect the dataset with replace val                 #
###############################################################################

#Let's look at our dataset....seems resonable
df_emp.head()

#Let's look at the count
#Note the odd/different values
df_emp.count()

#How to fix salary......suggestions?
#These will be basic options.  Note, you can always use the apply
#function to update the values using more robust methods found in
#your other stats classes.

#Identify the "not" nas....
df_emp[df_emp['salary'].notna()]

#how about the nas
df_emp[df_emp['salary'].isnull()]

#Let's fill in with 0's
df_emp['salary'].fillna(0, inplace=True)
df_emp.count()

#That is great, but we have other info to derive an average
#recall we have average salary in job file.
#reset our dataframe
res = r.get(url + file_1)
res.status_code
df_emp = pd.read_csv(io.StringIO(res.text)) 

#Let's populate via the average
#bit brute force, but gets the job done
for index, row in df_job.iterrows():
        df_emp['salary'][(df_emp['jobtitleid'] == row['jobtitleid']) & (df_emp['salary'].isnull())] = row['avg_salary']

df_emp.count()

#Let's look at a slightly nicer way of doing what we just did.

#reset the dataframe
res = r.get(url + file_1)
res.status_code
df_emp = pd.read_csv(io.StringIO(res.text)) 

for index, row in df_emp.iterrows():
    if pd.isna(df_emp.at[index, 'salary']):
        df_emp.at[index, 'salary'] = df_job['avg_salary'][df_job['jobtitleid']==row['jobtitleid']]

#What is the major difference between the last 2 blocks of code.  
#How are they operating differently?

###############################################################################
#                            Join Issues                                      #
###############################################################################

#Let's join our files
dfmerged = df_emp.merge(df_job, how='inner', on='jobtitleid')
dfmerged.head()

#let's look at count
dfmerged.count()
#where are our rows???? 80 vs 99.  note our join type
dfmerged = df_emp.merge(df_job, how='left', on='jobtitleid')
dfmerged.count()

#so what happened?
#Let's update with an "other" option.  0 for average age and salary
dfmergedcln = dfmerged.fillna({'jobtitleid' : -1, 'jobtitle':'other', 'avg_salary':0, 'avg_age':0})
dfmergedcln.count()

#Note, the prior example has us update values "hardcoded"
#in practice, it may be better to add that row to the job file,
#add our 'dummy' job titleid to our file
#then remerge.  It may save potential errors in keying in data.