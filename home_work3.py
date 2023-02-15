"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна
возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""

from fractions import Fraction

a = input('Введите первую дробь: ')

b = input('Введите вторую дробь: ')

numerator_a = int(a.split('/')[0])
denominator_a = int(a.split('/')[1])

numerator_b = int(b.split('/')[0])
denominator_b = int(b.split('/')[1])

a = Fraction(numerator_a, denominator_a)
b = Fraction(numerator_b, denominator_b)

sum_numerator_c = numerator_a * denominator_b + numerator_b * denominator_a
mult_numerator_c = numerator_a * numerator_b
denominator_c = denominator_a * denominator_b

print(f'Сумма: {sum_numerator_c}/{denominator_c} =', sum_numerator_c / denominator_c)
print(f'Проверка суммы: {a+b} = {float(a + b)}')
print(f'Произведение: {mult_numerator_c}/{denominator_c} =', mult_numerator_c / denominator_c)
print(f'Проверка произведения: {a*b} = {float(a * b)}')
