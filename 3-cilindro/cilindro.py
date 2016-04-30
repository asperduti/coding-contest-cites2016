from math import sqrt, asin, pi

file = "cilindro.asc"

puntos = []

for line in open(file,"r"):
    puntos.append(line.split())

Mz = puntos[0]
mz = puntos[0]
mx = puntos[0]
Mx = puntos[0]

for p in puntos:
    if float(p[0]) > float(Mx[0]): Mx = p
    if float(p[0]) < float(mx[0]): mx = p
    if float(p[2]) > float(Mz[2]): Mz = p
    if float(p[2]) < float(mz[2]): mz = p
'''
print "El punto mas a la derecha es ", Mx
print "El punto mas a la izquierda es ", mx
print "El punto mas alto es ", Mz
print "El punto mas bajo es ", mz
'''

dx = pow(float(Mz[0])-float(mx[0]),2)
dy = pow(float(Mz[1])-float(mx[1]),2)
dz = pow(float(Mz[2])-float(mx[2]),2)
altura = sqrt(dx+dz)

dx = pow(float(Mz[0])-float(Mx[0]),2)
dy = pow(float(Mz[1])-float(Mx[1]),2)
dz = pow(float(Mz[2])-float(Mx[2]),2)
radio = sqrt(dx+dz)/2

dz = float(Mz[2])-float(mx[2])
angulo = pi/2 - asin(dz/altura)

print "La altura del cilindro es : %f" % (altura)
print "El radio del cilindro es : %f" % (radio)
print "El angulo(radianes) es : %f" % (angulo)
