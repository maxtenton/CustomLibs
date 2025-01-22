from collections import namedtuple
from math import pi, sqrt

class SpatialMath:

    global vec2
    vec2 = namedtuple("vector2", ["x", "y"])
    global vec3
    vec3 = namedtuple("vector3", ["x", "y", "z"])
    global rot
    rot = namedtuple("rotation", ["x", "y", "z"])

    def vector2(x, y):
        vec2var = vec2(x, y)
        return vec2var

    def vector3(x, y, z):
        vec3var = vec3(x, y, z)
        return vec3var

    def rotation(x = 0, y = 0, z = 0, bRad = False):
        if(bRad == True):
            rotvar = rot(x*180/pi, y*180/pi, z*180/pi)
            return rotvar
        else:
            rotvar = rot(x, y, z)
            return rotvar
        
class Math:
    
    def fac(n):
        result = 1
        for i in range(1, n+1):
            result = result * i
        return result