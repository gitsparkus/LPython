"""
Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите
функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.
"""

import os
import csv
import pickle


class FileTools:

    def __init__(self, work_dir: str):
        self.work_dir = work_dir

    def json_to_pickle(self):
        path = self.work_dir

        files = (file for file in os.listdir(path) if file.endswith('.json'))

        for file in files:
            new_filename = f'{os.path.splitext(file)[0]}.pickle'
            with open(os.path.join(path, file), 'r', encoding='UTF-8') as f:
                data = f.read()
                with open(os.path.join(path, new_filename), 'wb') as f:
                    pickle.dump(data, f)

    def to_csv(self, file_pickle: str, file_csv: str):
        file_pickle = os.path.join(self.work_dir, file_pickle)
        file_csv = os.path.join(self.work_dir, file_csv)
        with open(file_pickle, 'rb') as f:
            dicts_list = pickle.load(f)

            with open(file_csv, 'w', newline='', encoding='utf-8') as f_csv:
                writer = csv.writer(f_csv)

                for i, row in enumerate(dicts_list):
                    if i == 0:
                        writer.writerow(row.keys())
                    else:
                        writer.writerow(row.values())

    def read_csv(self, file: str):

        file = os.path.join(self.work_dir,file)

        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            pickle_str = ''
            for row in reader:
                pickle_str += str(row)

            print(pickle.dumps(pickle_str))


if __name__ == '__main__':

    files_tool = FileTools('c:/temp/')
    files_tool.json_to_pickle()
    files_tool.to_csv('pickle', 'csv')
    files_tool.read_csv('csv')