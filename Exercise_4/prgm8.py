import pandas as pd

details = {
    'Name' : ['A','B','C','D','E'],
    'Age' : [20,24,25,26,27],
}
df = pd.DataFrame(details)
print(df[:2])
