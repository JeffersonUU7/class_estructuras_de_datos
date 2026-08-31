
# Guía: Sintaxis básica de Python, función print() y tipos de datos


# Ejercicio 1: Imprimir un texto que contiene comillas dobles

texto = "Este es un texto de ejemplo,\n" \
        "que ocupa varias líneas,\n" \
        "y puede contener \"comillas dobles\" sin problema."

print(texto)



# Ejercicio 2: Crear una matriz de ceros de 3x3

# Una "matriz" en Python se puede representar de dos formas:

# Forma A: con listas anidadas (sin librerías externas)
matriz_lista = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

print("Matriz 3x3 con listas:")
for fila in matriz_lista:
    print(fila)

# Forma B: usando la librería NumPy, muy usada para trabajar
# con matrices y operaciones numéricas.

import numpy as np

matriz_numpy = np.zeros((3, 3))

print("\nMatriz 3x3 con NumPy:")
print(matriz_numpy)



# Ejercicio 3: Imprimir los símbolos \ y /

# El símbolo / no necesita escape, se imprime directo.
# El símbolo \ SÍ necesita escape porque \ es el caracter usado
# para crear secuencias especiales (\n, \t, \", etc). Para
# imprimir una sola barra invertida literal, se escribe \\.

print("Barra diagonal (/):", "/")
print("Barra invertida (\\):", "\\")

# También se pueden imprimir juntos en una sola cadena:
print("Los dos símbolos son: \\ y /")

