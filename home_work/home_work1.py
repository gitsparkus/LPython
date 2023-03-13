"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты
обхода сохраните в файлы json, csv и pickle.
 - Для дочерних объектов указывайте родительскую директорию.
 - Для каждого объекта укажите файл это или директория.
 - Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и
   директорий.
Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
"""

from pathlib import Path
import os
import json
import csv
import pickle


def read_dir(path: Path, parent: str = ''):
    d = {'fullpath': os.path.abspath(path), 'parent': parent, 'size': 0}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [read_dir(Path(f'{path}/{x}'), d['fullpath']) for x in os.listdir(path)]
        d['size'] = sum((x['size'] for x in d['children']))
    else:
        d['type'] = "file"
        d['size'] = os.stat(d['fullpath']).st_size
    return d


if __name__ == '__main__':
    path_dict = read_dir(Path('c:/temp/'))
    with open('../pickle', 'wb') as f:
        pickle.dump(path_dict, f)

    with open('../csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=path_dict.keys())

        writer.writeheader()
        writer.writerow(path_dict)

    with open('../json', 'w') as f:
        json.dump(path_dict, f, indent=2)
