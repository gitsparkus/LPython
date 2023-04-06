"""
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК. Соберите информацию
о содержимом в виде объектов namedtuple. Каждый объект хранит:
имя файла без расширения или название каталога,
расширение, если это файл,
флаг каталога,
название родительского каталога.
"""

from collections import namedtuple
from pathlib import Path
import os
import argparse

File = namedtuple('File', ['name', 'ext', 'is_dir', 'parent_name'])


def read_dir(path: Path, parent: Path = None, result_list: list = None):
    if result_list == None:
        result_list = []

    if parent:
        name, ext = os.path.splitext(path.name)
        file = File(name, ext, os.path.isdir(path), parent.absolute())
        result_list.append(file)
    if os.path.isdir(path):
        for x in os.listdir(path):
            read_dir(Path(f'{path}/{x}'), path, result_list)

    return result_list


def parser_function():
    parser = argparse.ArgumentParser(description='Сканирование директории')
    parser.add_argument('--path')
    if src_path := parser.parse_args().path:
        return Path(src_path)


if __name__ == '__main__':
    if path:=parser_function():
        print(read_dir(path))
