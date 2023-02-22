"""
✔ Напишите функцию, которая принимает на вход строку —
абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла.
"""


def parse_path(path: str) -> tuple:
    path = path.replace('\\', '/').rsplit('/', 1)
    return path[0], *path[1].rsplit('.')


if __name__ == '__main__':
    print(parse_path(r'c:\www\ddd\eee.jpg'))
