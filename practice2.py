import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open('50000 Sales Records.csv'):
    df = pd.read_csv("50000 Sales Records.csv")

    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    df.units_sold = df.units_sold.astype(float)
    grouped_by_region1 = df.groupby('region').sum()['units_sold']
    grouped_by_region2 = df.groupby('region').sum()['total_revenue']
    grouped_by_region1.plot(kind='bar', x='region', y='units_sold')
    grouped_by_region1.plot(kind='bar', x='region', y='total_revenue')



    fig,(ex1,ex2) = plt.subplots(1,2)
    ex1.pie(grouped_by_region1)
    ex2.pie(grouped_by_region2)
    plt.show()