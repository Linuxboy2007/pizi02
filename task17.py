# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 08:43:15 2026

@author: linux
"""

def task17(mass: list[list[int]]) -> list[list[int]]:
    """
    Задана целочисленная квадратная матрица размером n*n. Написать программу,
    преобразующую исходную матрицу по правилу: нечетные столбцы разделить на
    среднее значение внедиагональных элементов матрицы, а четные оставить без
    изменения.
    :param mass: list[list[int]]
    :return: list[list[int]]
    """
    sum_without_dg = 0

    for i in range(len(mass)):
        sum_without_dg += sum(mass[i]) - mass[i][i]

    average = sum_without_dg / (len(mass) * (len(mass)-1))

    for i in range(len(mass)):
        for j in range(len(mass[i])):
            if j % 2 == 1:
                mass[i][j] = mass[i][j]/average

    return mass
