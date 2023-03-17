"""
Напишите следующие функции:
    Нахождение корней квадратного уравнения
    Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
    Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
    Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
"""

import math
from pathlib import Path
from random import randint
import csv
import json


def process_csv(func):
    """Декоратор выводит результат решения для a,b,c, если они переданы. В противном случае обрабатывает csv-файл"""

    def wrapper(*args):
        if args:
            return func(*args)
        with open('csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for item in reader:
                if item:
                    a, b, c = map(float, item)
                yield func(a, b, c)

    return wrapper


def logging(func):
    """Логирование переданных параметров и результатов в файл"""

    def wrapper(*args):
        file_name = ','.join(map(str, args)) + '.json'
        result = func(*args)
        result_dict = {file_name: result}
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(result_dict, f)

        return result

    return wrapper


@process_csv
@logging
def quadratic(a: float, b: float, c: float):
    """Функция решает квадратное уравнение"""

    d = b ** 2 - 4 * a * c

    if d > 0:
        if a != 0:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            return x1, x2
        elif b != 0:
            return -c / b
        return None
    elif d == 0:
        x = -b / (2 * a)
        return x

    return None


def generate_csv(path: Path):
    """Функция генерирует csv-файл"""

    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for _ in range(randint(100, 1000)):
            a = randint(-1000, 1000)
            b = randint(-1000, 1000)
            c = randint(-1000, 1000)
            writer.writerow([a, b, c])


if __name__ == '__main__':
    generate_csv(Path('csv'))

    print("Введите коэффициенты для уравнения")
    print("ax^2 + bx + c = 0:")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    print(quadratic(a, b, c))

    for i in quadratic():
        print(i)
