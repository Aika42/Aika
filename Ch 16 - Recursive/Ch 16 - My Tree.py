import turtle
import random

def tree(branch, t):
    if branch > 50:
        t.color('brown')
    else:
        t.color('green')
    if branch > 5:
        t.forward(branch)
        t.right(random.randrange(15,45))
        tree(branch-20, t)
        t.left(random.randrange(15,45)*2)


def tur():
    t = turtle.Turtle()
    w = turtle.Screen()

    t.up()
    t.goto(0,-100)
    t.down()

    t.left(90)

    tree(100, t)




    w.exitonclick()
