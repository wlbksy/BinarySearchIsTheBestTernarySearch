from element import Element
from typing import List

from utils import *


def find_left_valley_using_le_right(vec: List[Element]) -> int:
    l = 0
    r = len(vec) - 1

    while l < r:
        mid = l + r >> 1
        if check_le_right(vec, mid):
            r = mid
        else:
            l = mid + 1

    return l


def find_right_valley_using_le_left(vec: List[Element]) -> int:
    l = 0
    r = len(vec) - 1

    while l < r:
        mid = l + r + 1 >> 1
        if check_le_left(vec, mid):
            l = mid
        else:
            r = mid - 1

    return l


def find_left_valley_using_ge_left(vec: List[Element]) -> int:
    l = 0
    r = len(vec) - 1

    while l < r:
        mid = l + r + 1 >> 1
        if check_ge_left(vec, mid):
            r = mid - 1
        else:
            l = mid

    return l


def find_right_valley_using_ge_right(vec: List[Element]) -> int:
    l = 0
    r = len(vec) - 1

    while l < r:
        mid = l + r >> 1
        if check_ge_right(vec, mid):
            l = mid + 1
        else:
            r = mid

    return l
