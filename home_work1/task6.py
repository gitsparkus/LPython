"""
Доработайте прошлую задачу.
Добавьте сравнение прямоугольников по площади
Должны работать все шесть операций сравнения

!!! Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
"""


class Rectangle:
    """
    Класс прямоугольник. Умеет считать площидь и периметр прямоугольника, складывать, вычетать и сравнивать
    прямоугольники,
    """

    def __init__(self, length, width=None):
        self.length = length
        self.width = length if width is None else width

    def area(self):
        """Метод получения площиди прямоугольника"""

        return self.width * self.length

    def perimeter(self):
        """Метод получения периметра прямоугольника"""

        return 2 * (self.width + self.length)

    def __add__(self, other):
        new_perimeter = self.perimeter() + other.perimeter()
        new_width = self.width + other.width
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_width, new_length)

    def __sub__(self, other):
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_width = abs(self.width - other.width)
        new_length = new_perimeter / 2 - new_width
        return Rectangle(new_width, new_length)

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()


if __name__ == '__main__':
    r1 = Rectangle(4, 12)
    r2 = Rectangle(4, 3)
    print(r2 < r1)
