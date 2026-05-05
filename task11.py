# -*- coding: utf-8 -*-
import random
n = int(input("Введите количество строк n: "))
m = int(input("Введите количество столбцов m: "))
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        num = random.randint(0, 100)
        row.append(num)
    matrix.append(row)
print("\nМатрица:")
for row in matrix:
    for element in row:
        print(element, end = ' ')
    print()
sums = [] # начинаем считать суммы строк, в этот пустой список будем складывать суммы каждой строки
for row in matrix: # перебираем каждую строку матрицы, цикл выполнится столько раз, сколько строк я укажу
    sums.append(sum(row)) # складываем с помощью sum все числа из каждой строки и с помощью append добавляем результаты
min_sum = min(sums) # находим минимум
max_sum = max(sums) # находим максимум
min_index = sums.index(min_sum) + 1 # тут ищем на какой позиции(индекс) находится минимальный элемент в списке и результат сохраняем в перменную min_index (прибавила 1, чтобы начиналось не с 0, а с 1)
max_index = sums.index(max_sum) + 1 # тут ищем на какой позиции(индекс) находится максимальный элемент в списке и результат сохраняем в перменную max_index
print("\nСуммы строк: ", sums) # вывод результатов
print(f"Строка {min_index} имеет наименьшую сумму =  ", min_sum)
print(f"Строка {max_index} имеет наибольшую сумму =  ", max_sum)

