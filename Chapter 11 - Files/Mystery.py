def mystery():
    import turtle
    wn = turtle.Screen()
    t = turtle.Turtle()

    # load points
    with open('Mystery.txt') as f:
        for l in f:
            points = l.split()
            if points[0] == 'UP':
                t.up()
            elif points[0] == 'DOWN':
                t.down()
            else:
                t.goto(int(points[0]),int(points[1]))
                t.stamp()

    wn.exitonclick()


mystery()

