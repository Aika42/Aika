def lcs(xs: str, ys: str) -> int:
    cache = {}

    def S(i, j) -> int:
        if i >= len(xs) or j >= len(ys):
            return 0

        key = str(i) + ':' + str(j)
        res = cache.get(key)
        if res:
            return res

        if xs[i] == ys[j]:
            res = 1 + S(i + 1, j + 1)
        else:
            res = max(S(i + 1, j), S(i, j + 1))

        cache[key] = res
        return res

    return S(0, 0)


def lcs_tbl(xs: str, ys: str) -> int:
    n = len(xs) + 1
    m = len(ys) + 1
    tb = [[0] * m for _ in range(n)]

    for x in range(1, n):
        for y in range(1, m):
            if xs[x - 1] == ys[y - 1]:
                tb[x][y] = 1 + tb[x - 1][y - 1]
            else:
                tb[x][y] = max(tb[x][y - 1], tb[x - 1][y])
    return tb[n - 1][m - 1]


def lcs_palindrome(xs: str) -> int:
    ys = list(reversed(xs))
    return lcs_tbl(xs, ys)


# return lcs_palindrome(s)


def test_lcs_tbl():
    assert lcs_tbl('a', 'b') == 0
    assert lcs_tbl('abca', 'bda') == 2
    assert lcs_tbl('abca', 'bda') == 2
    assert lcs_tbl('cgabca', 'gbdaca') == 4
    assert lcs_tbl('bbbab', 'babbb') == 4


def test_lcs():
    assert lcs('a', 'b') == 0
    assert lcs('abca', 'bda') == 2
    assert lcs('abca', 'bda') == 2
    assert lcs('cgabca', 'gbdaca') == 4
    assert lcs('bbbab', 'babbb') == 4


def test_lcs_palindrome():
    assert lcs_palindrome('abca') == 3
    assert lcs_palindrome('cbbd') == 2
    assert lcs_palindrome('bbbab') == 4


def xtest_lcs_palindrome_1():
    s = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg"
    print('len(s)', len(s))
    assert lcs_palindrome(s) == 494


def test_palindrome():
    def is_palindrome(s: str) -> bool:
        if len(s) <= 1:
            return True

        h, t = s[0], s[len(s) - 1]
        if h == t:
            res = is_palindrome(s[1:len(s) - 1])
        else:
            res = False
        return res

    assert not is_palindrome("ab")
    assert is_palindrome("ababa")
    assert is_palindrome("abba")


def test_lcs_all():
    # https://www.techiedelight.com/longest-common-subsequence-finding-lcs/

    def lcs_all(xs: str, ys: str) -> 'set[ str ]':
        def S(x, y) -> 'set[str]':
            if x >= len(xs) or y >= len(ys):
                return {''}

            if xs[x] == ys[y]:
                a = S(x + 1, y + 1)
                res = set(xs[x] + s for s in a)
                return res

            a1 = S(x, y + 1)
            a2 = S(x + 1, y)
            e1 = a1.pop()
            e2 = a2.pop()

            if len(e1) > len(e2):
                a1.add(e1)
                return a1
            if len(e1) < len(e2):
                a2.add(e2)
                return a2
            else:
                a1.add(e1)
                a2.add(e2)
                return a1.union(a2)

        return S(0, 0)

    assert lcs_all('a', 'a') == {'a'}
    assert lcs_all('ab', 'aba') == {'ab'}
    assert lcs_all('abab', 'xbaxba') == {'aba', 'bab'}
    assert lcs_all('XMJYAUZ', 'MZJAWXU') == {'MJAU'}
    assert lcs_all('ABCBDAB', 'BDCABA') == {'BCAB', 'BCBA', 'BDAB'}


def test_lcs_all_cache():
    # https://www.techiedelight.com/longest-common-subsequence-finding-lcs/

    def lcs_all(xs: str, ys: str) -> 'set[ str ]':

        cache = {}

        def S(x, y) -> 'set[str]':
            if x >= len(xs) or y >= len(ys):
                return {''}

            key = str(x) + ':' + str(y)
            res = cache.get(key)
            if res:
                return res

            if xs[x] == ys[y]:
                a = S(x + 1, y + 1)
                res = set(xs[x] + s for s in a)
            else:
                a1 = S(x, y + 1)
                e1 = a1.pop()
                a1.add(e1)

                a2 = S(x + 1, y)
                e2 = a2.pop()
                a2.add(e2)

                if len(e1) > len(e2):
                    res = a1
                elif len(e1) < len(e2):
                    res = a2
                else:
                    res = a1.union(a2)

            cache[key] = res
            return res

        return S(0, 0)

    assert lcs_all('a', '') == {''}
    assert lcs_all('a', 'a') == {'a'}
    assert lcs_all('ab', 'aba') == {'ab'}
    assert lcs_all('abab', 'xbaxba') == {'aba', 'bab'}
    assert lcs_all('XMJYAUZ', 'MZJAWXU') == {'MJAU'}
    assert lcs_all('ABCBDAB', 'BDCABA') == {'BCAB', 'BCBA', 'BDAB'}


#

#
