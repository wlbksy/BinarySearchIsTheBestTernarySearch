from element import Element
from typing import List


def check_ge_valid(vec: List[Element], mid: int, target: int) -> bool:
    return vec[mid].value >= target


def find_left_bound(vec: List[Element], target: int) -> int:
    l = 0
    r = len(vec) - 1

    while l < r:
        mid = l + r >> 1
        if check_ge_valid(vec, mid, target):
            r = mid
        else:
            l = mid + 1

    return l


target = 8
raw_vec_list = [
    [7, target, 9],
    [target, 9],
    [7, target],
    [7, 9],
    [target, target, 9],
    [7, target, target, 9],
    [7, target, target],
    [6, 7],
    [9, 10],
]


test_vecs = [[Element(ele, idx) for idx, ele in enumerate(l)] for l in raw_vec_list]


test_func = [find_left_bound]

for test_vec in test_vecs:
    print(test_vec)
    print("target: {}".format(target))

    for func in test_func:
        idx = func(test_vec, target)
        print(func.__name__, test_vec[idx])

    print()
