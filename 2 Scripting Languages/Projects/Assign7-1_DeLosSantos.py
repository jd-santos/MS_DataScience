# Create dictionary from data 

import pandas as pd
import numpy as np 

emp_data = {'Department': ['Accounting', 'Accounting', 'Sales', 'Sales', 'Sales', 'Sales'],
            'Employee' : ['Margaret', 'Chris', 'Jaeki', 'Yuane','Nina','Lara'],
            'Salary': [120000, 87000, 43500, 60000, 55000, 73000]
            }
# Pass dictionary into dataframe
df_emp = pd.DataFrame(emp_data)

# Describe the Data
df_emp.describe()

# Sort by department, then salary, and dislay
df_emp = df_emp.sort_values(by=['Department', 'Salary'], ascending=[True, True])

# Print dataframe
print(df_emp)

# Classify range of salaries
salaryBin = [0, 50000, 60000, 150000]
salaryGroup = ['low', 'middle', 'high']

# Assign salaries to groups
group = pd.cut(df_emp['Salary'],salaryBin,labels = salaryGroup)
df_emp = df_emp.assign(salaryGroup = group)

# Get number of employees in each group
count_emp = pd.value_counts(df_emp['salaryGroup'])

# Print dataframe and number of employees in each group
print(df_emp, count_emp)

# Create new group of department and salary
dept_sal = df_emp.groupby(['Department', 'Salary'])

# Calculate mean of the salary in each department
dept_sal.agg(np.mean)