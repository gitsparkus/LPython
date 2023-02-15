"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию
hex используйте для проверки своего результата.
"""

hex_number = ''
number = int(input('Введите число: '))

print(f'Результат функции hex: {hex(number)}')
while number > 0:
    remainder = number % 16
    if remainder == 10:
        remainder = 'a'
    elif remainder == 11:
        remainder = 'b'
    elif remainder == 12:
        remainder = 'c'
    elif remainder == 13:
        remainder = 'd'
    elif remainder == 14:
        remainder = 'e'
    elif remainder == 15:
        remainder = 'f'

    hex_number = str(remainder) + hex_number
    number = number // 16

hex_number = '0x' + hex_number

print(f'Мой результат: {hex_number}')
