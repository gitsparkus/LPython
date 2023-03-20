"""
Добавьте к задачам 1 и 2 строки документации для классов

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


class Archive:  # noqa
    """Класс, сохраняющий архив старых значений при создании новых экземпляров."""

    instance = None
    count_archive = []
    text_archive = []

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        else:
            cls.instance.count_archive.append(cls.instance.count)
            cls.instance.text_archive.append(cls.instance.text)
        return cls.instance

    def __init__(self, count, text):
        self.count = count
        self.text = text


if __name__ == '__main__':
    help(MyStr)
    help(Archive)
