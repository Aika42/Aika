import turtle
import random

def tree(branch, t):
    if branch > 50:
        t.color('brown')
    else:
        t.color('green')
    if branch > 20:
        t.forward(branch)
        t.right(20)
        tree(branch-20,t)
        t.backward(branch)
        t.left(40)
        tree(branch-20,t)



def tur():
    t = turtle.Turtle()
    w = turtle.Screen()

    t.up()
    t.goto(0,-100)
    t.down()

    t.left(90)

    tree(60, t)

    w.exitonclick()

tur()
