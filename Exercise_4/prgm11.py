import pandas as pd

details = {
    'cname' : ['Capgemini','Apple','TCS','Wipro','CTS'],
    'profit' : [24,25,-5,0,1],
}
df = pd.DataFrame(details)
df.loc[df.profit <= 0,'profit'] = False
df.loc[df.profit > 0,'profit'] = True
print(df)