# what problem are you solving?

# please write examples (tests) for it

# Can you write down the logic of your solution?
# Like:  for every coin in coins I do ....

# In case of coin problem I strongly advise to use Recursive first.
# After you understand Recursive solution trying iterative - the one you made -
# be easier


# original version
def coin_change(coins: list, change: int) -> int:
    # a = [[0] * (change + 1)] * len(coins)
    a = [[0] * (change + 1) for _ in range(len(coins))]
    for i in range(len(coins)):
        for j in range(change + 1):
            if j == 0:
                a[i][j] = 1
            else:
                if i == 0:
                    if j % coins[i] == 0:
                        a[i][j] = 1
                    else:
                        a[i][j] = 0
                else:
                    if coins[i] < j:
                        a[i][j] = a[i - 1][j]
                    else:
                        a[i][j] = a[i - 1][j] + a[i][j - coins[i]]
    print(a)


def xtest_coin_change0():
    print(coin_change((1, 2), 3))
    # print(coin_change((2, 3, 5, 10), 15))


def iterative0(cs: list, a: int) -> int:
    tb = [[0] * (a + 1) for _ in range(len(cs))]

    for ci in range(len(tb)):
        for ai in range(a + 1):

            # if a == 0 solution is 1 for any cs
            if ai == 0:
                tb[ci][ai] = 1
                continue

            # the last coin
            if ci == 0:
                tb[ci][ai] = 1 if ai % cs[ci] == 0 else 0
            else:
                tb[ci][ai] = tb[ci - 1][ai] + tb[ci][ai - cs[ci]]

    # print(tb)
    return tb[len(cs) - 1][a]


def test_iterative0():
    got = iterative0((1, 2), 3)
    assert got == 2
    got = iterative0((1, 2, 3), 4)
    assert got == 4
    got = iterative0((2, 5, 3, 6), 10)
    assert got == 5


def recursive(cs: tuple, amount: int) -> int:
    def S(ci: int, n: int) -> int:
        if n == 0:
            return 1
        if n < 0 or ci >= len(cs):
            return 0

        return S(ci, n - cs[ci]) + S(ci + 1, n)

    return S(0, amount)


def test_recursive():
    got = recursive((1, 2), 3)
    assert got == 2
    got = recursive((1, 2, 3), 4)
    assert got == 4
    got = recursive((2, 5, 3, 6), 10)
    assert got == 5


def recursive_cached(cs: tuple, amount: int) -> int:
    cache = {}

    def S(ci: int, n: int) -> int:
        key = (ci, n)
        res = cache.get(key)
        if res:
            return res

        if n == 0:
            return 1
        if n < 0 or ci >= len(cs):
            return 0

        res = S(ci, n - cs[ci]) + S(ci + 1, n)
        cache[key] = res
        return res

    return S(0, amount)


def test_recursive_cached():
    got = recursive_cached((1, 2), 3)
    assert got == 2
    got = recursive_cached((1, 2, 3), 4)
    assert got == 4
    got = recursive_cached((2, 5, 3, 6), 10)
    assert got == 5


def test_2d_array():
    a = [[0] * 2] * 3
    assert a[0][0] == 0 and a[1][0] == 0
    a[0][0] = 1
    assert a[0][0] == 1 and a[1][0] == 1

    a = [[0] * 2 for _ in range(3)]
    assert a[0][0] == 0 and a[1][0] == 0
    a[0][0] = 1
    assert a[0][0] == 1 and a[1][0] == 0
