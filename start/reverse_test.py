def reverse(s: str) -> str:
    s1 = []

    i = len(s)-1
    while i > -1:
        s1.append(s[i])
        i = i - 1
    return ''.join(s1)



def test_reverse():
    assert reverse("a") == "a"
    assert reverse("ab") == "ba"
    assert reverse("abc") == "cba"

test_reverse()
