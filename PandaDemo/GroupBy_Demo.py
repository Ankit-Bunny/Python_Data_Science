import pandas as pd

# Create dataframe
data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}
df = pd.DataFrame(data)
print(df)

by_company = df.groupby('Company')
print(by_company.mean())
print(by_company.sum())
print(by_company.std())
print(by_company.sum().loc['FB'])
print(df.groupby('Company').sum().loc['FB'])
print(df.groupby('Company').count())
print(df.groupby('Company').max())
print(df.groupby('Company').min())
print(df.groupby('Company').describe())
print(df.groupby('Company').describe().transpose())
print(df.groupby('Company').describe().transpose()['FB'])


