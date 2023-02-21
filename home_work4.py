"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции. Дополнительно сохраняйте все
операции поступления и снятия средств в список.
"""


MUL = 50
PERCENT_OUT = 1.5
PERCENT_MIN = 30
PERCENT_MAX = 600
EVERY_COUNTER = 3
PERCENT_INCOME = 3
RICH = 5_000_000
PERCENT_RICH = 10


def get_menu_action():
    print('\n1. Пополнить')
    print('2. Снять')
    print('0. Выйти')
    return input('Что вы хотите сделать: ')




menu = None
balance = 0
counter = 1

while menu != '0':

    menu = get_menu_action()

    if menu in ('1', '2'):
        cash = int(input('Введите сумму: '))
        if balance >= RICH:
            balance *= 0.9

        if cash % MUL != 0:
            print(f'\033[93mСумма должна быть кратна {MUL}\033[0m\nБаланс: {balance}')
            continue

        if menu == '1':
            balance += cash

        if menu == '2':
            commission = cash * (PERCENT_OUT / 100)
            if commission < 30:
                commission = 30
            elif commission > 600:
                commission = 600
            if (cash + commission) <= balance:
                balance -= (cash + commission)
            else:
                print(f'\033[93mНедостаточно средств!\033[0m\nБаланс: {balance}')
                continue

        if counter == 3:
            balance += balance * (PERCENT_INCOME / 100)
            counter = 1
        else:
            counter += 1

    print(f'\nБаланс: {balance}')

print('Всего доброго!')