"""
✔ Дорабатываем функции из предыдущих задач.
✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
(добавьте проверки).
✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
"""

from random import choices, randint
from string import ascii_letters, digits
import os

__CURRENT_PATH = os.getcwd()


def make_files(extension: str, min_name: int = 6, max_name: int = 30,
               min_size: int = 256, max_size: int = 4096, count: int = 42, path: str = __CURRENT_PATH):
    if os.path.exists(path):
        for _ in range(count):
            name = ''.join(choices(ascii_letters + digits, k=randint(min_name, max_name)))
            data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
            full_file_name = f'{path}/{name}.{extension}'

            if not os.path.exists(full_file_name):
                with open(full_file_name, 'wb') as f:
                    f.write(data)


def maker(path: str = __CURRENT_PATH, **kwargs):
    if os.path.exists(path):
        for extension, count in kwargs.items():
            make_files(extension=extension, count=count, path=path)


if __name__ == '__main__':
    make_files('bin', count=10)
    maker(zip=2, jpg=3, png=4, avi=3, doc=2, txt=3, mp4=3)
    maker(zip=2, jpg=3, png=4, avi=3, doc=2, txt=3, mp4=3, path='c:/temp')
