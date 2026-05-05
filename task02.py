# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 08:43:15 2026

@author: linux
"""
def multiply_matrices(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    row_products = [1] * n
    for i in range(n):
        prod = 1
        for k in range(n):
            prod *= B[i][k]
        row_products[i] = prod
    for j in range(n):
        for i in range(n):
            C[i][j] = A[i][j] + row_products[j]
    return C
n = int(input("Введите размер матриц n: "))
print("Введите первую матрицу A (через пробел, каждая строка с новой строки):")
A = []
for i in range(n):
    row = list(map(float, input().split()))
    A.append(row)
print("Введите вторую матрицу B (через пробел, каждая строка с новой строки):")
B = []
for i in range(n):
    row = list(map(float, input().split()))
    B.append(row)
C = multiply_matrices(A, B)
print("Результат:")
for row in C:
    for val in row:
        print(f"{val:8.2f}", end=" ")
    print()
