"""
Нарисовать в консоли ёлку спросив у пользователя количество
рядов.
Пример результата:
Сколько рядов у ёлки? 5
    *
   ***
  *****
 *******
*********
"""

rows = int(input('Сколько рядов у ёлки?'))

for i in range(1, rows + 1):
    starts_qty = i * 2 - 1
    space_qty = rows - starts_qty // 2

    print(f"{' ' * space_qty}{starts_qty * '*'}")

