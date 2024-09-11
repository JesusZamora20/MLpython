# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:42:47 2024

@author: jberm
"""
import numpy as np
import pandas as pd

#crear un dataframe
data = np.array([['', 'Col1','Col2'], ['Fila1',11,22], ['Fila2',33,44]])
print(pd.DataFrame(data=data[1:,1:], index=data[1:,0], columns=data[0,1:]), "\n")

df = pd.DataFrame(np.array([[1,2,3], [4,5,6], [7,8,9]]))
print('Dataframe:')
print(df, "\n")

#crear una serie
serie = pd.Series({"Argentina":"Buenos aires",
                 "Chile":"Santiago de Chile",
                 "Colombia": "Bogota",
                 "Peru":"Lima"})

print('Series:')
print(serie, "\n")

#forma del dataframe
print('forma del Dataframe:')
print(df.shape, "\n")

#altura del dataframe
print('altura del Dataframe:')
print(len(df.index), "\n")

#Estadisticas del dataframe
print('Estadisticas del Dataframe:')
print(df.describe(), "\n")

#Correlacion del dataframe
print('Correlacion del Dataframe:')
print(df.corr(), "\n")

#conteo de los datos del dataframe
print('conteo de los datos del Dataframe:')
print(df.count(), "\n")

#Valor mas alto de cada columna del dataframe
print('Valor mas alto de cada columna del Dataframe:')
print(df.max(), "\n")

#Valor mas bajo de cada columna del dataframe
print('Valor mas bajo de cada columna del Dataframe:')
print(df.min(), "\n")

#Mediana de cada columna del dataframe
print('Mediana de cada columna del Dataframe:')
print(df.median(), "\n")

#desviacion estandar de cada columna del dataframe
print('desviacion estandar de cada columna del Dataframe:')
print(df.std(), "\n")

#Seleccionar primer columna del dataframe
print('Seleccionar primer columna del Dataframe:')
print(df[0], "\n")

#Seleccionar dos columnas del dataframe
print('Seleccionar dos columna del Dataframe:')
print(df[[0,1]], "\n")

#Seleccionar valor de la primera fila y ultima columna del dataframe
print('Seleccionar valor de la primera fila y ultima columna del Dataframe:')
print(df.iloc[0][1], "\n")

#Seleccionar valor de la primera fila del dataframe
print('Seleccionar valores de la primera fila del Dataframe:')
print(df.iloc[0,:], "\n")

#verificar si hay datos nulos en el dataframe
print('Datos nulos en el DataFrame:')
print(df.isnull())

#Suma de datos nulos en el dataframe
print('suma de Datos nulos en el DataFrame:')
print(df.isnull().sum())

#reemplaza los valores perdidos por la media
print('reemplaza los valores perdidos por la media:')
print(df.fillna(df.mean()))






















