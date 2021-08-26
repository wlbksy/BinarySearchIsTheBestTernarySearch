from element import Element
from typing import List


def check_le_left(vec: List[Element], mid: int) -> bool:
    left = mid - 1

    assert mid >= 0 and mid < len(vec)
    assert left >= 0 and left < len(vec)

    return vec[mid].value <= vec[left].value


def check_le_right(vec: List[Element], mid: int) -> bool:
    right = mid + 1

    assert mid >= 0 and mid < len(vec)
    assert right >= 0 and right < len(vec)

    return vec[mid].value <= vec[right].value


def check_ge_left(vec: List[Element], mid: int) -> bool:
    left = mid - 1

    assert mid >= 0 and mid < len(vec)
    assert left >= 0 and left < len(vec)

    return vec[mid].value >= vec[left].value


def check_ge_right(vec: List[Element], mid: int) -> bool:
    right = mid + 1

    assert mid >= 0 and mid < len(vec)
    assert right >= 0 and right < len(vec)

    return vec[mid].value >= vec[right].value
