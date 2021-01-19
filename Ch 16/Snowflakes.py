def snowflake(n, t):
    """forward, left(60), forward, right(120), forward, left(60)"""
    t.left(60)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)

    t.up()
    t.backward(50)
    t.down()

    t.right(60)
    t.forward(100)
    t.right(120)
    t.forward(100)
    t.right(120)
    t.forward(100)




def t():
    import turtle
    wn = turtle.Screen()
    t = turtle.Turtle()

    t.up()
    t.goto(-100,-100)
    t.down()

    t.speed(1)

    snowflake(3, t)



    wn.exitonclick()

t()

