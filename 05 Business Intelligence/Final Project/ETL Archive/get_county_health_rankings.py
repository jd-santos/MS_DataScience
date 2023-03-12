"""
    Author:     jucoy@ttu.edu
    Date:       9/30/2020
    Descr:      Retrieve latest version of US County Health Rankings from source.
"""
# import required libraries
import io
import numpy as np
import pandas as pd
import requests as r

# define mainline logic function
def main():
    # instantiate local variables
    remote_infile = 'https://www.countyhealthrankings.org/sites/default/files/media/document/analytic_data2020_0.csv'
    outfile_texas_health_ranking_data = 'outfile_texas_health_ranking_data.csv'

    try:

        # retrieve remote csv file
        res = r.get(remote_infile)
        res.status_code

        # create DataFrame from request
        df = pd.read_csv(io.StringIO(res.text), error_bad_lines=False, index_col=False, low_memory=False)

        # sub-setting
        texas_df = df[(df['State Abbreviation'].str.upper() == 'TX')]

        # slice only columns I need for our analysis
        # analyze the data
        # clean it

        # write Texas specific data to outfile.
        texas_df.to_csv(outfile_texas_health_ranking_data, index=False)

    except Exception as ex:
        # display error for user
        print(type(ex).__name__, ':', ex)


# app entry point
main()
