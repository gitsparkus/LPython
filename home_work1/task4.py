"""
Доработаем класс Архив из задачи 2
Добавьте методы представления экземпляра для программиста и для пользователя.

!!! Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
"""


class Archive:
    """Класс, сохраняющий архив старых значений при создании новых экземпляров. Доработаны методы представления."""

    instance = None
    counts = []
    texts = []

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        else:
            cls.instance.counts.append(cls.instance.count)
            cls.instance.texts.append(cls.instance.text)
        return cls.instance

    def __init__(self, count, text):
        self.count = count
        self.text = text

    def __str__(self):
        c = self.instance.counts if self.instance.counts else "Empty"
        t = self.instance.texts if self.instance.texts else "Empty"
        return f"Value: {self.instance.count}, text: {self.instance.text} " \
               f"value archive: {c}, text archive: {t}"

    def __repr__(self):
        return f"Archive({self.instance.count}, '{self.instance.text}')"


if __name__ == '__main__':
    d1 = Archive(1, 'a')
    print(d1.text, d1.texts)
    print(f'{d1}')
