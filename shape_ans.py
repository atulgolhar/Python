#!/usr/bin/env python3
#shape_ans.py


"""
>>> import shape_ans
>>> a = shape_ans.Point()
>>> repr(a)
'Point(0, 0)'
>>> b = shape_ans.Point(3,4)
>>> b.distance_from_origin()
5.0
"""

import math
import cmath

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y 

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    def __add__(self, other):               #p = q + r  Point.__add__()
        return Point(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):              #p += q  Point.__iadd__()
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):               #p = q - r  Point.__sub__()
        return Point(self.x - other.x, self.y - other.y)

    def __isub__(self, other):              #p -= q  Point.__isub__()
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):               #p = q * n   Point.__mul__()
        return Point(self.x * other, self.y * other)

    def __imul__(self, other):              #p *= n  Point.__imul__()
        self.x *= other
        self.y *= other
        return self

    def __truediv__(self, other):           #p = q / n  Point.__truediv__()
        return Point(self.x / other, self.y / other)

    def __itruediv__(self, other):   #p /= n   Point.__itruediv__()
        self.x /= other
        self.y /= other
        return self

    def __floordiv__(self, other):          #p = q // n   Point.__floordiv__()
        return Point(self.x // other, self.y // other)

    def __ifloordiv__(self, other):         #p //= n   Point.__ifloordiv__() 
        self.x //= other
        self.y //= other
        return self

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)

    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)

class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)

    def __repr__(self):
        return "Circle({0.radius!r}, {0.x!r}, {0.y!r})".format(self)

    def __str__(self):
        return repr(self)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
