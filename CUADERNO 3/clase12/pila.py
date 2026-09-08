pila = []

pila.append("iniciar Sesión") # append() para agregar elemento 
# print(pila)

pila.append("Consultar el perfil")
pila.append("Ver amigos en comun")
pila.append("Hola k ase?")

print("pila actual:")
print(pila)

#Desapilar un elemnto
accion = pila.pop()

print("\n Accion retirada: ")
print(accion)

print("\n Penultima Accion retirada: ")
print(pila)