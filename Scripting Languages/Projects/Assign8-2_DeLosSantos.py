import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

# Capture state data as dataframe
d = {'State': ['CA','TX','FL','NY','IL','PA'],
    'Timezone': ['PST','CST','EST','EST','CST','EST'],
    'Population': [39250,27862,20612,19745,12801,12784],
    'Percentage': [.12,.09,.06,.06,.04,.04]
    }

# Convert to dataframe and display
df_states = pd.DataFrame(d)
df_states

# Sort the data by time zone and state, both in alphabetical order
df_states.sort_values(['Timezone', 'State'])
df_states

# Convert population to real population (thousands) and add as column
df_states['RealPopulation'] = df_states['Population'] * 1000
df_states

# Display the avg, min, and max values of populations of all six states
print(df_states['Population'].mean())
print(df_states['Population'].min())
print(df_states['Population'].max())

# Display the group sum of population for each time zone
df_states.groupby(['Timezone'])['Population'].agg('sum')

# Draw a bar plot to show populations
# The title is Population
# Y-axis is 'In Thousands', X-axis is 'State'
df_states.plot(kind = 'bar', x = 'State', y = 'Population')
plt.title = ('Population')
plt.ylabel = ('In Thousands')
plt.xlabel = ('State')
plt.show()

# Draw a pie chart of populations
plt.pie(df_states['Population'], labels = df_states['State'])