def words():
    text = "I will be running in January!!! and I will move close to the mountains in 2021!!!"

    i = 0
    ch1 = 0
    for ch in text:
        if ch == "e":
            ch1 = ch1 + 1
        if ch != " ":
            i = i + 1

    percent = ch1 * 100 / i

    print(
        'Your text contains {} alphabetical characters, of which {} ({}%) are "e"'.format(
            i, ch1, percent
        )
    )


# Print out a neatly formatted multiplication table, up to 12 x 12.
def multtable(x: int, y: int):

    for i in range(1, 11):

        print()
        for j in range(1, 11):
            print(i, "*", j, "=", end=" ")
            print(i * j)


# 9.5 Write a function that will return the number of digits in an integer.
def intdigit(x: int) -> int:
    return len(str(abs(x)))


def test_intdigit():
    assert intdigit(465) == 3
    assert intdigit(43) == 2
    assert intdigit(0) == 1


# 9.6 Write a function that reverses its string argument.
def reversal(s: str) -> str:

    newstring = ""
    i = len(s) - 1
    while i >= 0:
        newstring = newstring + s[i]
        i = i - 1
    return newstring


# 9.7 Write a function that mirrors its string argument, generating a string containing the original string and the string backwards.
def mirror(s: str) -> str:

    return reversal(s) + s


# 9.8 Write a function that removes all occurrences of a given letter from a string.
def removal(s: str, r: str) -> str:
    s1 = ""
    for ch in s:
        if ch != r:
            s1 = s1 + ch

    return s1


# 9.9 Write a function that recognizes palindromes.
def palindrome(s: str) -> bool:
    if reversal(s) == s:
        return True
    return False


assert palindrome("kayak") == True
assert palindrome("Wolf") == False

# 9.10 Write a function that counts how many non-overlapping occurences of a substring appear in a string.
def substring(s: str, r: str) -> bool:

    for ch in s:
        for ch1 in r:
            if ch1 == ch:
                return True
    return False


def substring1(s: str, r: str) -> int:

    if substring(s, r):
        return len(r)
    return -1


# 9.11 Write a function that removes the first occurrence of a string from another string.
def removal2(s: str, r: str) -> str:

    i = 0
    while i < len(s):
        if s[i] == r:
            return s[:i] + s[i + 1 :]
        i = i + 1
    return -1


# Example from book
def remove3(substr, theStr):
    index = theStr.find(substr)
    if index < 0:  # substr doesn't exist in theStr
        return theStr
    return_str = theStr[:index] + theStr[index + len(substr) :]
    return return_str


assert remove3("an", "banana") == "bana"
assert remove3("cyc", "bicycle") == "bile"

# 9.12 Write a function that removes all occurrences of a string from another string.
def removal4(s: str, r: str) -> str:

    if len(s) > len(r):
        i = 0
        while i < len(s):
            if s[i : (len(r) + i)] == r:
                return s[0:i] + s[i + len(r) :]
            i = i + 1
    return -1


assert removal4("bicycle", "cycle") == "bi"
assert removal4("bicycle", "icy") == "bcle"
assert removal4("bicycle", "le") == "bicyc"


# 9.18 Write a function that implements a substitution cipher.
def encrypt(s: str, mapping: str) -> str:

    s1 = mapping.split(",")
    r1 = ""

    j = 0
    while j < len(s):
        i = 0
        while i < len(s1):
            if s1[i][0] == s[j]:
                r1 = r1 + s1[i][3]
            i = i + 1
        j = j + 1
    return r1


def test_encrypt():
    mapping = "a->x,b->y,c->t"
    assert encrypt("a", mapping) == "x"
    assert encrypt("ab", mapping) == "xy"
    assert encrypt("abba", mapping) == "xyyx"
    assert encrypt("abcbba", mapping) == "xytyyx"


# 9.19 Write a function that decrypts the message from the previous exercise.
def decrypt(s: str, mapping: str) -> str:
    s1 = mapping.split(",")
    r1 = ""

    j = 0
    while j < len(s):
        i = 0
        while i < len(s1):
            if s1[i][3] == s[j]:
                r1 = r1 + s1[i][0]
            i = i + 1
        j = j + 1
    return r1


def test_decrypt():
    mapping2 = "a->x,b->y,c->t"
    assert decrypt("x", mapping2) == "a"
    assert decrypt("xy", mapping2) == "ab"
    assert decrypt("xyyx", mapping2) == "abba"
    assert decrypt("xytyyx", mapping2) == "abcbba"
    print("ok")
    print("test")
    print("chub")
