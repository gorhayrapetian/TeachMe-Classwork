from abc import ABC
from math import pi


r = int(input('Enter the radius of a circle: '))

a = int(input('Enter the length of a side of square: '))

b = int(input('Enter the length of leg of right triangle: '))

c = int(input('Enter the another leg length of right triangle: '))

class GeometricFigure(ABC):

    def get_perimeter(self):
        pass

    def get_area(self):
        pass

class Circle(GeometricFigure):

    def __init__(self, radius):
        self.radius = radius

    def get_perimeter(self): # circumference
        return 2 * self.radius * pi 

    def get_area(self):
        return self.radius ** 2 * pi

class Square(GeometricFigure):

    def __init__(self, side):
        self.side = side

    def get_perimeter(self):
        return 4 * self.side

    def get_area(self):
        return self.side ** 2 

circle_obj = Circle(int(r))

square_obj = Square(int(a))

list_of_figures = [circle_obj, square_obj]

for figure_obj in list_of_figures:
    print(figure_obj.get_perimeter())
    print(figure_obj.get_area())