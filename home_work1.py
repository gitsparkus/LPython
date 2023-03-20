"""
Доработаем задачи 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
"""


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
        animal = cls.animals.get(animal_type, Animal)
        return animal(*args)


if __name__ == '__main__':
    fish = AnimalFactory.get_animal('Fish', 'Red', 'Fishname', 12)
    print(fish.get_color())
    bird = AnimalFactory.get_animal('Bird', True, 'BirdName', 7)
    print(bird)
    dog = AnimalFactory.get_animal('Dog', 40, 'DogName', 8)
    print(dog.get_height())
    other_animal = AnimalFactory.get_animal('Cat', 'Boris', 12)
    print(other_animal)
