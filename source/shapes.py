import math

#parent class
class Shape:


    def area(self):
        pass

    def perimeter(self):
        pass

#inheritance the Shape class
#Circle class automatically gets everything Shape has, and can override the empty pass methods with real implementaions
class Circle(Shape):

    #run automatically once, at the exact moement a new Circle object is created
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius