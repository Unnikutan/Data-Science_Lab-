import pandas as pd

sr = pd.Series(pd.date_range('05-01-2021','05-12-2021',freq='D'))
print(sr.to_string(index=False))