# r = Rectangle(Point(4, 5), 6, 5). location of lower corner (4,5), width 6 and height 5

from point import Point


class Rectangle:

    def __init__(self, initP, initW, initH):
        self.P = initP
        self.W = initW
        self.H = initH

    def __str__(self):
        return 'Rectangle ' + str(self.P) + ', ' + str(self.W) + ', ' + str(self.H)

    def getwidth(self):
        return self.W

    def getheight(self):
        return self.H

    def area(self):
        return self.W * self.H

    def perimeter(self):
        return self.W + self.H + self.W + self.H

    def transpose(self):
        temp = self.W
        self.W = self.H
        self.H = temp

    def contains(self, p: Point):
        return self.H + self.P.getY() > p.getY() >= self.P.getY() and self.W + self.P.getX() > p.getX() >= self.P.getX()

    def diagonal(self):
        return (self.W ** 2 + self.H ** 2) ** 0.5


def test():
    b = Rectangle(Point(0, 0), 6, 4)
    assert b.H == 4
    assert b.getwidth() == 6
    b.transpose()
    assert b.H == 6
    assert b.getwidth() == 4
    print("OK")

    c = Rectangle(Point(0, 0), 8, 10)
    assert c.contains(Point(1, 1))


def test_0():
    c = Rectangle(Point(10, 5), 2, 2)
    assert not c.contains(Point(1, 1))
    assert c.contains(Point(11, 6))

    assert c.diagonal() == 8 ** 0.5
