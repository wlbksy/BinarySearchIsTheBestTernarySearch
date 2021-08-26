from element import Element

from find_valley import *
import pytest


class TestFindValley:
    def test_valley(self):
        max_ele = 10
        peak_vec_list = [
            [max_ele],
            [1, max_ele, 1],
            [max_ele, 1],
            [1, max_ele],
            [1, max_ele, max_ele, 1],
            [1, max_ele, max_ele],
            [max_ele, max_ele, 1],
            [max_ele, max_ele],
        ]

        min_ele = -1 * max_ele

        valley_element_vecs = [
            [Element(-1 * ele, idx) for idx, ele in enumerate(l)] for l in peak_vec_list
        ]

        test_func = [
            find_left_valley_using_le_right,
            find_left_valley_using_ge_left,
            find_right_valley_using_le_left,
            find_right_valley_using_ge_right,
        ]

        for valley_element_vec in valley_element_vecs:
            for func in test_func:
                result_idx = func(valley_element_vec)

                min_idx = len(valley_element_vec)
                max_idx = -1
                for idx, e in enumerate(valley_element_vec):
                    if e.value == min_ele:
                        min_idx = min(min_idx, idx)
                        max_idx = max(max_idx, idx)

                if "find_left" in func.__name__:
                    assert result_idx == min_idx
                else:
                    assert result_idx == max_idx
