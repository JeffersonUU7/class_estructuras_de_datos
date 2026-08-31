import sys
print ("--------- Numero Enteros----------")
print (f"Tamaño de un entero: {sys.getsizeof(0)} bytes")

numero = 10**100
print(numero)


print ("-------- Numero decimales (float)---------")
print (f"Tamaño de un decimal: {sys.float_info.max}")
print (f"Tamaño de un decimal: {sys.float_info.min}")

print (1.125 ** 100)


print ("-------- Valor Booleano--------------")

print(True)
print(False)
print(type(False))

print (int(True))
print (int(False))


cadena = "HOla mundo"
print (cadena)
print ("Longitud de la palabra:" , len(cadena))

print ("Hola mi nombre es \"Jefferson\"")
print ("hola mi nombre es jefferson\nsoy ingeniero ")
print ("Nombre/\nNota 1\nNota 2\nNota 3")

