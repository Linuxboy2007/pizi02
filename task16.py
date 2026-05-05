# Репина задача 16 изменена
# 16.Задана целочисленная квадратная матрица размером n*n. Написать программу,
# преобразующую исходную матрицу по правилу: четные столбцы разделить на
# среднее значение диагональных элементов матрицы, а нечетные разделить на
# минимальное значение диагональных элементов матрицы.

matrix = [[1,2,3],
         [4,5,6],
         [7,8,9]]
diagonal = [matrix[i][i] for i in range (len(matrix))]
trace = sum(diagonal)
value = trace / len(matrix)
for i in range(len(matrix)):
    if i % 2 == 0:
        matrix[i] = [x / value for x in matrix[i]]

print('Диагональные элементы:', diagonal)
print('Сумма диаг эл', trace)
print('Преобразованная матрица')
for row in matrix:
    print(row)
