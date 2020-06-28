import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create dataframe for city data
cities = {
    'CityA_High': [33,37,44,56,67,75,79,78,71,60,50,38],
    'CityA_Low': [19,22,28,38,47,57,62,60,53,42,35,24],
    'CityB_High': [54,59,67,76,83,91,93,94,84,75,63,55],
    'CityB_Low': [26,30,37,46,56,65,69,67,59,48,36,28]
    }

df_city = pd.DataFrame(cities, index = pd.date_range('2019-01-01','2019-12-31', freq = 'M'))

# Create DF for just City A
df_acity = df_city[['CityA_High', 'CityA_Low']].copy()

# Draw line plots for City A to display high and low temp change
df_acity.plot()

# Draw bar plots for City A to show the comparison of high and low temperature
df_acity.plot(kind = 'bar')

# Draw a scatter plot to show the correlation between both cities monthly high/low temps
df_city.plot(kind = 'scatter', x = ['CityA_High', 'CityA_Low'], y = ['CityB_High', 'CityB_Low'], style = ['r','b'])