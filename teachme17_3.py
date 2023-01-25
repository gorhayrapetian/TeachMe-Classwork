from abc import ABC
from cmath import sqrt

b = int(input('Enter the length of the opposite leg of right triangle: '))

c = int(input('Enter the length of adjacent leg of right triangle: '))

class GeometricFigure(ABC):

    def get_perimeter(self):
        pass

    def get_area(self):
        pass

class RightTriangle(GeometricFigure):

    def __init__(self, lega, legb):
        self.lega = lega
        self.legb = legb
        self.hypotenuse = int((((self.lega ** 2) + (self.legb ** 2))) ** 0.5)
        # self.hypotenuse = 5


    def get_perimeter(self):
        return self.lega + self.legb + self.hypotenuse

triangle_obj = RightTriangle(int(b), int(c))

print(triangle_obj.get_perimeter())