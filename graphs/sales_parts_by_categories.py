import matplotlib.pyplot as plt
from main import category_sales, total_sales_amount

# plt.pie(category_sales.values, labels=category_sales.index, autopct="%1.1f%%")
# plt.title("Графік – Частка продажів за категоріями")
# plt.show()

plt.figure(figsize=(8, 8))
plt.pie(category_sales.values,
        labels=category_sales.index,
        autopct="%1.1f%%",
        startangle=90,
        pctdistance=0.8,
        wedgeprops={"width": 0.4})

plt.text(0,
         0,
         f"{total_sales_amount:,.0f}\nзагалом",
         ha="center",
         va="center",
         fontsize=16)

plt.title("Частка продажів за категоріями", fontsize=16)
plt.tight_layout()
plt.show()
