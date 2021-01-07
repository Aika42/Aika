def plotRegression():
    f = open('labdata.txt','r')
    d = {}
    for line in f:
        d[line[0:2]] = line[3:5]

    mX, mY = 0, 0
    n = 0
    sumXY = 0
    sumX = 0
    minX, minY = 100, 100
    maxX, maxY = -1, -1

    for key, value in d.items():

        n = n + 1
        mX = mX + int(key)
        mY = mY + int(value)

        sumXY = sumXY + int(key)*int(value)

        sq_sumX = sumX + int(key)**2

        if int(key) < minX:
            minX = int(key)

        if int(value) < minY:
            minY = int(value)

        if int(key) > maxX:
            maxX = int(key)

        if int(value) > maxY:
            maxY = int(value)

    meanX = mX / n
    meanY = mY / n
    m = (sumXY - n * meanX * meanY) / (sq_sumX - n * meanX**2)

    return minX, maxX, minY, maxY, m, meanX, meanY



f = plotRegression()

def fred(f):

    minX, maxX, minY, maxY, m, meanX, meanY = f

    import turtle
    wn = turtle.Screen()
    wn.setworldcoordinates(minX-10, minY-10, maxX+10, maxY+10)

    fred1 = turtle.Turtle()

    for x in range(minX, maxX, 2):
        y = meanY + m * (x-meanX)
        fred1.goto(x,y)

    wn.exitonclick()

fred(f)