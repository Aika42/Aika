
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





