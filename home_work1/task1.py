"""
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания (time.time)

!!! Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
"""

from time import time


class MyStr(str):
    """Расширенный класс строки, который хранит еще и автора строки."""

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time()
        return instance


if __name__ == '__main__':
    s = MyStr('Hello world!', 'student')
    print(s)
