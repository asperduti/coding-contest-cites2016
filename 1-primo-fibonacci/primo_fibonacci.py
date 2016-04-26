# -*- coding: UTF-8 -*-

from math import sqrt
from  random import randrange
import sys

# Implementacion del test Miller-Rabin https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
# Fuente: http://stackoverflow.com/a/14616936/6029880
def probably_prime(n, k):
    """Return True if n passes k rounds of the Miller-Rabin primality
    test (and is probably prime). Return False if n is proved to be
    composite.
    """
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31] # etc.

    if n < 2: return False
    for p in small_primes:
        if n < p * p: return True
        if n % p == 0: return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


# Devuelvo el numero de fibonacci. No es correcto para numeros altos
def fibonacci(n):
    srqt5 = sqrt(5)
    return ((1+srqt5)**n-(1-srqt5)**n)/(2**n*srqt5)

# Devuelvo el numero de fibonacci. Muy rapido para numeros grandes
def fib(n):
    i = n - 1
    a, b = 1, 0
    c, d = 0, 1
    while i > 0:
        if (i % 2) != 0:
            a , b = d*b+c*a,d*(b+a)+c*b
        c,d = c*c + d*d, d*(2*c+d)
        i = i / 2
    return a+b

if __name__ == "__main__":
    try:
        n=int(sys.argv[1])
        fn = 0
        primos = []
        for num in range(1,n+1):
            fn=fib(num)
            if probably_prime(fn,7):
                primos.append(num)

        print "Los numeros f(n) primos para n <= %d son: " % (n), primos
        print "El numero fn(%d) tiene %d cifras" % (n, (len(str(fn))))
    except:
        print "Debe ingresar un numero entero"
