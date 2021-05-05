# Given two strings ‘X’ and ‘Y’, find the length of the longest common
# substring.

# https://www.geeksforgeeks.org/longest-common-substring-dp-29/

from typing import Generator


def is_subs(xs: str, x: str) -> bool:
    n = len(xs)
    m = len(x)
    for i in range(n - m + 1):
        if xs[i:i + m] == x:
            return True
    return False


def test_is_subs():
    assert is_subs('ab', '')
    assert is_subs('ab', 'a')
    assert is_subs('abc', 'bc')
    assert not is_subs('abc', 'ax')


def all_subs(xs: str) -> 'Generator[str]':
    return (xs[i:j] for i in range(len(xs)) for j in range(i + 1, len(xs) + 1))


def test_all_subs():
    xs = 'abcd'
    got = set(all_subs(xs))
    # print(got)
    assert len(got) == len(xs) * (len(xs) + 1) / 2


def bf(xs: str, ys: str) -> int:
    """brute force"""
    try:
        return max(len(x) for x in all_subs(xs) if is_subs(ys, x))
    except ValueError:
        return 0


def test_bf():
    assert bf('a', '') == 0
    assert bf('ab', 'bc') == 1
    assert bf('abcd', 'xbcdy') == 3


def lcs(xs: str, ys: str) -> int:
    """dynamic solution"""
    n = len(xs)
    m = len(ys)

    def S(i: int, j: int) -> int:

        if i >= n or j >= m:
            return 0
        if xs[i] == ys[j]:
            if i < n - 1 and j < m - 1 and xs[i + 1] == ys[j + 1]:
                return 1 + S(i + 1, j + 1)
            return 1
        return max(S(i + 1, j), S(i, j + 1))

    return S(0, 0)


def test_lcs():
    assert lcs('a', '') == 0
    assert lcs('ab', 'bc') == 1
    assert lcs('abcd', 'xbcdy') == 3
    assert lcs('abcdxyz', 'xyzabcd') == 4
    assert lcs('zxabcdezy', 'yzabcdezx') == 6


#

#
