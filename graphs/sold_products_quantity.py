import matplotlib.pyplot as plt
from main import product_quantity

# plt.bar(product_quantity.index,product_quantity.values)
# plt.title("Графік – Кількість проданих товарів")
# plt.xlabel("Товар")
# plt.ylabel("Кількість проданих одиниць")
# plt.show()

data = product_quantity.sort_values()
plt.figure(figsize=(9, 6))
bars = plt.barh(data.index,data.values)

plt.title("Кількість проданих товарів", fontsize=16)
plt.xlabel("Кількість")
plt.ylabel("Товар")
plt.grid(axis="x", linestyle="--", alpha=0.4)

for bar in bars:
    value = bar.get_width()
    plt.text(value,
             bar.get_y() + bar.get_height() / 2,
             f" {value}",
             va="center")
plt.tight_layout()
plt.show()
