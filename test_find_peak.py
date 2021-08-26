from element import Element

from find_peak import *
import pytest


class TestFindPeak:
    def test_peak(self):
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

        peak_element_vecs = [
            [Element(ele, idx) for idx, ele in enumerate(l)] for l in peak_vec_list
        ]

        test_func = [
            find_left_peak_using_ge_right,
            find_left_peak_using_le_left,
            find_right_peak_using_ge_left,
            find_right_peak_using_le_right,
        ]

        for peak_element_vec in peak_element_vecs:
            for func in test_func:
                result_idx = func(peak_element_vec)

                min_idx = len(peak_element_vec)
                max_idx = -1
                for idx, e in enumerate(peak_element_vec):
                    if e.value == max_ele:
                        min_idx = min(min_idx, idx)
                        max_idx = max(max_idx, idx)

                if "find_left" in func.__name__:
                    assert result_idx == min_idx
                else:
                    assert result_idx == max_idx
