import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)
# selecting columns
print(df['W'])
print(df[['W', 'Z']])
df['new'] = df['W'] + df['Y']
print(df)
print(df.drop('new', axis=1))
print(df)
# call inplace=True if you want the change is to be permanent
df.drop('new', axis=1, inplace=True)
print(df)
print(df.drop('E', axis=0))
print(df)
# df.drop('E', axis=0, inplace=True)
# print(df)

print(df.shape)
# selecting rows
# by calling level name
print(df.loc['A'])
# by calling index position
print(df.iloc[2])
# selecting subset of rows and columns
print(df.loc['B', 'Y'])
print(df.loc[['A', 'B'], ['W', 'Y']])


