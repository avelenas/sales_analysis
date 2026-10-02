import pandas as pd

sales = pd.read_csv("sales.csv")
print("===== Виведіть в консоль перші 5 рядків =====")
print(sales.head())
print("\n===== Виведіть останні 5 рядків =====")
print(sales.tail())
print("\n===== Виведіть інформацію про таблицю за допомогою info() =====")
print(sales.info)
print("\n===== Виведіть статистичну інформацію за допомогою describe() =====")
print(sales.describe())

sales["total"] = sales["quantity"] * sales["price"]
sales["date"] = pd.to_datetime(sales["date"])

total_sales_quantity = sales["quantity"].sum()
total_sales_amount = sales["total"].sum()
average_sale = round(sales["total"].mean(), 2)
max_sale_amount = sales["total"].max()
min_sale_amount = sales["total"].min()

product_quantity = sales.groupby("product")["quantity"].sum()
biggest_quantity_sale = product_quantity.idxmax()

category_sales = sales.groupby("category")["total"].sum()
biggest_biggest_sale = category_sales.idxmax()

print("\nЗагальну кількість проданих товарів: ", total_sales_quantity)
print("Загальну суму продажів: ", total_sales_amount)
print("Середню суму одного продажу: ", average_sale)
print("Найдорожчий продаж (найбільше значення total): ", max_sale_amount)
print("Найдешевший продаж: ", min_sale_amount)
print("Товар із найбільшою кількістю проданих одиниць: ", biggest_quantity_sale)
print("Категорію з найбільшою сумою продажів: ", biggest_biggest_sale)

category_statistics = sales.groupby("category").agg(
    operations=("total", "count"),
    quantity=("quantity", "sum"),
    total_sales=("total", "sum"),
    average_sale=("total", "mean"))
category_statistics["average_sale"] = category_statistics["average_sale"].round(2)
print("\n",category_statistics)
