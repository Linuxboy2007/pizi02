# -*- coding: utf-8 -*-
"""
Зенькова Александра Юрьевна, это Я!!!! Дана целочисленная квадратная матрица размером n*m. Написать программу,
формирующую два одномерных массива. В один переслать по строкам верхний
треугольник матрицы, включая элементы главной диагонали, в другой – нижний
треугольник. Полученные массивы распечатать
"""
def main():
    print("Введите размеры матрицы n и m:")
    n = int(input("n = "))
    m = int(input("m = "))

    if n != m:
        print("Матрица должна быть квадратной! n должно равняться m")
        return

    print(f"Введите элементы матрицы {n}x{n}:")
    matrix = []
    for i in range(n):
        row = []
        print(f"Введите {n} элементов {i + 1}-й строки через пробел:")
        elements = input().split()
        for j in range(n):
            row.append(int(elements[j]))
        matrix.append(row)

    print("\nИсходная матрица:")
    for i in range(n):
        for j in range(n):
            print(f"{matrix[i][j]:4d}", end="")
        print()

    upper = []
    for i in range(n):
        for j in range(i, n):
            upper.append(matrix[i][j])

    lower = []
    for i in range(n):
        for j in range(0, i):
            lower.append(matrix[i][j])

    print("\nВерхний треугольник (включая главную диагональ):")
    print(upper)

    print("\nНижний треугольник (без главной диагонали):")
    print(lower)

if __name__ == "__main__":
    main()
