import matplotlib.pyplot as plt
from main import daily_sales

# plt.plot(daily_sales.index,daily_sales.values)
# plt.title("Графік – Динаміка продажів")
# plt.xlabel("Дата")
# plt.ylabel("Сума продажів")
# plt.grid()
# plt.show()

plt.figure(figsize=(11, 6))
plt.plot(daily_sales.index, daily_sales.values, marker="o", linewidth=2)
plt.title("Динаміка продажів", fontsize=16)
plt.xlabel("Дата")
plt.ylabel("Сума продажів")
plt.grid(True, linestyle="--", alpha=0.4)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
