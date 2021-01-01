# 10.4 Write a function called average that takes a list of numbers as a parameter and returns the average of the numbers.
def average(xs: list) -> int:
    import math
    sum = 0
    for ch in xs:
        sum = sum + ch
    avg = sum/len(xs)
    avg1 = math.floor(avg)
    if avg1 == avg:
        return avg1
    else:
        return avg

def test_average():
    assert average([4, 3, 6, 7]) == 5
    assert average([4]) == 4
    assert average([0, 10, 20, 3]) == 8.25

# 10.5 Write a Python function named max that takes a parameter containing a nonempty list of integers and returns the maximum value.
def max(xs: list) -> int:
    m = xs[0]
    for ch in xs:
        if ch > m:
            m = ch
    return m

def test_max():
    assert max([4, 3, 6, 7]) == 7
    assert max([4]) == 4

# 10.6 Write a function sum_of_squares(xs) that computes the sum of the squares of the numbers in the list xs.
def sum_of_squares(xs: list) -> int:
    sum = 0
    sq = [ch * ch for ch in xs]
    for ch1 in sq:
        sum = sum + ch1
    return sum

def test_sum_of_squares():
    assert sum_of_squares([2, 3, 4]) == 29

# 10.7 Write a function to count how many odd numbers are in a list.
def odd_numbers(xs: list) -> int:

    xs1 = [ch for ch in xs if ch % 2 == 0]
    return len(xs1)

def test_odd_numbers():
    assert odd_numbers([2, 3, 4]) == 2

# 10.8 Sum up all the even numbers in a list.
def sum_even(xs: list) -> int:

    xs1 = [ch for ch in xs if ch % 2 == 1]
    sum = 0
    for ch in xs1:
        sum = sum + ch

    return sum

def test_sum_even():
    assert sum_even([3, 4, 6, 9]) == 12
    assert sum_even([33, 3, 6]) == 36

# 10.9 Sum up all the negative numbers in a list.
def sum_negative(xs: list) -> int:
    xs1 = [ch for ch in xs if ch < 0]
    sum = 0
    for ch1 in xs1:
        sum = sum + ch1
    return sum

def test_sum_negative():
    assert sum_negative([-3, 4, 6, -9]) == -12
    assert sum_negative([8, 9, -1]) == - 1
    assert sum_negative([90, 80]) == 0


# 10.10 Count how many words in a list have length 5.
def count_words(xs: list) -> int:
    xs1 = [ch for ch in xs if len(ch) >= 5]

    return len(xs1)

def test_count_words():
    assert count_words(['wolf', 'Algonquin', 'Newyear']) == 2

# 10.11 Sum all the elements in a list up to but not including the first even number.
def sum_even_not_first(xs: list) -> int:
    xs1 = [ch for ch in xs if ch % 2 == 1]
    sum = 0
    for ch1 in xs1:
        sum = sum + ch1
    newsum = sum - xs1[0]
    return newsum

def test_sum_even_not_first():
    assert sum_even_not_first([3, 4, 5, 6, 11, 3]) == 19
    assert sum_even_not_first([23, 0, 8, 9]) == 9


# 10.12 Count how many words occur in a list up to and including the first occurrence of the word “sam”.






