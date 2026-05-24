# Ушакова Кристина
# Дана целочисленная матрица размером n*m и число K. Написать программу,
# переставляющую строки и столбцы таким образом, чтобы максимальный по
# модулю элемент был расположен на пересечении K-й строки и K-го столбца

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
k = int(input("Введите k: "))

A = []
print("Введите матрицу:")
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

max_val = abs(A[0][0])
max_i = 0
max_j = 0

for i in range(n):
    for j in range(m):
        if abs(A[i][j]) > max_val:
            max_val = abs(A[i][j])
            max_i = i
            max_j = j

A[max_i], A[k - 1] = A[k - 1], A[max_i]

for i in range(n):
    A[i][max_j], A[i][k - 1] = A[i][k - 1], A[i][max_j]

print("Результирующая матрица:")
for row in A:
    print(row)
