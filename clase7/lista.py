# Crear una lista de estudiantes

estudiantes = ["Ana","Luis","Carlos", "Maria"] #Creacion de lista
print(estudiantes[0]) #Imprime "Ana"

#Agregar un nuevo estudiante a la lista
estudiantes.append("Pedro")
print(estudiantes[0:5]) #Imprime "Ana", "Luis", "Carlos", "Maria", "Pedro"

#eliminar un estudiante de la lista
estudiantes.remove("Luis")
print(estudiantes[0:4]) #Imprime "Ana", "Carlos", "Maria", "Pedro"

#mostrar la lista actualizada
print(estudiantes) #Imprime "Ana", "Carlos", "Maria", "Pedro"
