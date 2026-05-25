# -*- coding: utf-8 -*-
# Батыркин Никита Владимирович ПИЗИ23о2
# Дана действительная матрица размером n*m, все элементы которой различны. В каждой строке выбирается элемент с наибольшим значением, затем среди этих чисел выбирается наибольшее. Указать индексы элемента с найденным значением
def find_max(matrix):
    max_value = matrix[0][0]
    row_index = 0
    col_index = 0

    for i in range(len(matrix)):

        row_max = max(matrix[i])
        j = matrix[i].index(row_max)

        if row_max > max_value:
            max_value = row_max
            row_index = i
            col_index = j

    return max_value, row_index, col_index


n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

matrix = []

for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

value, row, col = find_max(matrix)

print("Наибольший элемент:", value)
print("Индексы:", row, col)
