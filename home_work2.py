"""
Создайте класс Матрица. Добавьте методы для:
    вывода на печать,
    сравнения,
    сложения,
    *умножения матриц
"""


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
            raise ValueError("Размеры матриц должны быть одинаковыми!")
        return Matrix(
            [list(map(lambda x, y: x + y, self.__matrix[i], other.__matrix[i])) for i in range(len(self.__matrix))])

    def __eq__(self, other):
        return str(self) == str(other)


if __name__ == '__main__':
    list1 = [[1, 2], [3, -4]]
    list2 = [[5, 6], [7, 8]]

    matrix1 = Matrix(list1)
    matrix2 = Matrix(list2)

    matrix3 = matrix1 + matrix2

    matrix4 = Matrix(list1)

    print(matrix1, '\n')
    print(matrix2, '\n')
    print(matrix3)

    print(matrix1 == matrix2)

    print(matrix1 == matrix4)
