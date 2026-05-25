# -*- coding: utf-8 -*-
#Недилько Полина ПИЗИ23о2
#Даны две действительные квадратные матрицы размером n*n. Получить новую матрицу умножением элементов каждой строки первой матрицы на наименьшее из значений элементов соответствующей строки второй матрицы  

def input_matrix(n, name):
    print(f"Введите элементы матрицы {name} ({n}x{n}):")
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            while True:
                try:
                    value = float(input(f"{name}[{i}][{j}] = "))
                    row.append(value)
                    break
                except ValueError:
                    print("Ошибка! Введите число.")
        matrix.append(row)
    return matrix


def print_matrix(matrix, name):
    print(f"\nМатрица {name}:")
    for row in matrix:
        for value in row:
            print(f"{value:10.2f}", end=" ")
        print()


def find_min_in_row(row):
    return min(row)


def get_new_matrix(matrix1, matrix2):
    n = len(matrix1)
    result = []
    
    for i in range(n):
        min_val = find_min_in_row(matrix2[i])
        new_row = [matrix1[i][j] * min_val for j in range(n)]
        result.append(new_row)
    
    return result


def main():
    print("=" * 50)
    print("Программа умножения элементов строк матрицы")
    print("=" * 50)
    
    while True:
        try:
            n = int(input("Введите размер матриц n (n x n): "))
            if n > 0:
                break
            else:
                print("Ошибка! Размер должен быть положительным числом.")
        except ValueError:
            print("Ошибка! Введите целое число.")
    
    matrix1 = input_matrix(n, "A")
    matrix2 = input_matrix(n, "B")
    
    print_matrix(matrix1, "A")
    print_matrix(matrix2, "B")
    
    result = get_new_matrix(matrix1, matrix2)
    
    print_matrix(result, "Результат")
    
    print("\nНаименьшие элементы строк матрицы B:")
    for i in range(n):
        min_val = find_min_in_row(matrix2[i])
        print(f"Строка {i}: {min_val:.2f}")


if __name__ == "__main__":
    main()

