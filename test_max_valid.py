from element import Element
from find_max_valid import find_right_bound
import pytest


class TestFindMaxValid:
    def test_find_max_valid(self):
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
            result_idx = find_right_bound(test_vec, target)

            has_target_flag = False
            max_target_idx = -1
            for idx, e in enumerate(test_vec):
                if e.value <= target:
                    has_target_flag = True
                    max_target_idx = max(max_target_idx, idx)

            if has_target_flag:
                assert result_idx == max_target_idx
            else:
                assert result_idx == 0
