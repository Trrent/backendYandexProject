""" В этом файле находятся функции, используемые в main.py"""
from random import choice

ALL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def generate_code(code_len=25):
    """ Возвращает случайную строку из 25 символов"""
    return "".join([choice(ALL_CHARS) for i in range(code_len)])


if __name__ == '__main__':
    print(generate_code(40))