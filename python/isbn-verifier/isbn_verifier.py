'''
Author: your name
Date: 2020-09-16 12:40:05
LastEditors: onepisYa
LastEditTime: 2021-03-30 21:58:27
Description: file content
'''
import re


def is_valid(isbn):
    pat = r"[0-9-]{9,12}[Xx0-9]"
    _isbn = re.search(pat, isbn)
    if not _isbn:
        return False
    _isbn = re.sub(r"[-]", "", _isbn.group())
    if len(_isbn) != 10:
        return False
    s_mod = sum(a * b for a, b in zip(
        map(lambda y: 10 if y in ['x', 'X'] else int(y), _isbn),
        range(10, 0, -1))) % 11
    return True if s_mod == 0 else False
