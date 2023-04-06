"""
Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.
"""

import logging
import argparse

logging.basicConfig(level=logging.INFO, filename='Matrix.log', encoding='utf-8')
logger = logging.getLogger(__name__)


class MatrixSizeError(Exception):

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def __str__(self):
        error = f"Размеры матриц должны быть одинаковыми! Переданы матрицы с размерами {self.value1} и {self.value2}"
        logger.error(error)
        return error


class Matrix:

    def __init__(self, list_of_lists):
        if isinstance(list_of_lists, list) and sum({isinstance(x, list) for x in list_of_lists}):
            if len({len(x) for x in list_of_lists}) == 1:
                self.__matrix = list_of_lists
                logger.info(f'Создана матрица: \n{self}')
            else:
                error = "Размеры списков должны быть одинаковыми!"
                logger.error(error)
                raise ValueError(error)
        else:
            error = "Матрица должны быть списком списков"
            logger.error(error)
            raise ValueError(error)

    def __str__(self):
        return '\n'.join(['  '.join(map(str, x)) for x in self.__matrix])

    def __add__(self, other):
        if len(self.__matrix) != len(other.__matrix):
            raise MatrixSizeError(len(self.__matrix), len(other.__matrix))
        logger.info(f'Выполнено сложение матриц: \nМатрица1:\n{self}\nМатрица2:\n{other}')
        return Matrix(
            [list(map(lambda x, y: x + y, self.__matrix[i], other.__matrix[i])) for i in range(len(self.__matrix))])

    def __eq__(self, other):
        return str(self) == str(other)


def split_list(list_to_split, size):
    for i in range(0, len(list_to_split), size):
        yield list_to_split[i:i + size]


def parser_function():
    parser = argparse.ArgumentParser(description='Получение матрицы заданного размера из строки')
    parser.add_argument('--list')
    parser.add_argument('--size')
    if matrix_list := parser.parse_args().list:
        if matrix_size := int(parser.parse_args().size):
            int_list = [int(x) for x in matrix_list.split(',')]
            result = list(split_list(int_list, matrix_size))
            return result


if __name__ == '__main__':
    args = parser_function()
    matrix = Matrix(args)
    print(matrix+matrix)
    # matrix = Matrix([[1, 2], [3, 4]])
    # new_matrix = matrix + matrix
    # matrix1 = Matrix([[1, 2, 3], [3, 4, 7], [1,3,4]])
    # new_matrix = matrix + matrix1
    # print(matrix)
    # matrix2 = Matrix([[1, 2, 4], [3, 4]])
