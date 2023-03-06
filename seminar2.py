"""
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY и возвращает
истину, если дата может существовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999]. И весь период действует григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.
"""


def __is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)


def check_date(str_date: str):
    day, month, year = map(int, str_date.split('.'))
    if month not in range(1, 13) or day not in range(1, 32):
        return False

    if day == 31 and month not in (1, 3, 5, 7, 8, 10, 12):
        return False

    if month == 2:
        return day <= 28 + __is_leap_year(year)

    return True


if __name__ == '__main__':
    print(check_date('28.02.2005'))
    print(check_date('29.02.2005'))
    print(check_date('29.02.2004'))
