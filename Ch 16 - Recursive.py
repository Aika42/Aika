def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

def word_reverse(s):
    if len(s) <= 1:
        return s
    return s[len(s)-1] + word_reverse(s[:len(s)-1])

def palindrome(s):

    if word_reverse(s) == s:
        return True
    return False

palindrome('kaya')

