
# import required libraries
import io
import os
import pandas as pd
import requests as r

# set variables for file access

# Store current absolute path of this file
path = os.path.abspath("cdc_svi_ETL.py")

# Retrieve file in current directory
cdc_csv = os.path.join(os.path.dirname(path), "SVI2018_US.csv")

# ----------Cleaning-----------------
# Store csv in dataframe
df_raw = pd.read_csv(cdc_csv)

#df_raw.head()

# Lots of columns so we'll output them to a list
#df_raw.columns.tolist()

# Data is conviently formatted with prefixes so we'll subset with those
# Include the description fields (state, state code, county names, etc)
df_sub1 = df_raw.loc[:, df_raw.columns.str.startswith(("ST", "CO", "LO", "EP", "E_HH", "E_HU", "E_TOT" ))]
df_sub1.info()

# Drop 1: EPL, this was subsetted above and we don't want it 
df_drop1 = df_sub1.drop(df_sub1.loc[:, df_sub1.columns.str.startswith("EPL")], axis = 1)

# Drop 2: Other attributes not in scope for this analysis 
df_drop2 = df_drop1.drop(df_drop1.loc[:, df_drop1.columns.str.endswith(("MINRTY", "LIMENG"))], axis = 1)

# Filter dataframe to just Texas
df_tx = df_drop2[df_drop2['ST_ABBR']=='TX']
df_tx.head(100)
df_tx.info()

# Export the column list since I can't copy/paste neatly out of VS Code
df_columnlist = pd.DataFrame(df_tx.columns.tolist())
df_columnlist['DataTypes'] = df_tx.dtypes.tolist()
df_columnlist.to_csv('CDC-SVI_Raw_Columns.csv', index = 0)

# --------- Grouping -----------
# Group by counties
# Sum E_ Prefixes
# Mean of EP (percentages)
df_final = df_tx \
    .groupby(['ST', 'STATE', 'ST_ABBR', 'STCNTY', 'COUNTY']).agg \
        (SumPop = ('E_TOTPOP', 'sum'),
        Sum_HU = ('E_HU', 'sum'),
        Sum_HH = ('E_HH', 'sum'),
        Mean_EP_POV = ('EP_POV', 'mean'),
        Mean_EP_UNEMP = ('EP_UNEMP', 'mean'),
        MEAN_EP_POV = ('EP_POV', 'mean'),
        MEAN_EP_UNEMP = ('EP_UNEMP', 'mean'),
        MEAN_EP_PCI = ('EP_PCI', 'mean'),
        MEAN_EP_NOHSDP = ('EP_NOHSDP', 'mean'),
        MEAN_EP_AGE65 = ('EP_AGE65', 'mean'),
        MEAN_EP_AGE17 = ('EP_AGE17', 'mean'),
        MEAN_EP_DISABL = ('EP_DISABL', 'mean'),
        MEAN_EP_SNGPNT = ('EP_SNGPNT', 'mean'),
        MEAN_EP_MUNIT = ('EP_MUNIT', 'mean'),
        MEAN_EP_MOBILE = ('EP_MOBILE', 'mean'),
        MEAN_EP_CROWD = ('EP_CROWD', 'mean'),
        MEAN_EP_NOVEH = ('EP_NOVEH', 'mean'),
        MEAN_EP_GROUPQ = ('EP_GROUPQ', 'mean'),
        MEAN_EP_UNINSUR = ('EP_UNINSUR', 'mean')
        ) 
 
 # Final output of rows = 254, the number of Texas counties!
df_final.head()
df_final.info()
