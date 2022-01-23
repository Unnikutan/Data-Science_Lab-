import pandas as pd

df = pd.DataFrame({'Name': ['Unni','Ammu','Hari','Anna'],
                   'Age': [22,21,23,24],
                   'Rank': [10,1,,4,3]})

print(df)
print('SORTED DATAFRAME')
df = df.sort_values(by=['Name','Rank'], ascending=[True,True])
print(df)