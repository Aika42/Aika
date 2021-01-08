def calc_coef(points):
    k = points.keys()
    v = points.values()
    sumXY = sum(x * y for x, y in points.items())
    sq_sumX = sum([i ** 2 for i in k])

    maxX, maxY = max(k), max(v)
    minX, minY = min(k), min(v)

    n = len(k)

    meanX = sum(k) / n
    meanY = sum(v) / n
    m = (sumXY - n * meanX * meanY) / (sq_sumX - n * meanX ** 2)

    return minX, maxX, minY, maxY, m, meanX, meanY


def test_plotRegression():
    # load points
    points = {}
    with open("./labdata.txt") as f:
        for l in f:
            points[int(l[0:2])] = int(l[3:5])

    minX, maxX, minY, maxY, m, meanX, meanY = calc_coef(points)

    def y(x):
        return meanY + m * (x - meanX)

    import turtle

    wn = turtle.Screen()
    wn.setworldcoordinates(minX - 10, minY - 10, maxX + 10, maxY + 10)

    fred = turtle.Turtle()

    # draw coordinates
    fred.up()
    fred.goto(minX - 5, minY - 5)
    fred.down()
    fred.goto(maxX + 5, minY - 5)
    fred.goto(minX - 5, minY - 5)
    fred.goto(minX - 5, maxY + 5)

    # plot Regression
    fred.up()
    fred.goto(minX, y(minX))
    fred.down()
    fred.goto(maxX, y(maxY))

    # points
    for i, j in points.items():
        i = int(i)
        j = int(j)
        fred.up()
        fred.goto(i, j)
        fred.down()
        fred.stamp()

    wn.exitonclick()


# plotRegression()
