"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна
подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа
используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1_000

num = randint(LOWER_LIMIT, UPPER_LIMIT)

# print(num)

for i in range(10):
    n = int(input('Введите число: '))
    if n < num:
        print('Загаданное число больше')
    elif n > num:
        print('Загаданное число меньше')
    else:
        print('Вы победили!')
        break
else:
    print('Попытки кончились. Вы проиграли!')
