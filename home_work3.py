"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода.
Например нельзя создавать прямоугольник со сторонами отрицательной длины.
"""


class WrongAnimalTypeError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Фабрика не умеет создавать животных с типом '{self.value}'"


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_unique(self):
        pass


class Fish(Animal):
    def __init__(self, color, *args):
        self.color = color
        super().__init__(*args)

    def get_color(self):
        return f'Цвет рыбы {self.name} - {self.color}'


class Bird(Animal):
    def __init__(self, is_flies, name, age):
        self.is_flies = is_flies
        super().__init__(name, age)

    def can_flies(self):
        return f"The bird {self.name} flies? {self.is_flies}!"

    def __str__(self):
        spam = 'летает' if self.is_flies else 'ходит'
        return f'Перед нами птица по имени {self.name}. Ей {self.age} лет. Эта птица {spam}'


class Dog(Animal):
    def __init__(self, height, *args):
        self.height = height
        super().__init__(*args)

    def get_height(self):
        if self.height < 0.5:
            return f'{self.name} маленький собачонок'
        elif 0.5 < self.height < 1:
            return f'{self.name} средний собачонок'
        else:
            return f'{self.name} огромный пёс'


class AnimalFactory:
    animals = {
        'Fish': Fish,
        'Bird': Bird,
        'Dog': Dog
    }

    @classmethod
    def get_animal(cls, animal_type, *args):
        if animal := cls.animals.get(animal_type, None):
            return animal(*args)
        else:
            raise WrongAnimalTypeError(animal_type)


if __name__ == '__main__':
    fish = AnimalFactory.get_animal('Fish', 'Red', 'Fishname', 12)
    print(fish.get_color())
    bird = AnimalFactory.get_animal('Bird', True, 'BirdName', 7)
    print(bird)
    dog = AnimalFactory.get_animal('Dog', 40, 'DogName', 8)
    print(dog.get_height())
    other_animal = AnimalFactory.get_animal('Cat', 'Boris', 12)
    print(other_animal)
