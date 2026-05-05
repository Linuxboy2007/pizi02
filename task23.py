# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 08:43:15 2026

@author: linux
"""

n = int(input("Введите количество строк n: "))
m = int(input("Введите количество столбцов m (четное): "))

# Проверка, что m четное
if m % 2 != 0:
    print("Ошибка: m должно быть четным!")
    exit()

# Ввод матрицы
print("Введите матрицу построчно (элементы через пробел):")
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print("\nИсходная матрица:")
for row in matrix:
    print(*row)

# Меняем столбцы местами
for j in range(m // 2):
    for i in range(n):
        # Меняем j-й и (m-1-j)-й столбцы
        matrix[i][j], matrix[i][m - 1 - j] = matrix[i][m - 1 - j], matrix[i][j]

print("\nМатрица после обмена столбцов:")
for row in matrix:
    print(*row)
