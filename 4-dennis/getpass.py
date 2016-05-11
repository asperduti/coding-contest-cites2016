# -*- coding: UTF-8 -*-
import crypt
from time import time
import sys

# Alfabeto del diccionario
alfabeto = 'abcdefghijklmnopqrstuvwxyz'

#Longitud maxima para del pass
longitud = 6

def dehash():
    time1=time()

    print "Se va a realizar ataque por diccionario"
    files = ["john.txt", "/etc/dictionaries-common/words"]
    for file in files:
        print "Se usa el diccionario %s" %(file)
        #for line in open(file,"r"):
        try:
            with open(file,"r") as (infile):
                for line in infile:
                    #Testing de hash
                    line = line.replace("\n","").lower()
                    if len(line) <= longitud:
                        for item in lista:
                            salt_hash = item[1]
                            if crypt.crypt(line,salt_hash) == salt_hash:
                                lista.remove(item)
                                print "El password para %s es %s" % (salt_hash, line)
                                time2=time()
                                print "Enlapsed time: ", time2-time1
                                if len(lista) == 0:
                                    return
        except IOError:
            print "No se pudo abrir el diccionario"


    print "Se va a realizar ataque por fuerza bruta"
    #inicializo diccionario, se usa si no se encuentra nada en los archivos
    diccionario = list(alfabeto)
    for l in range(longitud-1):
        tmp = diccionario
        diccionario = []
        for passw in tmp:
                for a in alfabeto:

                    #Si es es la long maxima no guardo en memoria el diccionario
                    if l != longitud-1:
                        diccionario.append(passw+a)

                    #Testing de hash
                    for item in lista:
                        salt_hash = item[1]
                        if crypt.crypt(passw+a,salt_hash) == salt_hash:
                            lista.remove(item)
                            print "Password: "+passw+a
                            time2=time()
                            print "Enlapsed time: ", time2-time1
                            if len(lista) == 0:
                                return
if __name__ == "__main__":
    try:
        shadowfile = open(sys.argv[1],"r")
        lista = []
        passwords = []

        for line in shadowfile:
            if raw_input("Desea crackear " +line+"[s/n]")=='s':
                lista.append(line.split(":"))

        print "Se va intentar crackear %d hashes con una longitud maxima por password de %d" % (len(lista),longitud)

        dehash()
    except IOError:
        print "No se pudo abrir el archivo"
