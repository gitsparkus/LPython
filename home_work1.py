"""
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""

import sys


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
    if len(sys.argv) != 2:
        print('Ошибка! Должен быть передан один паратметр формата ДД.ММ.ГГГГ')
    else:
        date = sys.argv[1]
        print(check_date(date))
