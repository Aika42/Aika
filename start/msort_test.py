# def msort(xs: list) -> list:
#     if len(xs) < 1:
#         return []
#     l, r = xs[:len(xs) // 2], xs[len(xs) // 2:]

#     for i in range(len(l) - 1):
#         if l[i] >= l[i + 1]:
#             l[i], l[i + 1] = l[i + 1], l[i]

#     for j in range(len(r) - 1):
#         if r[j] >= r[j + 1]:
#             r[j], r[j + 1] = r[j + 1], r[j]

#     return merge(l, r)


def msort(xs: list) -> list:
    if len(xs) < 2:
        return xs

    r, l = xs[:len(xs) // 2], xs[len(xs) // 2:]
    return merge(msort(l), msort(r))


def merge(l: list, r: list) -> list:
    """got 2 sorted list
    return sorted list"""
    if len(l) < 1:
        return r
    if len(r) < 1:
        return l
    if l[0] <= r[0]:
        return [l[0]] + merge(l[1:], r)
    return [r[0]] + merge(l, r[1:])


def test0():
    xs = [1]
    assert msort(xs) == sorted(xs)
    xs = [2, 1]
    assert msort(xs) == sorted(xs)
    xs = [3, 2, 1]
    assert msort(xs) == sorted(xs)
    xs = [4, 0, 3, 2, 1]
    assert msort(xs) == sorted(xs)
