import pandas as pd
from sqlalchemy import create_engine

"""

# Reading and writing Data Frames from csv and excel file from panda 
df = pd.read_csv('example')
print(df)

df.to_csv('My_output', index=False)

print(pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1'))

df.to_excel('Excel_Sample2_Output.xlsx', sheet_name='New')

"""
"""
# Reading from html sources 
df = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/')
print(type(df))
print(df[0].head())
"""

df = pd.read_csv('example')
print(df)
engine = create_engine('sqlite:///:memory:')

df.to_sql('data', engine)

sql_df = pd.read_sql('data', con=engine)
print(sql_df)
