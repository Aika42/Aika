import turtle
import random

def tree(branch, t):
    if branch > 30:
        t.color('brown')
    else:
        t.color('green')
    if branch > 20:
        t.forward(branch)
        t.right(20)
        tree(branch-10,t)
        t.left(20)
        t.backward(branch)
        #t.left(20)






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
