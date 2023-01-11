import numpy as np
import pandas as pd

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)

print(df)

# drop the value on nan on row
print(df.dropna())
# drop the value on nan on column
print(df.dropna(axis=1))

# Keep only the rows with at least 2 non-NA values.
print(df.dropna(thresh=2))

print(df.fillna(value='Fill Value'))
print(df['A'].fillna(value=df['A'].mean()))




