""" В этом файле находятся функции, используемые в проекте"""
from datetime import datetime
from random import choice

ALL_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


def generate_code(code_len=25):
    """ Возвращает случайную строку из 25 символов"""
    return "".join([choice(ALL_CHARS) for i in range(code_len)])


def validate_iso8601(dt_str):
    try:
        datetime.fromisoformat(dt_str.replace('Z', '+00:00'))
    except:
        return False
    return True


def get_date(line):
    return datetime.strptime(line, "%Y-%m-%dT%H:%M:%S.%fZ")


if __name__ == '__main__':
    print(generate_code(40))