n = int(input("Введите размер матрицы n: "))

print("Введите первую матрицу:")
A = []
for i in range(n):
    row = list(map(int, input().split()))
    A.append(row)

print("Введите вторую матрицу:")
B = []
for i in range(n):
    row = list(map(int, input().split()))
    B.append(row)

C = []

for i in range(n):
    min_value = min(B[i])

    new_row = []
    for j in range(n):
        new_row.append(A[i][j] * min_value)

    C.append(new_row)

print("Результирующая матрица:")
for row in C:
    print(row)