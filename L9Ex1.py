import pandas as pd
with open('50000 Sales Records.csv'):

    df = pd.read_csv("50000 Sales Records.csv")

    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    df.units_sold = df.units_sold.astype(float)
    pd.set_option('display.max_columns', 20, 'display.width', 500,'display.max_rows', 10, 'float_format', '{:,.2f}'.format)
    pd.options.display.float_format = '{:,.2f}'.format
    #print(df)
    List_of_Regions = df.region.unique()

    print (List_of_Regions)

    print("Total units sold", df.groupby('region')['units_sold'].sum())
    print("Total revenue", df.groupby('region')['total_revenue'].sum())

    print("Total units sold", df.units_sold.sum())
    print("Total revenue %.2f" %(df.total_revenue.sum()))
    print("Average revenue %.2f" %(df.total_revenue.sum()/df.units_sold.sum()))




#


#print("$",df.total_cost.sum())
#print(df.region.value_counts())
#print(df.region.unique())
