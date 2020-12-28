def reverse1(s: str) -> str:
    s1 = []

    i = len(s) - 1
    while i > -1:
        s1.append(s[i])
        i = i - 1
    return "".join(s1)


def test_reverse():
    assert reverse1("a") == "a"
    assert reverse1("ab") == "ba"
    assert reverse1("abc") == "cba"
    assert reverse1("abca") == "acba"


test_reverse()


def reverse2(s: str) -> str:

    return "".join([s[i] for i in range(len(s) - 1, -1, -1)])


def test_reverse2():
    assert reverse2("a") == "a"
    assert reverse2("ab") == "ba"
    assert reverse2("abc") == "cba"


# test_reverse2()

# Write a function that will return the number of digits in an integer.
# You can NOT use str() to convert int into a string
# You should use operataion  // in a loop (or recursion)
def int_len(n: int) -> int:
    # NotImplemented
    a = 0
    i = 10
    # while n > 0:
    #     NotImplemented
    #     i+=1
    return a


def test_int_len():
    assert int_len(1) == 1
    assert int_len(10) == 2
    assert int_len(100) == 3
    assert int_len(1111) == 4

