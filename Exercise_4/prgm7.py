import pandas as pd

data = {'Name': ['Shiyas','Unni','Sha'],
                   'Age': [21,22,25],
                   'Rank': [40,50,60]}

index = {'a', 'b','c'}
df = pd.DataFrame(data,index)
print(df)
df.reset_index(inplace = True, drop = True)
print('Default Index')
print(df)