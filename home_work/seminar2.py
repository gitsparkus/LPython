"""
Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл. Для тестированию
возьмите pickle версию файла из задачи 4 семинара. Функция должна извлекать ключи словаря для заголовков столбца из
переданного файла.
"""

from pathlib import Path
import pickle
import csv


def to_csv(file_pickle: Path, file_csv: Path):
    with open(file_pickle, 'rb') as f:
        dicts_list = pickle.load(f)

        with open(file_csv, 'w', newline='', encoding='utf-8') as f_csv:
            writer = csv.writer(f_csv)

            for i, row in enumerate(dicts_list):
                if i == 0:
                    writer.writerow(row.keys())
                else:
                    writer.writerow(row.values())


if __name__ == '__main__':
    to_csv(Path('../pickle'), Path('../csv'))
