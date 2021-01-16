import math
import random
import turtle

def mountains(x1, y1, x2, y2):
    t = turtle.Turtle()
    w = turtle.Screen()

    x3, y3 = values(-45, 45, x1, x2, y1, y2)

    d1 = x3 - x1
    d2 = x2 - x3

    if d1 < 25:
        t.up()
        t.goto(x1,y1)
        t.down()
        t.goto(x3,y3)
        return
    else:
        mountains(x1, y1, x3, y3)

    if d2 < 25:
        t.up()
        t.goto(x3, y3)
        t.down()
        t.goto(x2, y2)
        return
    else:
        mountains(x3, y3, x2, y2)


    w.exitonclick()



def values(smin, smax, x1, x2, y1, y2):

    x3 = random.randrange(x1,x2)

    y_up1 = y1 + (x3 - x1)* math.tan(math.radians(smax)) # from y1 to max y3
    y_up2 = y1 + (x2 - x3)* math.tan(math.radians(smax)) # from y2 to max y3
    y_up = int(min(y_up2, y_up1))


    y_dw1 = y2 + (x3 - x1)* math.tan(math.radians(smin)) # from y2 to min y3
    y_dw2 = y2 + (x2 - x3)* math.tan(math.radians(smin)) # from y2 to min y3
    y_dw = int(min(y_dw2, y_dw1))

    print("y_dw and y_up are ", y_dw, y_up)

    y3 = random.randrange(y_dw, y_up)

    print("x3 and y3 are ", x3, y3)

    return x3, y3

x1, x2 = 10, 400
y1, y2 = 85, 150
mountains(x1, x2, y1, y2)



