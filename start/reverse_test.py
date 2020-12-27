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

def reverse2(s: str) -> str:

    return ''.join([s[i] for i in range(len(s)-1,-1,-1)])


def test_reverse2():
    assert reverse2("a") == "a"
    assert reverse2("ab") == "ba"
    assert reverse2("abc") == "cba"

test_reverse2()

# Petals
import turtle

def petals(fred: turtle):
    for i in range(5):
        fred.right(20)
        fred.circle(100, 90)
        fred.circle(-100, 90)
        fred.circle(100, 90)
        fred.circle(-100, 90)

        fred.left(-20)
        fred.circle(-100, -90)
        fred.circle(100, -90)
        fred.circle(-100, -90)
        fred.circle(100, -90)

def main():
    fred = turtle.Turtle()
    fred.speed(20)

    wn = turtle.Screen()

    fred.up()
    fred.goto(-200, -200)
    fred.down()

    petals(fred)

    wn.exitonclick()

main()




