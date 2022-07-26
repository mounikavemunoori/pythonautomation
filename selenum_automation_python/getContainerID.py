# Import the xlrd module
# import xlrd

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_excel('xlread.xlsx', sheet_name='Sheet1')

# print("Column headings:")
# print(df.columns)
# for i in df.index:
print(df['CONTAINER ID'][0])
