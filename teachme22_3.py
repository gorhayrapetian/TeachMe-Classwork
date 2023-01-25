from collections import namedtuple
from math import sqrt

# distance between two points 

Point = namedtuple('Point', ['x', 'y'],) # making two points from this

def distance(point_1, point_2):
    
    distance = sqrt((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) 
    return distance

my_point_1 = Point(5, 3)
    
my_point_2 = Point(4, 6)

print(distance(my_point_1, my_point_2))