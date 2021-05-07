# https://leetcode.com/problems/super-washing-machines/

from typing import List


def sol(xs: List[int]) -> int:
    n = len(xs)
    total = sum(xs)
    if total % n != 0:
        return -1

    opt = total // n
    pref = 0
    ans = 0
    for i, x in enumerate(xs):
        pref += x
        deff = max(0, pref - (i + 1) * opt)
        supr = max(0, total - pref + x - (n - i) * opt)
        ans = max(ans, deff + supr)
    return ans


def test_sol():
    print()
    assert sol([1]) == 0
    assert sol([1, 1, 1]) == 0
    assert sol([1, 0, 5]) == 3
    assert sol([0, 3, 0]) == 2
    assert sol([0, 2, 0]) == -1
