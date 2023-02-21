"""
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного
аргумента, а значение - имя аргумента. Если ключ не хешируем, используйте его строковое представление.
"""
from typing import Hashable


def key_func(**kwargs) -> dict:
    result = {}

    for k, v in kwargs.items():
        if isinstance(v, Hashable):
            result[v] = k
        else:
            result[str(v)] = k

    return result


print(key_func(aaa=1, bbb=2, ccc=3, ddd=[1, 2, 3]))
