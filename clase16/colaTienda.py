colaTienda = [] #creamos una cola vacia porque esta iniciando a abrir la tienda

#Operaciones de la cola ENQUEUE (agregar elementos a la cola)
#Tienda Rosita

colaTienda.append('Cliente 1: Ana')
colaTienda.append('Cliente 2: Carlos')
colaTienda.append('Cliente 3: Luis')

print("Clientes de la Tienda Rosita:", colaTienda) 

#Operacion Peek

print("Primer cliente en la cola (Peek):", colaTienda[0]) #Mostramos el primer cliente de la cola sin eliminarlo

#Operacion SIZE

print("Cantidad de clientes en la cola (Size):", len(colaTienda)) #Mostramos la cantidad de clientes en la cola

#Operacion DEQUEUE (eliminar elementos de la cola)

print("Cliente atendido (DEQUEUE):", colaTienda.pop(0)) #Eliminamos y mostramos el primer cliente de la cola

#Mostrar los clientes que siguen

print("Clientes que siguen en la cola son:", colaTienda) #Mostramos los clientes que siguen en la cola

#Operacion rear
#consultar quien esta al final

print("Ultimo cliente en la cola (Rear):", colaTienda[-1]) #Mostramos el ultimo cliente de la cola sin eliminarlo

#usamos de nuevo pop para ver si funciona el if
print("Cliente atendido (DEQUEUE):", colaTienda.pop(1)) #Eliminamos y mostramos el primer cliente de la cola
print("Cliente atendido (DEQUEUE):", colaTienda.pop(0)) #Eliminamos y mostramos el primer cliente de la cola

#Operacion IS EMPTY
#Comprueba si todavia hay clientes en la cola

if not colaTienda:
    print("La cola esta vacia (Is Empty): True")
else:
    print("La cola esta vacia (Is Empty): False")