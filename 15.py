n = int(input("Введите размер матрицы n: "))

print("Введите элементы матрицы:")
a = []
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)


max_diag = abs(a[0][0])
for i in range(1, n):
    if abs(a[i][i]) > max_diag:
        max_diag = abs(a[i][i])

print(f"\nМаксимальный диагональный элемент по модулю: {max_diag}")


for i in range(n):
    for j in range(0, n, 2):
        a[i][j] = a[i][j] / max_diag

print("\nРезультат:")
for i in range(n):
    for j in range(n):
        print(f"{a[i][j]:.2f}", end=" ")
    print()