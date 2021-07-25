import pandas as pd

data = pd.read_csv('Positions_bluesurfincest_Page_2021_07_07.csv')

df = data.dropna(axis = 0, how = 'any')

print("Old df length:", len(data), "\nNew data frame length:", len(df), "\nNumber of rows with at least 1 NA value: ", (len(data)-len(df)))

df.to_csv('new_1.csv')

