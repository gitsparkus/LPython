"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для
проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод
отрицательных чисел и чисел больше 100 тысяч.
"""

MIN_NUMBER = 1
MAX_NUMBER = 100_000

number = int(input('Введите число:'))

is_prime = True

if number < MIN_NUMBER or number > MAX_NUMBER:
    print(f'Число должно быть не меньше {MIN_NUMBER} и не больше {MAX_NUMBER}')
else:
    if number == 1:
        is_prime = False
    else:
        for i in range(2, number):
            if (number % i) == 0:
                is_prime = False
                break

print(f"{number} - {'' if is_prime else 'не'} простое число")
