import pytest
import source.shapes as shapes
import math

class TestCircle:

    #Set up Method to run before each test
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

     #Tear Down Method run teardown code after each method
    def teardown_method(self, method):
        print(f"Tearing down {method}")
        #not needed but it is automatic
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        result = self.circle.perimeter()

        expected = 2 * math.pi * self.circle.radius

        assert result == expected

    #using my_rectangle fixture from conftest.py
    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()
    