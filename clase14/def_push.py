def push(pila, elemento): #Creando una funcion llamada push()
    pila.append(elemento)
    
    
def pop(pila): #Creamoa pop para retirar elementos
    return pila.pop()


#Creamos una pila vacia
pila = []
push(pila, "A")
push(pila, "B")
push(pila, "C")

print("Elementos de la pila: " , pila) #Mostramos la pila


elemento = pop(pila)
print("El ultimo elemento es: " , elemento)


