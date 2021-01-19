import turtle
MIN_LEN = 20

def tree(branchlen, t):
    """tree = branch with two other smaller trees"""
    if branchlen < MIN_LEN:
        return
    t.forward(branchlen)
    t.right(20)
    tree(branchlen-10, t)
    t.left(20*2)
    tree(branchlen-10, t)
    t.right(20)
    t.backward(branchlen)


def tur():
    t = turtle.Turtle()
    w = turtle.Screen()

    t.left(90)

    tree(60, t)

    w.exitonclick()

tur()
