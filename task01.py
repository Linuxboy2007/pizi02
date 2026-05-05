def main():
    print("Введите размеры матрицы n и m:")
    n = int(input("n = "))
    m = int(input("m = "))

    if n != m:
        print("Матрица должна быть квадратной! n должно равняться m")
        return


