"""
✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
✔ Каждая группа включает файлы с несколькими расширениями.
✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
"""
import os
import shutil

__CURRENT_PATH = os.getcwd()
__FILE_TYPES = {
    'video': ('avi', 'mp4'),
    'image': ('jpg', 'png'),
    'text': ('doc', 'txt')
}


def sort_files(path: str = __CURRENT_PATH):
    files = os.listdir(path)

    for k, v in __FILE_TYPES.items():
        new_path = os.path.join(path, k)
        if not os.path.exists(new_path):
            os.mkdir(new_path)
        for file in files:
            ext = file.rsplit('.')[:0:-1]
            if ext and ext[0] in v:
                shutil.move(os.path.join(path, file), os.path.join(new_path, file))


if __name__ == '__main__':
    sort_files('c:/temp')
