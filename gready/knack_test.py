import itertools as itt
from functools import reduce


def power_set(xs: 'List[Itme]') -> 'List[Itme]':
    return (x for i in range(len(xs)) for x in itt.combinations(xs, i + 1))


def knapsack(xs: 'List[Item]', w: float) -> 'List[Item]':
    def sum_w(xs) -> float:
        return sum(x[0] for x in xs)

    def sum_v(xs) -> float:
        return sum(x[1] for x in xs)

    ps = (x for x in power_set(xs) if sum_w(x) <= w)
    # print(ps)
    return max(ps, key=sum_v)


def powerset(lst):
    return reduce(
        lambda result, x: result + [subset + [x] for subset in result], lst,
        [[]])


def assert_list_eq(xs, ys):
    assert sorted(xs) == sorted(ys)


def test_power_set():

    assert_list_eq(power_set(range(2)), [(0, ), (0, 1), (1, )])
    assert_list_eq(map(tuple, powerset(range(2))), [(), (0, ), (0, 1), (1, )])

    # print(powerset(range(3)))


def test_knapsack_br_force():
    assert knapsack([(1, 1), (2, 2), (3, 3)], 3) == ((3, 3), )
    assert knapsack([(1, 1), (2, 2), (3, 3)], 3) == ((3, 3), )
    assert knapsack([(1, 1), (2, 2), (3, 3)], 4) == ((1, 1), (3, 3))
