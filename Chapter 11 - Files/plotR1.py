def calc_coef():
    sum, sum_sqx = 0, 0
    maxX, maxY = 0, 0
    minX, minY = 100, 100
    n = 0
    sum_x, sum_y = 0, 0

    xs = []

    with open("labdata.txt") as f:
        for l in f:
            points = l.split()
            x = int(points[0])
            y = int(points[1])
            xs.append([x, y])

            sum = sum + x*y
            sum_sqx = sum_sqx + x**2

            sum_x = sum_x + x
            sum_y = sum_y + y

            if maxX < x:
                maxX = x
            if maxY < y:
                maxY = y
            if minX > x:
                minX = x
            if minY > y:
                minY = y

            n = n + 1
    print(xs)
    meanX = sum_x / n
    meanY = sum_y / n

    m = (sum - n * meanX * meanY) / (sum_sqx - n * meanX ** 2)

    return meanX, meanY, maxX, maxY, minX, minY, m, xs

def plotRegression():

    meanX, meanY, maxX, maxY, minX, minY, m, xs  = calc_coef()

    def y(x):
        return meanY + m * (x - meanX)

    import turtle
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(minX - 10, minY - 10, maxX + 10, maxY + 10)

    # draw coordinates
    t.speed(10)
    t.up()
    t.goto(minX - 5, minY - 5)
    t.down()
    t.goto(maxX + 5, minY - 5)
    t.goto(minX - 5, minY - 5)
    t.goto(minX - 5, maxY + 5)

    # plot Regression
    t.up()
    t.goto(minX, y(minX))
    t.down()
    t.goto(maxX, y(maxY))

    # points
    for i in range(len(xs)):
        t.up()
        t.goto(xs[i][0], xs[i][1])
        t.down()
        t.stamp()

    wn.exitonclick()


plotRegression()
