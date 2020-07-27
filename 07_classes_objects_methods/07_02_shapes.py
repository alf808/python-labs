'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
class Rectangle:
    """class that models a rectangle"""

    def __init__(self, length, width):
        """constructor with length and width"""
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return self.length * 2 + self.width * 2


class Circle:
    """class that models a circle"""

    PI = 3.14159

    def __init__(self, radius):
        """constructor with radius"""
        self.radius = radius

    def area(self):
        return self.PI * self.radius**2

    def circumference(self):
        return 2 * self.PI * self.radius


circ = Circle(3)
squ = Rectangle(2,2)
print(circ.circumference())
print(squ.area())