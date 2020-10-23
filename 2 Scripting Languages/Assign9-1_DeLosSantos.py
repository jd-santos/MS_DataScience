import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

# Add salary info
dict_salary = {'Year': [2002, 2002, 2004, 2004, 2004, 2004, 2005, 2005],
                'Name': ['Tom', 'Joe','Tom', 'Joe','Tom', 'Joe','Tom', 'Joe'],
                'Salary': [54000,50000,56000,50000,58120,57100,58120,60300],
                'Interest Rate': [.1,.1,.15,.1,.16,.16,.16,.2]
                }
# Put info in dataframe
df_salary = pd.DataFrame(dict_salary, columns = ['Year', 'Name', 'Salary', 'Interest Rate'])

# Sort chronologically
df_salary.sort_values('Year', ascending = True)

# Describe the data
df_salary.describe()

# Add new column to indicate salary holding 
# Multily salary by interest rate and add 1500
df_salary['Holding'] = (df_salary['Salary'] * df_salary['Interest Rate'] + 1500)
df_salary

# Sum holding for each person
df_salary.groupby(['Name'])['Holding'].agg('sum')

# Draw a line plot that shows each person's holdings change
df_holding = df_salary.groupby(['Name'])['Holding']
df_holding.plot( x = 'Year', y = ['Joe', 'Tom'], legend = True, title = 'Holding Comparison')~