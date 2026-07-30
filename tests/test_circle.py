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

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2
        
        
       