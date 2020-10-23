# Pandas Cheatsheet
### Rename Axis/Axes
`DataFrame.rename(args)`
E.g. `df_tx.rename(columns={'E_TOTPOP': 'TOTPOP', 'E_HH': 'Households', 'E_HU': 'Housing_Units'}, errors='raise')`
- Renamed three column indexes, raise errors if there are mismatches 

### Groupby Multiple Columms with Sum and Mean
[Source](https://stackoverflow.com/questions/48909110/python-pandas-mean-and-sum-groupby-on-different-columns-at-the-same-time)
You need agg by dictionary and then rename columns names:
```
d = {'Missed':'Sum1', 'Credit':'Sum2','Grade':'Average'}
df=df.groupby('Name').agg({'Missed':'sum', 'Credit':'sum','Grade':'mean'}).rename(columns=d)
print (df)
```
      Sum1  Sum2  Average
Name                     
A        2     4       11
B        3     5       15

If want also create column from Name:
```
df = (df.groupby('Name', as_index=False)
       .agg({'Missed':'sum', 'Credit':'sum','Grade':'mean'})
       .rename(columns={'Missed':'Sum1', 'Credit':'Sum2','Grade':'Average'}))
print (df)
```
Name  Sum1  Sum2  Average
0    A     2     4       11
1    B     3     5       15

Solution with named aggregations:
```
df = df.groupby('Name', as_index=False).agg \ 
								(Sum1=('Missed','sum'), 
								Sum2= ('Credit','sum'),
								Average=('Grade','mean'))
print(df)
```
  Name  Sum1  Sum2  Average
0    A     2     4       11
1    B     3     5       15
