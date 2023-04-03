"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним тесты.
2-5 тестов на задачу в трёх вариантах:
doctest,
unittest,
pytest.
"""

import pytest


class MatrixSizeError(Exception):

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __str__(self):
        return f"Размеры матриц должны быть одинаковыми! Переданы матрицы с размерами {self.value1} и {self.value2}"


class Matrix:

    def __init__(self, list_of_lists):
        if isinstance(list_of_lists, list) and sum({isinstance(x, list) for x in list_of_lists}):
            if len({len(x) for x in list_of_lists}) == 1:
                self.__matrix = list_of_lists
            else:
                raise ValueError("Размеры списков должны быть одинаковыми!")
        else:
            raise ValueError("Матрица должны быть списком списков")

    def __str__(self):
        return '\n'.join(['  '.join(map(str, x)) for x in self.__matrix])

    def __add__(self, other):
        if len(self.__matrix) != len(other.__matrix):
            raise MatrixSizeError(len(self.__matrix), len(other.__matrix))
        return Matrix(
            [list(map(lambda x, y: x + y, self.__matrix[i], other.__matrix[i])) for i in range(len(self.__matrix))])

    def __eq__(self, other):
        return str(self) == str(other)


def test_equal():
    assert Matrix([[1, 3]]) == Matrix([[1, 3]])


def test_raises_exception_on_size():
    with pytest.raises(ValueError):
        Matrix([[5, 6], [7]])


def test_str():
    assert str(Matrix([[4, 6], [7, 1]])) == '4  6\n7  1'


if __name__ == "__main__":
    pass
