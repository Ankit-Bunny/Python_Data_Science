import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

print(df > 0)
print(df[df > 0])
print(df['W'] > 0)
print(df[df['W'] > 0])
print(df[df['Z'] < 0])
print(df[df['Z'] < 0][['X', 'Y']])

print(df[(df['W'] > 0) & (df['Y'] > 1)])

print(df.reset_index())

new_index = "CA NY WY OR CO".split()
df['States'] = new_index
print(df)
print(df.set_index('States'))
print(df)
