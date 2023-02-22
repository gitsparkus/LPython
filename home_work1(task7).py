"""
Задание №7
✔ Создайте функцию-генератор.
✔ Функция генерирует N простых чисел,
начиная с числа 2.
✔ Для проверки числа на простоту используйте
правило: «число является простым, если делится
нацело только на единицу и на себя».
"""


def get_prime(n: int):
    number = 2
    while n:
        is_prime = True
        for i in range(2, number):
            if (number % i) == 0:
                is_prime = False
                break
        if is_prime:
            n -= 1
            yield number
        number += 1


for x in get_prime(11):
    print(x)
