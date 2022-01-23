import pandas as pd
import numpy as np

data = {'Set_of_Numbers': [2, 3, 5,np.nan, 13, np.nan, 17]}
df = pd.DataFrame(nums)
df = df.fillna(0)
print(df)