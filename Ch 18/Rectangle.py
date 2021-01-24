# r = Rectangle(Point(4, 5), 6, 5). location of lower corner (4,5), width 6 and height 5

class Point:
    """Point class shows point coordinates in x, y """
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"

    def getX(self):
        return self.x

    def getY(self):
        return self.y



a = Point(1,2)



class Rectangle:

    def __init__(self, initP, initW, initH):
        self.P = initP
        self.W = initW
        self.H = initH

    def __str__(self):
        return 'Rectangle '+str(self.P)+', '+str(self.W)+', '+str(self.H)

    def getWidth(self):
        return self.W

    def getHeight(self):
        return self.H

    def area(self):
        return self.W * self.H

    def perimeter(self):
        return self.W + self.H + self.W + self.H

    def transpose(self):
        self.W = self.H
        self.H = self.W


b = Rectangle(a, 6, 4)
b.getHeight()
