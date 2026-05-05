# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 08:43:15 2026

@author: linux
"""

n = int(input("Введите размер матрицы n: "))

# Ввод матрицы
print("Введите матрицу построчно (элементы через пробел):")
matrix = []
for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

# Собираем элементы ниже главной диагонали
elements_below = []
for i in range(n):
    for j in range(i):
        elements_below.append(matrix[i][j])

# Если нет элементов ниже диагонали (n=1)
if not elements_below:
    max_below = float('-inf')
else:
    max_below = max(elements_below)

# Вычисляем сумму нужных элементов
sum_result = 0
found = False

for i in range(n):
    for j in range(i, n):  # главная диагональ и выше
        if matrix[i][j] > max_below:
            sum_result += matrix[i][j]
            found = True

# Вывод результата
if found:
    print(f"Сумма искомых элементов: {sum_result}")
else:
    print("Таких элементов нет")
