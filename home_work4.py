"""
✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""


def fibonacci_numbers(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    print(list(fibonacci_numbers(12)))
