# ref: https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression


def test_my_max():

    # find str with most 'b'
    def most_b(ss: 'List[str]') -> str:
        def key(s):
            return s.count('b')

        return max(ss, key=key)

    assert most_b(['a', 'c']) == 'a'
    assert most_b(['a', 'abab', 'ba']) == 'abab'
    assert most_b(['a', 'abab', 'ba', 'bbbc']) == 'bbbc'

    # find str with most 'bb'
    def most_bb(ss: 'List[str]') -> str:
        def key(s):
            return s.count('bb')

        return max(ss, key=key)

    assert most_bb(['a', 'c']) == 'a'
    assert most_bb(['a', 'abb', 'aba']) == 'abb'
    assert most_bb(['a', 'abbb', 'abbabb']) == 'abbabb'

    # make func my_max not using standard max()
    def my_max(xs: 'List[object]', key: '(object)->Comaprable') -> object:
        res = xs[0]
        for x in xs:
            if key(x) > key(res):
                res = x
        return res

    assert my_max(['a', 'c'], key=lambda s: s.count('b')) == 'a'
    assert my_max(['ab', 'cbab'], key=lambda s: s.count('b')) == 'cbab'

    # make fun that make func that find max by given key
    def make_mymax(key: '(object)->Comaprable') -> object:
        def f(xs):
            return max(xs, key=key)

        return f

    my_most_b = make_mymax(key=lambda s: s.count('b'))
    assert my_most_b(['a', 'c']) == 'a'
    assert my_most_b(['a', 'abab', 'ba']) == 'abab'
    assert my_most_b(['a', 'abab', 'ba', 'bbbc']) == 'bbbc'

    my_most_bb = make_mymax(key=lambda s: s.count('bb'))
    assert my_most_bb(['a', 'c']) == 'a'
    assert my_most_bb(['a', 'abb', 'aba']) == 'abb'
    assert my_most_bb(['a', 'abbb', 'abbabb']) == 'abbabb'

    # what following func does?
    def best(xs):
        return max(xs, key=lambda x: (x[2], x[0], x[1]))

    assert best(['abc', 'aaa', 'bbb', 'cba']) == 'abc'
    assert best(['abc', 'aac']) == 'abc'
    assert best(['abc', 'abb']) == 'abc'
    assert best(['abc', 'acc']) == 'acc'
    assert best(['abc', 'ccc']) == 'ccc'
    assert best(['cba', 'cbx']) == 'cbx'


#
