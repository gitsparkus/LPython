"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода.
Например нельзя создавать прямоугольник со сторонами отрицательной длины.
"""


class Rectangle:
    """Класс прямоугольник. Умеет считать площидь и периметр прямоугольника, складывать и вычетать прямоугольники."""

    def __init__(self, length, width=None):
        if length <= 0:
            raise ValueError(f'Длина прямоугольника не может быть меньше или равна 0! Передано значение: {length}')
        if width and width <= 0:
            raise ValueError(f'Ширина прямоугольника не может быть меньше или равна 0! Передано значение: {width}')

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

    def __str__(self):
        return f"Длина: {self.length}\nШирина: {self.width} "

    def __repr__(self):
        return f'{type(self).__name__}({self.length}, {self.width})'


if __name__ == '__main__':
    r1 = Rectangle(2)
    print(r1.perimeter())
    r2 = Rectangle(4, -5)
    print(r2.perimeter())
    r3 = r2 - r1
    print(f'{r1 = }')
    print(f'{r3 = }')
    print(r3.perimeter())
    print(r3.width, r3.length)

    print(f'{r3}')
    print(f'{r3=}')
