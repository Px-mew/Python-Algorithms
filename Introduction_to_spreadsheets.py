"""
В таблице для каждого региона записаны зарплаты для разных профессий.
Программа выводит название региона с самой высокой медианной зарплатой (медианой называется элемент, стоящий в середине массива после его упорядочивания) и название профессии с самой высокой средней зарплатой по всем регионам.
"""

import xlrd3

wb = xlrd3.open_workbook('salaries.xlsx')
# Выбираем лист: получаем имя листа, и переходим к нему по имени
sheet_names = wb.sheet_names()
sh = wb.sheet_by_name(sheet_names[0])

#Получаем значение ячейки
salary_by_region = []
mx = 0
imx = 0
for row in range(1, 9):
    salary_by_region.append(sh.row_values(row)[1:8])
    salary_by_region[row-1].sort()
    if mx < salary_by_region[row-1][3]:
        mx = salary_by_region[row-1][3]
        imx = row
print("Регион с самой высокой медианной зарплатой - ", end='')
print(sh.row_values(imx)[0])


salary_by_profi = []
avg_mx = 0
for col in range(1, 8):
    salary_by_profi.append(sh.col_values(col)[0:9])

for i in range(0, 7):
    if sum(salary_by_profi[i][1:])/8 > avg_mx:
        avg_mx = sum(salary_by_profi[i][1:])/8
        avg_mx_profi = salary_by_profi[i][0]
print("Профессия с самой высокой средней зарплатой по всем регионам - ", end='')
print(avg_mx_profi)
