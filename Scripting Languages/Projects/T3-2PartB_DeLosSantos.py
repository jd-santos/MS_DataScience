import pandas as pd
import numpy as np 

# Import tips csv
tips = pd.read_csv('tips.csv')
df_tips = pd.DataFrame(tips)

# Display first six and last six observations
print(df_tips.head(6))
print(df_tips.tail(6))

# Compute tip percentage and add to dataframe
df_tips['tip_percentage'] = (df_tips['total_bill'] / df_tips['tip'])
df_tips.head(6)

# Group by day and smoker
group = df_tips.groupby(['day', 'smoker'])

# Print mean and standard deviation of tip percentage of each day/smoker group
group.tip_percentage.agg([np.mean, np.std])