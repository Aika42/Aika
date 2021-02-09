from point import Point
from test_rectangle import Rectangle


def collision(r1: Rectangle, r2: Rectangle) -> bool:
    p11 = Point(r2.W, r2.H)
    p12 = Point(r2.W + r2.P.getX(), r2.H)
    p21 = Point(r2.W, r2.H + r2.P.getY())
    p22 = Point(r2.W + r2.P.getX(), r2.H + r2.P.getY())

    return r1.contains(p11) and r1.contains(p12) and r1.contains(p21) and r1.contains(p22)


def test_collision():
    p1 = Point(0, 0)
    p2 = Point(10, 10)
    r1 = Rectangle(p1, 8, 4)
    r2 = Rectangle(p2, 3, 2)
    assert collision(r1, r2) is False

    r9 = Rectangle(Point(4, 4), 8, 4)
    r3 = Rectangle(Point(0, 0), 8, 4)
    assert collision(r9, r3) is True
