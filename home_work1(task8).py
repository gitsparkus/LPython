"""
Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""

var1 = ''
var1s = 's'
var2 = ''
var2s = 's'
s = 's'


def my_func():
    for var in globals():
        if var.endswith('s') and var != 's':
            code = compile(f'{var[:len(var) - 1]} = {var}', "<string>", "single")
            eval(code, globals())
            code = compile(f'{var} = None', "<string>", "single")
            eval(code, globals())


my_func()

print(var1, var1s, var2, var2s, s)
