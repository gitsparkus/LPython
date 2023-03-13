"""
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых
pickle файлов.
"""

import pickle
import os


def json_search(path: str):
    files = (file for file in os.listdir(path) if file.endswith('.json'))

    for file in files:
        new_filename = f'{os.path.splitext(file)[0]}.pickle'
        with open(os.path.join(path, file), 'r', encoding='UTF-8') as f:
            data = f.read()
            with open(os.path.join(path, new_filename), 'wb') as f:
                pickle.dump(data, f)


if __name__ == '__main__':
    json_search('c:/temp/')
