# Modules!
import io
import pandas as pd
import requests as r

# Store URL and files in variables to play nice with others
url = 'http://drd.ba.ttu.edu/isqs6339/hw/hw2/'
file_1 = 'players.csv'
file_2 = 'player_sessions.csv'
file_out1 = 'output1.csv'
file_out2 = 'output2.csv'
file_out3 = 'output3.csv'

# Get the players data, confirm with a status code
res = r.get(url + file_1)
res.status_code

# Repeat for player_sessions data
# Store in res2 
res2 = r.get(url + file_2)
res2.status_code

# Store both datasets in two different dataframes
df_players = pd.read_csv(io.StringIO(res.text)) 
df_session = pd.read_csv(io.StringIO(res2.text)) 

# Check our dataframes
df_players
df_session

# Fix delimiter on df_players so we get real columns
df_players = pd.read_csv(io.StringIO(res.text), delimiter='|')
df_players 

# Examine the sessions datatypes to ensure numeric data is numeric
df_session.dtypes
# Damage is a float, not sure if this will cause math issues later

# Do a count of each player in the session df
# Checking that playerids match players df
df_session['playerid'].value_counts()

# Join the tables
# Using a left join on players to be safe, but inner could be an option
df_merge = df_players.merge(df_session, how='left', on='playerid')
df_merge

# Check count of player_id and compare with session above
# We've got a match!
df_merge['playerid'].value_counts()

# Identify player names containing V and change their guild
# This was dangerous, but I couldn't crack pulling the str[0] and using it to replace
df_merge.loc[(df_merge['clan'].isnull()) & (df_merge['handle'].str.contains('v')), 'clan'] = 'LoD'

# Create performance metric with damaage and healing math
df_merge['player_performance_metric'] = ((df_merge['damage_done']*3.125)+(df_merge['healing_done']*4.815))/4
df_merge

# Encode dps quality with high/medium/low buckets
df_merge['dps_quality'] = 'Low'
df_merge['dps_quality'][(df_merge['damage_done'] >= 400000) & (df_merge['damage_done'] < 599999)] = 'Medium'
df_merge['dps_quality'][df_merge['damage_done'] >= 600000] = 'High'
df_merge

# Encode a column for player_dkp_gen_rate based on suspciously biased criteria
# Broken, couldn't figure out conditional in time
# Investigate fixing with lambda or np.where
df_merge['player_dkp_gen_rate'][(df_merge['dps_quality'] == 'High')] = (df_merge['player_performance_metric']*1.25)
df_merge['player_dkp_gen_rate']
df_merge['player_dkp_gen_rate']

# Write to CSV, include sep parameter for | delimiter 
# Avg damage and healing per session by clan
df_csv1 = df_merge.groupby(['clan', 'session', 'damage_done', 'healing_done']).mean()
df_csv1
df_csv1.to_csv(file_out1, sep='|', index=False)

#Avg damage and healing by position
df_csv2 = df_merge.groupby(['position', 'damage_done', 'healing_done']).mean()
df_csv2
df_csv2.to_csv(file_out2, sep='|', index=False)

# Output of all merged data sorted by player dkp gen rate
# Didn't complete the player dkp rate
df_csv3 = df_merge.sort_values(by=['player_dkp_gen_rate'], inplace=True, ascending=False)
df_csv3
df_csv3.to_csv(file_out3, sep='|', index=False)


# This data as is may be clean because there were no modifications representing drastic changes to the source
# However, some of the techniques like filling in Clan NANs based on containing a 'v' would not scale 

# I did some basic steps to ensure the value counts added up and nothing looked suspicious.
# A left join was used to ensure we would capture all of the players after checking that all players were 
# represented in the data.

# I would like to have checked that the player positions and damage/healing stats made sense
# For example, checking that dps or healers had damage and healing values that were in sensible ranges
# This would be difficult to test directly because there is no cutoff for being good at your position
# I've met a lot of healers who suspiciously don't heal and end up with high DPS
# Ranked player stats:

# Damage: Mindmelter
df_damage = df_merge.sort_values(by=['damage_done'], ascending=False)
df_damage

# Healing: Bakko
df_healzpls = df_merge.sort_values(by=['healing_done'], ascending=False)
df_healzpls

# Player Performance: Bakko
df_perform = df_merge.sort_values(by=['player_performance_metric'], ascending=False)
df_perform