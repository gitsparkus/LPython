"""
Напишите функцию для транспонирования матрицы
"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# 1 2 3
# 4 5 6
# 7 8 9
#
# 1 4 7
# 2 5 8
# 3 6 9


def transponse(matrix_to_transponse: list) -> list:
    return list(zip(*matrix_to_transponse))


for row in matrix:
    print(row)

print()

for row in transponse(matrix):
    print(row)
