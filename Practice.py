import pandas as pd
pd.options.display.float_format= '{:.2f}'.format
pd.set_option('display.max_columns', 20, 'display.width', 500,'display.max_rows', 100)
df = pd.read_csv("50000 Sales Records.csv")
print(df)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
print(df.groupby('region')['total_profit'].sum()['Europe'])
#print("$",df.total_cost.sum())
#print(df.region.value_counts())
#print(df.region.unique())