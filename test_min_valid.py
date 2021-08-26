from element import Element
from find_min_valid import find_left_bound
import pytest


class TestFindMinValid:
    def test_find_min_valid(self):
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

        test_vecs = [
            [Element(ele, idx) for idx, ele in enumerate(l)] for l in raw_vec_list
        ]

        for test_vec in test_vecs:
            result_idx = find_left_bound(test_vec, target)

            has_target_flag = False
            min_target_idx = len(test_vec)
            for idx, e in enumerate(test_vec):
                if e.value >= target:
                    has_target_flag = True
                    min_target_idx = min(min_target_idx, idx)

            if has_target_flag:
                assert result_idx == min_target_idx
            else:
                assert result_idx == len(test_vec) - 1
