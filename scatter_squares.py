"""Нанесение и оформление отдельных точек"""
import matplotlib.pyplot as plt
import matplotlib.cm

print(list(matplotlib.cm.cmap_d.keys()))

x_values = list(range(1, 1000, 15))
y_values = [x**2 for x in x_values]
# Использование цветовой карты cmap=plt.cm.Blues.

plt.scatter(x_values, y_values, c=y_values, cmap='PuRd', edgecolor='none', s=40)
# Назначение заголовка диаграммы и меток осей.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# Назначение диапазона для каждой оси.
plt.axis([0, 1100, 0, 1100000])
# Назначение размера шрифта делений на осях.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.colorbar()
plt.show()
# Автоматическое сохранение диаграмм. Первый аргумент - имя файла. Второй аргумент - отсекает от диаграммы лишние пропуски
# plt.savefig('squares_plot.png', bbox_inches='tight')
