def words():
    text = "I will be running in January!!! and I will move close to the mountains in 2021!!!"

    i = 0
    ch1 = 0
    for ch in text:
        if ch == 'e':
            ch1 = ch1 + 1
        if ch != ' ':
            i = i + 1

    percent = ch1 * 100 / i

    print('Your text contains {} alphabetical characters, of which {} ({}%) are "e"'.format(i, ch1, percent))

# Print out a neatly formatted multiplication table, up to 12 x 12.
def multtable(x: int, y: int):

    for i in range(1,11):

        print(  '{} * {:<4} = {:<8}'.format(x, i, x*i), end='\t')
        print( '{} * {:<4} {:<4}'.format(y, i, y*i) )


# 9.5 Write a function that will return the number of digits in an integer.
def integdigit(x: int) -> int:

    str1 = str(abs(x))
    i = 0
    while i < len(str1):
        i = i + 1

    return i

# 9.6 Write a function that reverses its string argument.
def reversal(s: str) -> str:

    newstring = ''
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
    s1 = ''
    for ch in s:
        if ch != r:
            s1 = s1 + ch

    return s1

# 9.9 Write a function that recognizes palindromes.
def palindrome(s: str) -> bool:
    if reversal(s) == s:
        return True
    return False

assert palindrome('kayak') == True
assert palindrome('Wolf') == False

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
            return s[:i]+s[i+1:]
        i = i + 1
    return -1


# Example from book
def remove3(substr, theStr):
    index = theStr.find(substr)
    if index < 0: # substr doesn't exist in theStr
        return theStr
    return_str = theStr[:index] + theStr[index+len(substr):]
    return return_str

assert remove3('an', 'banana') == 'bana'
assert remove3('cyc', 'bicycle') == 'bile'

# 9.12 Write a function that removes all occurrences of a string from another string.
def removal4(s: str, r: str) -> str:


    if len(s) > len(r):
        i = 0
        while i < len(s):
            if s[i:(len(r)+i)] == r:
                return s[0:i] + s[i + len(r):]
            i = i + 1
    return -1

assert removal4('bicycle', 'cycle') == 'bi'
assert removal4('bicycle', 'icy') == 'bcle'
assert removal4('bicycle', 'le') == 'bicyc'

# 9.18 Write a function that implements a substitution cipher.
# In a substitution cipher one letter is substituted for another to garble the message.
# For example A -> Q, B -> T, C -> G etc. your function should take two parameters,
# the message you want to encrypt, and a string that represents the mapping of the 26 letters in the alphabet.
# Your function should return a string that is the encrypted version of the message.

def code(s, mapping)->str:

    list = []
    i = 0
    for i in mapping:
        mapping[i] = mapping[i+3]
        list.append(mapping[i])
        i = i + 5
    print(mapping[10])
    print(list)

mapping = 'a->x,b->y,c->t'
assert code('a', mapping) == 'x'
assert code('ab', mapping) == 'xy'

matrix = [[0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 2, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 3, 0]]

matrix1 = {(0,3): 1, (2,1): 2, (4,3): 3}

matrix == matrix1




