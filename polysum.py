'''
A small module to sum the area and square of the perimeter of a
regular polygon.  Written for MIT 6.00.1x spring 2016 to demonstrate
basic programming concepts and correct style.

Conforms to PEP8, verified by pep8online.com.

Copyright Matt Caldwell 2016, GPLv3
'''
from math import tan, pi


def polysum(num_sides, len_sides):
    '''
    polysum takes 2 arguments:
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
    poly_sum = _poly_area(num_sides, len_sides) + \
        _poly_perim_square(num_sides, len_sides)
    return round(poly_sum, 4)


def _poly_area(num_sides, len_sides):
    '''
    private function, returns sum of a regular polygon
    '''
    return (0.25*num_sides*len_sides**2)/tan(pi/num_sides)


def _poly_perim_square(num_sides, len_sides):
    '''
    private function, returns square of the sum of side lengths of
    a regular polygon
    '''
    return (num_sides*len_sides)**2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print('DONE')

