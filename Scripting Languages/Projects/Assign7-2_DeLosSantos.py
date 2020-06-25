import pandas as pd
import numpy as np 

# Create ID as list
id = ['a','b','c','d','e','f','g','h','i','j']

# Create dictionary of name, score, attempts, and pass/fail

exam_data = {'name': ['Yuan', 'David', 'Margaret', 'Daniel', 'Gina', 'Catherine', 'Chris','Jaeki', 'Ethan', 'Murphy'],
            'score' : [12.5, 9, 16.5, None, 9, 20, 14.5, None, 8, 19],
            'attempt': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'pass/fail': ['Yes', 'No','Yes','No','No','Yes','Yes','No','No','Yes']
            }

# Pass dictionary into dataframe with ID as index
df_exam = pd.DataFrame(exam_data, index = id)

# Quick dataframe check
print(df_exam)

# Display rows 1,3,5,6 of 'name' and 'score' columns
df_exam.loc[['a','c','e','f'],['name','score']]

# Display rows where number of attempts is greater than 2
df_exam[df_exam['attempt'] > 2]

# Display rows where the score is missing
df_exam[df_exam.score.isnull()]

# Display rows where attempts > 2 AND score is missing
df_exam[(df_exam['attempt'] > 2) & (df_exam.score.isnull())]

# Append new record "k" to dataframe with given values for each column
df_exam.loc['k'] = ['Song', 15.5, 1, 'Yes']
df_exam

# Delete record "h" from dataframe 
df_exam.drop(['h'])

# Replace values yes/no in pass/fail column with pass/fail
df_exam['pass/fail'].replace({'Yes':'pass', 'No':'fail'}, inplace = True)
print(df_exam)