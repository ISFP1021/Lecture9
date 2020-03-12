import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
    print("\n\n\nTotal revenue ", end="")
    print(f"{df.total_revenue.sum():,.0f}")


    print("\n\n\nTotal units sold ", end="")
    print(f"{df.units_sold.sum():,.0f}")

    print("Total revenue ", end="")
    print(f"${df.total_revenue.sum():,.2f}")
    print("Average revenue $%.2f" %(df.total_revenue.sum()/df.units_sold.sum()))

grouped_by_region1 = df.groupby('region').sum()['units_sold']
grouped_by_region2 = df.groupby('region').sum()['total_revenue']
grouped_by_region1.plot(kind='bar', x='region', y='units_sold')

plt.xlabel('Region')
plt.ylabel('Units Sold')
plt.title('Units Sold per Region')
plt.axis([0, 7, 0, 66000000])
plt.bar(np.arange(len(grouped_by_region1), grouped_by_region1, width=width))
plt.bar(np.arange(len(grouped_by_region2))+ width, grouped_by_region2, width=width)
plt.show()
# or plt.savefig("name.png")
#grouped_by_region.plot(kind='pie', x='region', y='units_sold')
#plt.show()
# or plt.savefig("name.png")
#grouped_by_region = df.groupby('region').sum()['total_revenue']
#grouped_by_region.plot(kind='bar', x='region', y='total_revenue')
#plt.show()
# or plt.savefig("name.png")
#grouped_by_region.plot(kind='pie', x='region', y='total_revenue')
#plt.show()

#


#print("$",df.total_cost.sum())
#print(df.region.value_counts())
#print(df.region.unique())
