import turtle

def circle(r, t):
    if r > 1:
        t.up()
        t.goto(0,-(r-5))
        t.down()
        t.circle(r)
        circle(r-10, t)

def tur():
    t = turtle.Turtle()
    w = turtle.Screen()
    w.setworldcoordinates(-120,-120,120,120)
    t.speed(10)

    circle(100, t)

    w.exitonclick()

# tur()





