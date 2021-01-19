def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


#fib(8)

def fib_dict(n: int, d: dict) -> int:
    if n in d:
        return d[n]
    else:
        ans = fib_dict(n-1, d) + fib_dict(n-2, d)
        d[n] = ans
        return ans

d = {1: 1, 2: 2}
fib_dict(8, d)
