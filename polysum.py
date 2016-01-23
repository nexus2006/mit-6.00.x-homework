'''
Polysum takes 2 arguments:
    num_sides = integer number of sides of a regular polygon
    len_sides = float length of each side of a regular polygon
and returns the sum of the area and the square of the perimeter
as a float, rounded to 4 decimal places, eg:

>>> polysum(4,4)
272.0
>>> polysum(8,19.5)
26172.0094
>>> polysum(7,2.333)
286.4805
'''
from math import tan, pi


def polysum(num_sides, len_sides):
    poly_sum = _poly_area(num_sides, len_sides) + \
               _poly_perim_square(num_sides, len_sides)
    return round(poly_sum, 4)


def _poly_area(num_sides, len_sides):
    return (0.25*num_sides*len_sides**2)/tan(pi/num_sides)


def _poly_perim_square(num_sides, len_sides):
    return (num_sides*len_sides)**2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print('DONE')

