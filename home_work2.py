"""
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей
на доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое
число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче
выше. Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""

from random import randint


def is_queens_under_attack(q1: tuple, q2: tuple) -> bool:
    """Функция проверяет находятся ли переданные ферзи под атакой друг друга"""

    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(coords: list) -> bool:
    """Функция проверяет есть ли в переданном списке координат ферзей такие, которые находятся под атакой друг друга"""
    copy_coords = coords.copy()

    if not coords:
        return False

    while len(copy_coords) > 1:
        queen_to_check = copy_coords.pop()

        for queen in copy_coords:
            if is_queens_under_attack(queen_to_check, queen):
                return False

    return True


def generate_queen():
    """Функция генерирует случайные координаты ферзя"""

    return randint(1, 8), randint(1, 8)


def generate_coords_list() -> list:
    """Функция гененрирует список координат для 8 ферзей, которые не могут атаковать друг друга"""

    result = []

    while len(result) < 8:
        result = []
        used = set()
        while len(result) < 8 and len(used) < 64:
            queen = generate_queen()
            used.add(queen)
            if queen not in result and check_queens([*result, queen]):
                result.append(queen)

    return result


if __name__ == '__main__':
    coordinates = [(1, 2), (4, 4), (5, 1), (8, 3), (6, 8), (2, 5), (3, 7), (7, 6)]

    print(check_queens(coordinates))

    for _ in range(4):
        print(generate_coords_list())
