def calc_coeff():
    f = open('labdata.txt', 'r')
    d = {}
    for line in f:
        d[line[0:2]] = line[3:5]

    k = []
    v = []
    sumXY = 0

    for key, value in d.items():

        k.append(int(key))
        v.append(int(value))
        sumXY = sumXY + int(key)*int(value)

    sq_sumX = sum([i**2 for i in k])
    maxX, maxY = max(k), max(k)
    minX, minY = min(v), min(v)

    mX = sum(k)
    mY = sum(v)
    n = len(k)

    meanX = mX / n
    meanY = mY / n
    m = (sumXY - n * meanX * meanY) / (sq_sumX - n * meanX**2)

    return minX, maxX, minY, maxY, m, meanX, meanY, d


def plotRegression():

    minX, maxX, minY, maxY, m, meanX, meanY, d = calc_coeff()

    def y(x): return meanY + m * (x-meanX)

    import turtle
    wn = turtle.Screen()
    wn.setworldcoordinates(minX-10, minY-10, maxX+10, maxY+10)

    fred = turtle.Turtle()

    # draw coordinates
    fred.up()
    fred.goto(minX-5, minY-5)
    fred.down()
    fred.goto(maxX+5, minY-5)
    fred.goto(minX-5, minY-5)
    fred.goto(minX-5, maxY+5)

    # plot Regression
    fred.up()
    fred.goto(minX, y(minX))
    fred.down()
    fred.goto(maxX, y(maxY))

    # points
    for i,j in d.items():
        i = int(i)
        j = int(j)
        fred.up()
        fred.goto(i,j)
        fred.down()
        fred.stamp()

    wn.exitonclick()

#plotRegression()

