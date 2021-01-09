def mystery():
    # load points
    points = []
    with open('Mystery.txt') as f:
        for l in f:
            points.append(l.split())


    for i in range(len(points)-1):
        if points[i][0] == 'UP' or points[i][0] == 'DOWN':
            points[i] = points[i][0]
        else:
            points[i] = [int(points[i][0]),int(points[i][1])]

    print(points)
    import turtle
    wn = turtle.Screen()
    #wn.setworldcoordinates()

    fred = turtle.Turtle()

    for i in range(10):
        print(points[i][0],points[i][1])
        if points[i] == 'UP':
            fred.up()
        if points[i] == 'DOWN':
            fred.down()
        else:
            fred.goto(points[i][0],points[i][1])
            fred.stamp()

    wn.exitonclick()


mystery()

