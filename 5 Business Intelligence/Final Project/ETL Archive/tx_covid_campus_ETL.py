
# import required libraries
import io
import os
import pandas as pd
import requests as r

# set variables for file access

# Store absolute path of this file
path = os.path.abspath("tx_covid_campus_ETL.py")

# Retrieve file in current directory
tx_csv = os.path.join(os.path.dirname(path), "tx_covid_campus_ETL.py")

# Store csv in dataframe
df = pd.read_csv(tx_csv)
