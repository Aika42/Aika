import itertools as itt
from functools import reduce


def power_set(xs: 'List[Itme]') -> 'List[Itme]':
    return (x for i in range(len(xs)) for x in itt.combinations(xs, i + 1))


def knapsack(xs: 'List[Item]', w: float) -> 'List[Item]':
    """
    Your Solution should be a function. See below.

    Every step in Solution have to a function and tests for this function.

    Don't do unnecessary work - test should be mostly short and obvious, like:

        assert filter_by_weight([(1,10),(2,5)], 1) == [(1,10)]

    Use list comprehension in function. Like:

    you want to filter numbers of xs less then 5:

        res = [x for in xs if x <= 5]

    you want to find max of ts: List[Tuple] by first element in Tuple:

        res = max(ts, key=lambda t: t[0])


    Data model:

        Item = Tuple[num, num]
        Bag = List[Item]

        Solution(items: List[Item], constr: float) -> Bag:

            1. create all possible bags : List[Bag]

            2. select (filter) bags with weight <= constr : List[Bag]

            3. select the best bag - a bag
                such that sum of items' value is max : Bag
    """
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


def powerset_iter(lst):
    res = [[]]
    for x in lst:
        res += [subs + [x] for subs in res]
    return res


def powerset_itertool(lst):
    res = []
    for i in range(len(lst) + 1):
        res += [x for x in itt.combinations(lst, i)]
    return res


def assert_list_eq(xs, ys):
    assert sorted(xs) == sorted(ys)


def test_power_set():

    assert_list_eq(power_set(range(2)), [(0, ), (0, 1), (1, )])
    assert_list_eq(map(tuple, powerset(range(2))), [(), (0, ), (0, 1), (1, )])
    assert_list_eq(map(tuple, powerset_iter(range(2))), [(), (0, ), (0, 1),
                                                         (1, )])
    assert_list_eq(map(tuple, powerset_itertool(range(2))), [(), (0, ), (0, 1),
                                                             (1, )])
    # print(powerset(range(3)))


def test_knapsack_br_force():
    assert knapsack([(1, 1), (2, 2), (3, 3)], 3) == ((3, 3), )
    assert knapsack([(1, 1), (2, 2), (3, 3)], 3) == ((3, 3), )
    assert knapsack([(1, 1), (2, 2), (3, 3)], 4) == ((1, 1), (3, 3))
