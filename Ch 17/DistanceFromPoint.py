# Add a distanceFromPoint method that works similar to
# distanceFromOrigin except that it takes a
# Point as a parameter and computes the distance between that point and self.
class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y


    def distanceFromPoint(self, p):
        return ((self.x - p.getX())**2 + (self.y - p.getY())**2)**0.5

# Add a method reflect_x to Point which returns a new Point,
# one which is the reflection of the point about the x-axis.

    def reflect_x(self):
        return (self.x, - self.y)

# Add a method slope_from_origin which returns the slope of the line joining the origin to the point.
# What cases will cause your method to fail? Return None when it happens.
    def slope_from_origin(self):
        if self.y == 0:
            return None
        return self.y / self.x


a = Point(2,6)
a.slope_from_origin()


