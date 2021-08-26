from element import Element
from typing import List


def check_le_valid(vec: List[Element], mid: int, target: int) -> bool:
    return vec[mid].value <= target


def find_right_bound(vec: List[Element], target: int) -> int:
    l = 0
    r = len(vec) - 1

    while l < r:
        mid = l + r + 1 >> 1
        if check_le_valid(vec, mid, target):
            l = mid
        else:
            r = mid - 1

    return l
