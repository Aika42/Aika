def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

def test_fact():
    assert fact(3) == 6
    assert fact(5) == 120
    assert fact(1) == 1
    print('ok')

#test_fact()

def word_reverse(s):
    if len(s) <= 1:
        return s
    return s[len(s)-1] + word_reverse(s[:len(s)-1])

def test_word_reverse():
    assert word_reverse('apple') == 'elppa'
    assert word_reverse('akka') == 'akka'
    print('tested')

#test_word_reverse()

def palindrome(s):

    if word_reverse(s) == s:
        return True
    return False

def test_palindrome():
    assert palindrome('kayak') == True
    assert palindrome('bob') == True
    assert palindrome('via') == False
    print('ok')

#test_palindrome()

def list_reverse(xs: list):
    if len(xs) <= 1:
        return xs
    return [xs[len(xs)-1]] + list_reverse(xs[:len(xs)-1])

def test_list_reverse():
    assert list_reverse([4, 5, 1, 3]) == [3, 1, 5, 4]

# test_list_reverse()

# Modify the recursive tree program using one or all of the following ideas:
#
# Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.
#
# Modify the color of the branches so that as the branchLen gets very short it is colored like a leaf.
#
# Modify the angle used in turning the turtle so that at each branch point the angle is selected at random in some range. For example choose the angle between 15 and 45 degrees. Play around to see what looks good.
#
# Modify the branchLen recursively so that instead of always subtracting the same amount you subtract a random amount in some range.
#
# If you implement all of the above ideas you will have a very realistic looking tree.


import turtle
import random

def tree(branchLen,t):
    if branchLen > 5:
        t.width(branchLen//10)
        if branchLen < 20:
            t.color('green')
        else:
            t.color("brown")

        angle = random.randrange(15,45)
        r = random.randrange(10,15)

        t.forward(branchLen)
        t.right(angle)
        tree(branchLen-r,t)
        t.left(angle+angle)
        tree(branchLen-r,t)
        t.right(angle)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    tree(75,t)
    myWin.exitonclick()

main()



