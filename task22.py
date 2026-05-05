# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 08:43:15 2026

@author: linux
"""

def task22(mass: list[int], size: int) -> list[list[int]]:
    """
    Задан массив из целых чисел размером n и число L. Написать программу,
    формирующую из него матрицу, содержащую по L элементов в строке.
    Недостающие элементы заполнить нулями
    :param
        mass: list[int]
        size: int
    :return: list[list[int]]
    """

    answer = []

    while len(mass) > 0:
        row = []
        for j in range(size):
            if len(mass) == 0:
                row.append(0)
            else:
                row.append(mass.pop(0))

        if len(mass) == 0:
            answer.append(row)
            break
        answer.append(row)

    return answer
