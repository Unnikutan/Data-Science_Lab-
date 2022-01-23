import pandas as pd
data=pd.DataFrame({"Name":['Andrew','Bob','Raju','Raju','Vijay','Samuel'],
	'occupation':['Engineer','Doctor','Engineer','Doctor','Doctor','Engineer'],
	'Salary':[50000,56000,48000,45000,40000,50000]})
df=pd.DataFrame(data)
df
occ_average_age=df.groupby('occupation')
print(df['Salary'].mean())
occ_average_age.head(6)