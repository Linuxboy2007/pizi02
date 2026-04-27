

def replace_min_with_zeros(matrix):
    """
    Задана действительная матрица размером n*m. Написать программу,
    позволяющую заменить все элементы, наименьшие в строке, на нули
    :param matrix:
    :return:
    """

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            mini = min(matrix[i])

            if matrix[i][j] == mini:
                matrix[i][j] = 0

    return matrix


def matrix_print(mass: list[list[int]]):
    """"""

    for i in mass:
        print(', '.join(list(map(str, i))))


matrix_print(replace_min_with_zeros([
    [1, 2, 3],
    [4, 5, 6]
]))