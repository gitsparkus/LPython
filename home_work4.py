"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции. Дополнительно сохраняйте все
операции поступления и снятия средств в список.

Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег

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


def add_cash(transactions: list, cash: int):
    transactions.append(cash)
    return True


def get_cash(transactions: list, cash: int):
    commission = calc_commission(cash)
    if (cash + commission) <= get_balance(transactions):
        transactions.append(-1 * commission)
        transactions.append(-1 * cash)
        return True


def check_cash(cash: int, mul: int):
    if cash % mul != 0:
        return False
    return True


def calc_commission(cash: int):
    commission = cash * (PERCENT_OUT / 100)
    if commission < 30:
        return 30
    elif commission > 600:
        return 600
    return commission


def get_balance(transactions: list):
    return sum(transactions)


def chech_rich(transactions: list, rich: int, percent: int):
    balance = get_balance(transactions)
    if balance >= rich:
        transactions.append(balance * (-1 * percent / 100))


def calc_bonus(transactions: list, counter: int, percent: int):
    if counter == 3:
        transactions.append(get_balance(transactions) * (percent / 100))
        return 1
    else:
        return counter + 1


if __name__ == '__main__':

    menu = None
    counter = 1
    transactions = []

    while menu != '0':

        print(f'\nБаланс: {get_balance(transactions)}')
        menu = get_menu_action()

        if menu in ('1', '2'):
            cash = int(input('Введите сумму: '))

            chech_rich(transactions, RICH, PERCENT_RICH)

            if check_cash(cash, MUL):
                if menu == '1':
                    add_cash(transactions, cash)

                if menu == '2':
                    if not get_cash(transactions, cash):
                        print(f'\033[93mНедостаточно средств!\033[0m')
                        continue

                counter = calc_bonus(transactions, counter, PERCENT_INCOME)
            else:
                print(f'\033[93mСумма должна быть кратна {MUL}\033[0m')

    print(f'Все операции: {transactions}')
    print('Всего доброго!')
