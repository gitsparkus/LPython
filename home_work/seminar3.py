"""
Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. Распечатайте его как pickle строку.
"""

import csv
from pathlib import Path
import pickle


def read_csv(file: Path):

    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        pickle_str = ''
        for row in reader:
            pickle_str += str(row)

        print(pickle.dumps(pickle_str))


if __name__ == '__main__':
    read_csv(Path('../csv'))
