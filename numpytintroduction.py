# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 23:42:32 2024

@author: jberm
"""

#Intro to numpy
import numpy as np

array = np.array([[1,2,3,4], [5,6,7,8]], dtype=np.int64)
print(array, "\n")

#array of ones - 3 rows 4 columns
unos = np.ones((3,4))
print(unos, "\n")

#array of zeroes - 3 rows 4 columns
ceros = np.zeros((3,4))
print(ceros, "\n")

#array of random numbers
aleatorios = np.random.random((2,2))
print(aleatorios, "\n")

#empty array
vacia = np.empty((3,2))
print(vacia, "\n")

#only one value array
full = np.full((2,2),8)
print(full, "\n")

#array with uniform spaces
espacio1 = np.arange(0,30,5)
print(espacio1, "\n")

espacio2 = np.linspace(0,2,5)
print(espacio2, "\n")

#matriz identidad
identidad1 = np.eye(4,4)
print(identidad1, "\n")

identidad2 = np.identity(4)
print(identidad2, "\n")

print("inspeccionar Matrices \n")
#dimension de una matriz
a = np.array([(1,2,3),(4,5,6)])
print(a.ndim)

#conocer el tipo de datos
a = np.array([1,2,3])
print(a.dtype)

#conocer el tama;o y forma de la matriz
a = np.array([1,2,3,4,5,6])
print(a.size)
print(a.shape)

#cambio de forma de una matriz
a = np.array([(1,2,3),(4,5,6)])
print(a, "\n")
a = a.reshape(3,2)
print(a, "\n")

#extraer valores
a = np.array(([1,2,3,4],[3,4,5,6]))
print(a[0,2], "\n") #extraer un solo valor de la matriz - fila 0 columna 2
print(a[0:,2], "\n")#valores de la columna 3

#encontrar el minimo, maxio y la suma
a = np.array([2,4,8])
print(a.min(),"\n")
print(a.max(),"\n")
print(a.sum(),"\n")

#operaciones matematicas, raiz cuadrada y desviacion estandar
a = np.array([(1,2,3),(3,4,5)])
print(np.sqrt(a),"\n")
print(np.std(a), "\n")

#suma resta division y multiplicacion
x = np.array([(1,2,3),(3,4,5)])
y = np.array([(1,2,3),(3,4,5)])

print(x+y, "\n")
print(x-y, "\n")
print(x*y, "\n")
print(x/y, "\n")
























