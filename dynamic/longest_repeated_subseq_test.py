# Longest Repeated Subsequence Problem
# # https://www.techiedelight.com/longest-repeated-subsequence-problem/


def lrs(xs: str) -> int:
    N = len(xs)

    def f(i, j) -> int:
        if i == N or j == N:
            return 0
        if i == j:
            return 0
        if xs[i] == xs[j]:
            return 1 + f(i + 1, j + 1)
        return max(f(i + 1, j), f(i, j + 1))

    return f(0, 1)


def test_lrs():
    assert lrs('') == 0
    assert lrs('a') == 0
    assert lrs('aa') == 1
    assert lrs('aaa') == 2
    assert lrs('abab') == 2
    assert lrs('ATACTCGGA') == 4
