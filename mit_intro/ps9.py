# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
class Triangle(Shape):
    def __init__(self, b, h):
        """
        h: height
        b: base
        """
        self.height = float(h)
        self.base = float(b)
    def area(self):
        """
        Returns area of the triangle
        """
        return (self.base*self.height)/2.0
    def __str__(self):
        return 'Triangle with base ' + str(self.base) + ' and height ' + str(self.height)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Triangle and self.base == other.base and self.height == other.height

#
# Problem 2: Create the ShapeSet class
#

class ShapeSet(object):
    def __init__(self):
        """
        shapes: list of shapes in the set
        place: position for iteration
        """
        self.shapes = []
        self.place = None
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        for shape in self.shapes:
            if shape == sh: raise ValueError('duplicate')
        self.shapes.append(sh)
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        self.place=0
        return self
    def next(self):
        if self.place>=len(self.shapes): raise StopIteration()
        self.place += 1
        return self.shapes[self.place-1]      
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        strings =''
        for shape in self.shapes:
            if type(shape) == Circle:
                strings = strings + str(shape) + "\n"
        for shape in self.shapes:
            if type(shape) == Square:
                strings = strings + str(shape) + "\n"
        for shape in self.shapes:
            if type(shape) == Triangle:
                strings = strings + str(shape) + "\n"
        return strings
        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(ss):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    largest =()
    currMax = ss.shapes[0]
    for i in range (1, len(ss.shapes)):
        if ss.shapes[i].area()>currMax.area():
            currMax = ss.shapes[i]
    largest = (currMax,)
    for shape in ss.shapes:
        newElem = ()
        if shape.area() == currMax.area() and shape != currMax:
            newElem = (shape,)
            largest = largest + newElem
    return largest

#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    inputFile = open(filename, 'r')
    ss = ShapeSet()
    for line in inputFile:
        words = line.rsplit(',')
        if words[0]=='circle':
            r = float(words[1])
            ss.addShape(Circle(r))
        elif words[0]=='square':
            h = float(words[1])
            ss.addShape(Square(h))
        elif words[0]=='triangle':
            b = float(words[1])
            h = float(words[2])
            ss.addShape(Triangle(b,h))
    return ss




t = Triangle(6,6)
ss = ShapeSet()
ss.addShape(t)
ss.addShape(Triangle(1.2,2.5))
ss.addShape(Circle(4))
ss.addShape(Square(3.6))
ss.addShape(Triangle(1.6,6.4))
ss.addShape(Circle(2.2))
ss.addShape(Triangle(100, 2))
ss.addShape(Square(10))
print(ss)
largest = findLargest(ss)
largest
for e in largest: print(e)

ss2 = readShapesFromFile("shapes.txt")
ss2
print (ss2)
