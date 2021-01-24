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
        temp = self.W
        self.W = self.H
        self.H = temp

    def contains(self, P):
        if P.getY() < self.H and P.getX() and P.getY() >= 0 and P.getX() >= 0:
            return True
        else:
            return False



def test():
    b = Rectangle(Point(0,0), 6, 4)
    assert b.H == 4
    assert b.getWidth() == 6
    b.transpose()
    assert b.H == 6
    assert b.getWidth() == 4
    print("OK")

    c = Rectangle(Point(0,0), 8, 10)
    assert c.contains(Point(1,1)) == True
    assert c.contains(Point(1,0)) == True
    assert c.contains(Point(9,9)) == False
    print('tested')


test()


