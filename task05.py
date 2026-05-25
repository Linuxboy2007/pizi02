# -*- coding: utf-8 -*-
"""
Грициненко Ярослав Андреевич ПИЗИ23о2 задание 5 
Дана действительная матрица размером n*m. Все элементы с наибольшим
значением заменить нулями (таких элементов может быть несколько)
"""

def replace_max_in_rows(matrix):
    for row in matrix:
        if not row:          
            continue
        max_val = max(row)   
        for i in range(len(row)):
            if row[i] == max_val:
                row[i] = 0.0
    return matrix

if __name__ == "__main__":
    try:
        n = int(input("Введите (n): "))
        m = int(input("Введите (m): "))

        matrix = []
        print("Введите элементы матрицы:")
        for i in range(n):
            row = list(map(float, input(f"Строка {i+1}: ").split()))
            if len(row) != m:
                print(f"В строке должно быть {m} элементов")
                exit(1)
            matrix.append(row)

        print("\nИсходная матрица:")
        for row in matrix:
            print(" ".join(f"{x:8.2f}" for x in row))

        replace_max_in_rows(matrix)
 
        print("\nМатрица после замены ")
        for row in matrix:
            print(" ".join(f"{x:8.2f}" for x in row))


