import math
import random
import turtle

t = turtle.Turtle()
w = turtle.Screen()
w.screensize(1500,1500, 'light blue')

MIN_D = 10
MAXTAN = 70

def m(p1, p2):
    if dist(p1,p2) < MIN_D:
        t.goto(p2)
    else:
        p3 = findP(p1,p2)
        m(p1,p3)
        m(p3,p2)

def dist(p1,p2):
    x1, y1 = p1
    x2, y2 = p2

    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def findP(p1, p2)->tuple:
    x1, y1 = p1
    x2, y2 = p2

    x3 = random.uniform(x1, x2)
    tn = math.tan(math.radians(MAXTAN))

    y_up = min(y1 + (x3 - x1)*tn, y2 + (x2 - x3)*tn)
    y_dw = max(y1 - (x3 - x1)*tn, y2 - (x2 - x3)*tn)
    y_min = 0
    y_d = max(y_min, y_dw)
    print(x1, x3,x2, y_up, y_dw)

    y3 = random.uniform(y_d,y_up)

    return int(x3),int(y3)

p1 = -400,0
p2 = 400,0
t.up()
t.goto(p1)
t.down()
m(p1, p2)

w.exitonclick()