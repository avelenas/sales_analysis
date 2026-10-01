import pandas as pd

sales = pd.read_csv("sales.csv")
print(sales.head())
print(sales.tail())
print(sales.info)
print(sales.describe())