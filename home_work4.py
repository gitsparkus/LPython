"""
Создайте словарь со списком вещей для похода в качестве
ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную
грузоподъёмность. Достаточно вернуть один допустимый вариант.

*Верните все возможные варианты комплектации рюкзака.
"""

from itertools import combinations

items_dict = {
    'Фонарик': 200,
    'Нож': 100,
    'Карта': 40,
    'Открывашка': 50,
    'Ботинки': 500,
    'Носки': 20,
    'Спички': 13
}

max_weight = int(input('Введите максимальную грузоподъемность: '))

weight = max_weight

backpack = {}

for k, v in items_dict.items():
    if weight >= v:
        backpack[k] = v
        weight -= v

print(f'Первый вариант: {backpack}')

# Все варианты

print(f'Все варианты:')
for i in range(1, len(items_dict.items()) + 1):
    all_combinations = combinations(items_dict.items(), i)
    for combination in all_combinations:
        if sum((x[1] for x in combination)) <= max_weight:
            print(combination)
