# -*- coding: utf-8 -*-
"""
@author: Aitor Donado.
"""

from funciones.circulo import area, perimetro


# Si el archivo .py estuviera más arriba en el arbol de carpetas:
# from ..funciones.circulo import area
perimetro(5)
area(5)

import funciones.circulo as circulo

circulo.perimetro(5)
circulo.area(5)


# Dos formas de hacer accesible el módulo circulo
# 1. Cambiando el directorio de trabajo
import os
os.chdir(r"/home/laptop/Proyectos Python/Introduccion_Python/funciones/")
# Ya se puede importar
import circulo
os.chdir(r"/home/laptop/Proyectos Python/python_c2b/")

# 2. Añadiendo la ubicación del directorio en el que está circulo al path
import sys
print(sys.path)
sys.path.append(r"/home/laptop/Proyectos Python/Introduccion_Python/funciones/")
# Ya se puede importar
import circulo


# Cargarmos un archivo de python creado.
# En ese archivo hemos definido las funciones que necesitamos.
# Tienen que estar en la misma carpeta.
print(circulo.area(5))
print(circulo.perimetro(5))

area(4)
perimetro(35)


# Otra forma de posibilitar la importación es introducir la ubicación en el path
import sys
sys.path
sys.path.append(r'/home/laptop/Proyectos Python/Introduccion_Python/funciones')
sys.path

import circulo as cir

cir.area(3)

print(cir.area(25))
print(cir.perimetro(35))


#############################
# Leer un archivo de texto. #
#############################
# Observar los modos de apertura
'''
"r" - Lectura - Valor predeterminado. Abre un archivo para lectura, error si el archivo no existe
"a" - Agregar - Abre un archivo para agregar, crea el archivo si no existe
"w" - Escribir - Abre un archivo para escribir, crea el archivo si no existe
"x" - Create - Crea el archivo especificado, devuelve un error si el archivo existe
'''

fichero = open(r"datos/quijote.txt", encoding = "utf8")
# Contenido como string
libro = fichero.read()

type(libro)
print(libro[:2000])

fichero.seek(0)

lineas = fichero.readlines()
type(lineas)
len(lineas)

print(lineas[:20])

fichero.close()

libro.count("Sancho")
libro.count("Quijote")
libro.count("Dulcinea")


print(libro[5000:6000])
libro[5000:6000]

libro = libro.replace("\n", " ")
print(libro[5000:6000])

libro = libro.replace("\n\n", "Salt0Renglon")
libro[5000:6000]
libro = libro.replace("\n", " ")
libro[5000:6000]
libro = libro.replace("Salt0Renglon", "\n\n")
libro[5000:6000]
print(libro[5000:6000])


# Añadir un nombre a un fichero de texto. Si no existe, se crea.
fichero = open("datos/nombres.txt", "w")
fichero.write('Ekaitz' + '\n')
fichero.close()

fichero = open("datos/nombres.txt", "a")
fichero.write('Íñigo' + '\n')
fichero.close()


from datetime import datetime

datetime.now()

with open("datos/nombres.txt", "a") as fichero:   
    fichero.write(f"Hola son las {datetime.now()}\n")


fichero = open("datos/nombres.txt", "r")
lineas = fichero.readlines()
fichero.seek(0)
contenido = fichero.read()
fichero.close()
print(contenido)
print(lineas)
# Ventaja de usar una estructura with al abrir un archivo
"""
Se asegura que el archivo se cerrará automáticamente al finalizar el bloque de código 
dentro de la estructura with, incluso si se produce un error o una excepción durante 
la ejecución del código. Esto evita que el archivo quede abierto accidentalmente, 
lo que podría causar problemas de rendimiento o corrupción de datos.
"""

with open('datos/quijote.txt', 'r', encoding="utf8") as archivo:
    contenido = archivo.read()

print(archivo)
print(contenido[:300])

# Usando el puntero
with open('datos/nombres.txt', 'r', encoding="utf8") as archivo:
    archivo.seek(2)   # Puntero al principio
    contenido2 = archivo.read(7)

print(contenido2)

#########################
# Lectura con escritura #
#########################

# Se puede abrir un fichero en modo lectura con escritura,
# pero éste debe existir previamente.
# Además por defecto el puntero estará al principio y si escribimos algo
# sobreescribiremos el contenido actual

# Creamos un fichero de prueba con 4 líneas
fichero = open('datos/fichero2.txt', 'w')
texto = "Línea 1\nLínea 2\nLínea 3\nLínea 4"
fichero.write(texto)
fichero.close()

# Lo abrimos en lectura con escritura y escribimos algo
fichero = open('datos/fichero2.txt', 'r+')
fichero.write("0123456789")
fichero.close()

with open('datos/fichero2.txt', 'r', encoding="utf8") as archivo:
    print(archivo.read())


# Volvemos a poner el puntero al inicio y leemos hasta el final
fichero = open('datos/fichero2.txt', 'r')   
fichero.seek(0)
print(fichero.read())
fichero.close()

########################
# Modificar una línea  #
########################
"""
Para lograr este fin lo mejor es 
    leer todas las líneas en una lista, 
    modificar la línea en la lista, 
    posicionar el puntero al principio y 
    reescribir de nuevo todas las líneas:
"""

fichero = open('datos/fichero2.txt', 'r+')
texto = fichero.readlines()

# Modificamos la línea que queramos a partir del índice
texto[1] = "Esta es la línea 2 modificada\n"

# Volvemos a poner el puntero al inicio y reescribimos
fichero.seek(0)
fichero.writelines(texto)
fichero.close()

# Leemos el fichero de nuevo
with open("datos/fichero2.txt", "r") as fichero:
    print(fichero.read())


