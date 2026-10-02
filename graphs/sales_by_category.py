import matplotlib.pyplot as plt

from main import category_statistics

# plt.bar(category_statistics.index,category_statistics["total_sales"])
# plt.title("Графік – Продажі за категоріями")
# plt.xlabel("Категорія")
# plt.ylabel("Сума продажів")
# plt.show()

plt.figure(figsize=(9, 6))
bars = plt.bar(category_statistics.index,category_statistics["total_sales"])

plt.title("Продажі за категоріями", fontsize=16)
plt.xlabel("Категорія")
plt.ylabel("Сума продажів")
plt.grid(axis="y", linestyle="--", alpha=0.4)

for bar in bars:
    value = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2,
             value,
             f"{value:,.0f}",
             ha="center",
             va="bottom")
plt.tight_layout()
plt.show()
