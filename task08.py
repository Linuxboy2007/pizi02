'''
ПИЗИ2302
Издыбаева Алина Равильевна
Дана целочисленная квадратная матрица размером n*m. Написать программу, позволяющую исключать из нее столбец, в котором расположен минимальный элемент главной диагонали
'''
n = int(input("Введите размер квадратной матрицы n: "))

matrix = []
print("Введите элементы матрицы построчно (через пробел):")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

min_value = matrix[0][0]
col_index = 0

for i in range(1, n):
    if matrix[i][i] < min_value:
        min_value = matrix[i][i]
        col_index = i

new_matrix = []
for i in range(n):
    new_row = []
    for j in range(n):
        if j != col_index:
            new_row.append(matrix[i][j])
    new_matrix.append(new_row)

print("Минимальный элемент главной диагонали: {min_value} (находится в столбце {col_index})")
print("Матрица после удаления этого столбца:")
for row in new_matrix:
    print(*row)
