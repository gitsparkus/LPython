"""
Создайте класс студента.
Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
"""
import csv

MIN_MARK = 2
MAX_MARK = 5
MIN_TEST_MARK = 0
MAX_TEST_MARK = 100


class NameDescriptor:
    def __init__(self):
        self.__name = ''

    def __get__(self, instance, owner):
        return self.__name

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Фамилия, Имя и Отчетсво могут быть только строками!")
        if not value.isalpha():
            raise ValueError("В Фамилии, Имени и Отчестве могут быть только буквы!")
        if not value.istitle():
            raise ValueError("Фамилия, Имя и Отчество должны начинаться с большой буквы!")
        self.__name = value

    def __delete__(self, instance):
        del self.__name


class Student:
    name = NameDescriptor()
    surname = NameDescriptor()
    patronymic = NameDescriptor()

    def __init__(self, name, surname, patronymic, subject_file):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

        with open(subject_file, 'r', encoding='utf-8') as f:
            self.__subjects_dict = {x[0]: {'marks': list(), 'testMarks': list()} for x in csv.reader(f)}
            self.__subjects = tuple(self.__subjects_dict.keys())

    @property
    def subjects(self):
        return self.__subjects

    def add_mark(self, subject, mark):
        if subject in self.subjects:
            if MIN_MARK <= mark <= MAX_MARK:
                self.__subjects_dict[subject]['marks'].append(mark)
            else:
                raise ValueError(f'Оценка должна быть больше {MIN_MARK} и меньше {MAX_MARK}!')
        else:
            raise ValueError(f'Нет предмета {subject}')

    def add_test_mark(self, subject, mark):
        if subject in self.subjects:
            if MIN_TEST_MARK <= mark <= MAX_TEST_MARK:
                self.__subjects_dict[subject]['testMarks'].append(mark)
            else:
                raise ValueError(f'Оценка теста должна быть больше {MIN_TEST_MARK} и меньше {MAX_TEST_MARK}!')
        else:
            raise ValueError(f'Нет предмета {subject}')

    def get_avg_test_score(self):
        result = []
        for subject, marks in self.__subjects_dict.items():
            test_marks = marks['testMarks']
            avg_marks = 0 if not test_marks else sum(test_marks) / len(test_marks)
            result.append({subject: avg_marks})
        return result

    def get_avg_score(self):
        result = []
        for marks in self.__subjects_dict.values():
            result.extend(marks['marks'])
        return 0 if not result else sum(result) / len(result)


if __name__ == '__main__':
    student1 = Student('Имя', 'Фамилия', 'Отчество', 'csv')
    student2 = Student('Имя', 'Фамилия', 'Отчество', 'csv')
    student1.add_mark('Физика', 4)
    student1.add_mark('Физика', 2)
    student1.add_mark('Физика', 5)
    student1.add_test_mark('Физика', 4)
    student1.add_test_mark('Физика', 3)
    student1.add_test_mark('Физика', 3)
    student1.add_test_mark('Химия', 40)

    print(student1.subjects)
    print(student1.get_avg_test_score())
    print(student1.get_avg_score())
