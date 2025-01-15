from collections import namedtuple
from math import pi

def vector2(x, y):
    vec2 = namedtuple("vector2", ["x", "y"])
    vec2var = vec2(x, y)
    return vec2var

def vector3(x, y, z):
    vec3 = namedtuple("vector3", ["x", "y", "z"])
    vec3var = vec3(x, y, z)
    return vec3var

def rotation(x = 0, y = 0, z = 0, bRad = False):
    rot = namedtuple("rotation", ["x", "y", "z"])
    if(bRad == True):
        rotvar = rot(x*180/pi, y*180/pi, z*180/pi)
        return rotvar
    else:
        rotvar = rot(x, y, z)
        return rotvar

def fac(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result