class Point2D:
    def __init__(self, x, y):
        self.xCoordinate = x
        self.yCoordinate = y

    def __sub__(self, other):
        # Follow the same methodology as described in the addition section
        if type(other) == Point2D:
            resultant = Point2D((self.xCoordinate - other.xCoordinate), self.yCoordinate - other.yCoordinate)
            return resultant
        else:
            return "Error - Invalid operation"

    #Define the string (human readable) represetnation of our object
    def __str__(self):
        return "("+str(self.xCoordinate)+", "+str(self.yCoordinate)+")"
    #Set the representation of our object: the objects representaiton (unambigious)
    __repr__ = __str__

class Point3D:
    def __init__(self, x, y, z):
        self.xCoordinate = x
        self.yCoordinate = y
        self.zCoordinate = z

    def __sub__(self, other):
        # Follow the same methodology as described in the addition section
        if type(other) == Point3D:
            resultant = Point3D((self.xCoordinate - other.xCoordinate), (self.yCoordinate - other.yCoordinate), (self.zCoordinate - other.zCoordinate))
            return resultant
        else:
            return "Error - Invalid operation"

    #Define the string (human readable) represetnation of our object
    def __str__(self):
        return "("+str(self.xCoordinate)+", "+str(self.yCoordinate)+", "+str(self.zCoordinate)+")"
    #Set the representation of our object: the objects representaiton (unambigious)
    __repr__ = __str__

class Vector:
    def __init__(self, initial, terminal):
        self.initialPoint = initial
        self.finalPoint = terminal

    @property
    def direction (self):
        return self.finalPoint - self.initialPoint

    def __str__(self):
        if type(self.initialPoint) == Point2D:
            return "(" + str(self.xCoordinate) + ", " + str(self.yCoordinate) + ")"
        elif type(self.initialPoint) == Point3D:
            return "(" + str(self.xCoordinate) + ", " + str(self.yCoordinate) + ", " + str(self.zCoordinate) + ")"

    __repr__ = __str__
