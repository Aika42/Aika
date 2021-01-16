import math
import random
import turtle

def mountains():
    #t = turtle.Turtle()
    #w = turtle.Screen()

    x,y = values(-40, 65, 10, 400)

    print(x,y)

    #w.exitonclick()



def values(sl_min, sl_max, x1, x2):

    x3 = random.randrange(x1,x2)

    y_up1 = (x3 - x1)* math.tan(math.radians(sl_max)) # from y1 to max y3
    y_up2 = (x3 - x2)* math.tan(math.radians(sl_max)) # from y2 to max y3
    if y_up2 < y_up1:
        y_up = int(y_up2)
    else:
        y_up = int(y_up1)

    y_dw1 = (x3 - x1)* math.tan(math.radians(sl_min)) # from y2 to min y3
    y_dw2 = (x3 - x2)* math.tan(math.radians(sl_min)) # from y2 to min y3
    if y_dw2 > y_dw1:
        y_dw = int(y_dw2)
    else:
        y_dw = int(y_dw1)


    print(y_dw, y_up)

    y3 = random.randrange(y_up, y_dw)

    print(x3, y3)

    return x3, y3


mountains()




import math

