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

#second shape class
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    #override define of "=" sign 
    def __eq__(self, other):
        #if its not a rectangle then we will return false
        if not isinstance(other, Rectangle):
            return False
        return self.width == other.width and self.length == other.length

    
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length*2) + (self.width*2)

#inherit from rectangle class to make square class
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length,side_length)