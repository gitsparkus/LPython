"""
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов
list-архивы так же являются свойствами экземпляра.

!!! Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
"""


class Archive:
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
    d1 = Archive(1, 'a')
    print(d1.text, d1.text_archive)
    d2 = Archive(2, 'b')
    print(d2.text, d2.text_archive)
    d3 = Archive(3, 'c')
    print(d3.text, d3.text_archive)
