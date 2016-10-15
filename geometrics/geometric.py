import math


__author__ = "Tobias Trabelsi"
__copyright__ = "GPLv3"
__version__ = "1.0"
__maintainer__ = "Tobias Trabelsi"
__email__ = "Tobias.Trabelsi@HS-Bochum.de"
__status__ = "Testing"

def calcCylinder(radius, height):
    diameter = radius*2
    ground = math.pow(radius, 2) * math.pi
    volume = ground * height
    girth = 2* math.pi * radius
    lateralSurface = girth * height
    surface = 2*ground+lateralSurface

    print("The Cylinder with a radius of ", radius, "and a height of ", height, "has the following atributes:")
    print("Diameter: \t \t \t %.2f" % round(diameter), "\t \t----------")
    print("Ground: \t \t \t %.2f" %  round(ground), "\t \t|        |")
    print("Volume: \t \t \t %.2f" % round(volume), "\t|        |")
    print("Girth: \t \t \t \t %.2f" % round(girth), "\t \t|        |")
    print("Lateral Surface: \t %.2f" % round(lateralSurface), "\t|        |")
    print("General Surface: \t %.2f"% round(surface), "\t----------")


def round(n, precision=0.05):
    correction = 0.5 if n >= 0 else -0.5
    return int( n/precision+correction ) * precision
