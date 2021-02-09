import turtle
BUSH_LEN = 30

def bush(bushlen, t):
    """bush is three sticks with three sticks on each"""
    if bushlen < BUSH_LEN:
        return
    t.left(60)
    t.forward(bushlen)
    bush(bushlen-20, t)
    #t.left(60)
    t.backward(bushlen)

    t.right(60)
    t.forward(bushlen)
    bush(bushlen-20, t)
    t.backward(bushlen)
    t.right(60)
    t.forward(bushlen)
    bush(bushlen-20, t)
    t.backward(bushlen)




def tur():
    t = turtle.Turtle()
    t.speed(1)
    w = turtle.Screen()
    t.left(90)
    bush(60, t)


    w.exitonclick()

tur()
