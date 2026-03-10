import pandas as pd
import numpy as np
from numpy import random

 # # Tipos de arrays
array_0 = np.array(5)
print(array_0)

array_1 = np.array([1,2,3,4,5,6])
print(array_1)

array_2 = np.array([[1,2,3],[4,5,6]])
print(array_2)

array_3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(array_3)

 # # Arrays llamadas
 # print(array_1[0])
 # print(array_2[1][1])  # fila, columna
 # print(array_3[0][1][1])  # dimensión, fila, columna

 # # shape
 # print(array_1.shape)
 # print(array_2.shape)
 # print(array_3.shape)

 # # reshape
 # print(array_1.reshape(1,6))
 # print(array_2.reshape(3,2))
 # print(array_3.reshape(2,3,2))

 # #Concatenacion
 # print(np.concatenate((array_1,array_1)))

 # #Split
# print(np.split(array_1,3))


#where
print(np.where(array_1 == 3))
arrayN = np.array([10,50,2,0,7,6])
print(np.sort(arrayN))

print(np.sort(arrayN)[::-1])


#Randmoa
numero = random.randit(100,200,1) #(Inico,fin, num ELEMENTOS)
print(numero)

numero = random.radint(10, size=(5))
print(numero)


numero = random.radiant(10 size=(2,3))
print(numero)

#Numeros deciamles]
numero = random.rand()
print(numero)

print(round(numero,2))

numero2 = random.rand() + 5
print(numero2)

numero3 = random.rand(3,5)
print(numero3)

#Listas
lista_nombres = ["Juan", "Pedro", "Maria"]
print(random.choice(lista_nombres))


#Ejercicio1 

# Array de 10 números enteros aleatorios entre 0 y 100
array1 = np.random.randint(0, 101, 10)
print("1:", array1)


#  Array de 5 números decimales aleatorios entre 0 y 1
array2 = np.random.random(5)
print("2:", array2)


#  Dos arrays aleatorios de longitud 5 y concatenarlos
a = np.random.randint(0, 100, 5)
b = np.random.randint(0, 100, 5)
concatenado = np.concatenate((a, b))
print("3:")
print("Array A:", a)
print("Array B:", b)
print("Concatenado:", concatenado)


# array de 10 números y dividirlo en dos arrays de 5
array4 = np.random.randint(0, 100, 10)
split_arrays = np.split(array4, 2)
print("4:")
print("Original:", array4)
print("Parte 1:", split_arrays[0])
print("Parte 2:", split_arrays[1])


# Matriz 3x3 con decimales entre 0 y 1
matriz = np.random.random((3,3))
print("5:")
print(matriz)


# Array de 10 números y seleccionar 3 al azar
array6 = np.random.randint(0, 100, 10)
seleccion = np.random.choice(array6, 3)
print("6:")
print("Array:", array6)
print("3 al azar:", seleccion)


#  Array de 10 números y calcular la media
array7 = np.random.randint(0, 101, 10)
media = np.mean(array7)
print("7:")
print("Array:", array7)
print("Media:", media)