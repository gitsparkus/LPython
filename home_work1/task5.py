"""
Дорабатываем класс прямоугольника из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр прямоугольника
Складываем и вычитаем периметры, а не длину и ширину.
При вычитании не допускайте отрицательных значений.

!!! Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
"""


class Rectangle:
    """Класс прямоугольник. Умеет считать площидь и периметр прямоугольника, складывать и вычетать прямоугольники."""

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


if __name__ == '__main__':
    r1 = Rectangle(2)
    print(r1.perimeter())
    r2 = Rectangle(4, 5)
    print(r2.perimeter())
    r3 = r2 - r1
    print(f'{r1 = }')
    print(f'{r3 = }')
    print(r3.perimeter())
    print(r3.width, r3.length)
