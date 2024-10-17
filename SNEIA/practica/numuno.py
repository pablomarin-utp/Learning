#ejericicio 2.1
import numpy as np

def lista_a_arreglo(lista):
  return np.array(lista)

print(lista_a_arreglo([25, 45, 5, 23, 59]))

#ejercicio 2
def media_columna(matriz, columna):
  return np.mean(matriz[:,columna])

matriz_ejemplo = np.array([[1, 2, 3], 
                           [4, 5, 6], 
                           [7, 8, 9]])
columna_ejemplo = 0

print(media_columna(matriz_ejemplo, columna_ejemplo))


def sumar_matrices(matriz1, matriz2):
    return np.dot(matriz1, matriz2)

matriz1_ejemplo = np.array([[1, 2], 
                            [3, 4]])

matriz2_ejemplo = np.array([[5, 6], 
                            [7, 8]])

print(sumar_matrices(matriz1_ejemplo, matriz2_ejemplo))
