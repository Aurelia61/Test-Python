# coding: utf-8

# import modul
from math import *

class Circle():
    """
        Class for Circle
    """

    def __init__(self, x_circle, y_circle, radius):
        """
            contructor of circle class
        """

        # coordonates of the circle center
        self.x = x_circle
        self.y = y_circle
        # radius of the circle
        self.radius = radius

    def perimeter(self):
        """
            calculate the perimeter of a circle
        """
        # return the perimeter
        return 2*pi*self.radius

    def surface(self):
        """
            calculate the surface of a circle
        """
        # return the surface 
        return pi*self.radius**2

    def test_belong(self, x_point, y_point):
        """
            check if a point belongs to the circle
        """
        # return true if the point belongs to the circle
        return (x_point-self.x)**2 + (y_point-self.y)**2 == self.radius**2


if __name__ == "__main__":
    my_circle = Circle(0,0,1)
    print(f"\nLe périmetre du cercle est : {my_circle.perimeter()}\n")
    print(f"La surface de mon cercle est : {my_circle.surface()}\n")
    print(f"Test d'appartenance du point A de coordonnées (0,1): {my_circle.test_belong(0,1)}\n")
    print(f"Test d'appartenance du point B de coordonnées (1,1): {my_circle.test_belong(1,1)}\n")
