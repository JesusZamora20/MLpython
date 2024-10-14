# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 00:14:01 2024

@author: jberm
"""

#Linear regresion con scikit learn

import numpy as np
from sklearn import datasets, linear_model
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt

housing = fetch_california_housing()

print(housing.keys(), "\n")

print("caracteristicas del dataset:")
print(housing.DESCR, "\n")

print("cantidad de datos")
print(housing.data.shape, '\n')

print("Nombres Columnas:")
print(housing.feature_names, "\n")

#preparando la regresion lineal simple

#seleccionando la columna que nos interesa

x = housing.data[:, np.newaxis,2]

#se definen los datos correspondientes a etiquetas
y = housing.target

#se grafican los datos
plt.scatter(x, y)
plt.xlabel("numero de habitaciones")
plt.ylabel("valor medio")
plt.show()


###### implementacion de la regresion lineal ########

from sklearn.model_selection import train_test_split

#se separan los datos de "train" en entrenamiento y prueba para probar los algoritmos
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.01)

#defino el algoritmo a usar
lr = linear_model. LinearRegression()

#se entrena el modelo
lr.fit(x_train, y_train)

#se realiza una prediccion
y_pred = lr.predict(x_test)

#graficamos los datos junto con el modelo
plt.scatter(x_test, y_test)
plt.plot(x_test, y_pred, color='red', linewidth=3)
plt.title('Regresion Lineal simple')
plt.xlabel('numero de habitaciones')
plt.ylabel('valor medio')
plt.show()

print()
print('DATOS DEL MODELO DE REGRESION LINEAL SIMPLE', '\n')
print('Valor de la pendiente o coeficiente a: ', lr.coef_, '\n')
print('valor de la interseccion o coeficiente b: ', lr.intercept_, '\n')
print('la ecuacion del algoritmo es: y =', lr.coef_, "x", lr.intercept_, '\n')
print("precision del modelo: ", lr.score(x_train, y_train))






