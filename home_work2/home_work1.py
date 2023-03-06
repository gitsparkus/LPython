"""
✔ Напишите функцию группового переименования файлов. Она должна:
    ✔ принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
    ✔ принимать параметр количество цифр в порядковом номере.
    ✔ принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри
        каталога.
    ✔ принимать параметр расширение конечного файла.
    ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из
        исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и
        расширение.
"""

import os

__CURRENT_PATH = os.getcwd()


def renamer(path: str = __CURRENT_PATH, result_name: str = '', counter_length: int = 3, source_ext: str = '',
            result_ext: str = '.tmp',
            start: int = 0, stop: int = 0):
    files = (file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)))
    counter = 1
    for file in files:
        if not source_ext or file.endswith(f'.{source_ext}'):
            name_part = ''
            if start and stop:
                name_part = file[start - 1:stop]
            file_name = f'{name_part}{result_name}{str(counter).zfill(counter_length)}.{result_ext}'
            os.rename(os.path.join(path, file), os.path.join(path, file_name))
            counter += 1


if __name__ == '__main__':
    renamer('c:/temp', result_name='new', counter_length=10, result_ext='log', start=3, stop=6)
