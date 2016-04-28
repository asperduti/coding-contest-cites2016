# -*- coding: UTF-8 -*-

'''
 Un perrito esta atado a dos postes A y B separados una distancia unitaria con
 dos correas. Cada correa tiene longitud uno.
 Un pajarito esta atado a dos puntos C y D separados una distancia unitaria con
 dos piolines. Cada piolin tiene longitud uno.
 a. ¿Sobre que superficie puede moverse el perrito?
 b. ¿Sobre que volumen puede moverse el pajarito?
'''

from math import pi, sin, pow
import sys

try:
    R = float(sys.argv[1])
    titha=2*pi/3
    Area=pow(R,2)*(titha-sin(titha))
    print "a. El perro se puede mover en un area de %f" % (Area)

    vol = pow(R,3)*pi*5/12
    print "b. El pajaro se puede mover en un volumen de %f" % (vol)
except:
        print ("Se debe pasar como argumento un numero")
