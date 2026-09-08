#Ejercicio 1
def saludar():
    print("¡Hola! Estudiantes") 
    
saludar()

#Ejercicio 2
def suma(a,b):
    return a + b

resultado = suma(5,3)
print(resultado) #8


#Parametros
def saludar(nombre):
    print("Hola", nombre)

#Ahora solicitamos los nombres al usuario

nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")

#y enviamos esos datoa a la funcion
saludar(nombre1)
saludar(nombre2)