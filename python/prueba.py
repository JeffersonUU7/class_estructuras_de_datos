
#ESTO YO LO HICE INGE, PARA PRACTICAR MAS MI LOGICA DE PYTHON:)

primer_numero = float(input("Ingrese el primer número: "))
segundo_numero = float(input("Ingrese el segundo número: "))

print("\nSeleccione una operación")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Opción: ")

if opcion == "1":
    resultado = primer_numero + segundo_numero
    print("Resultado:", resultado)

elif opcion == "2":
    resultado = primer_numero - segundo_numero
    print("Resultado:", resultado)

elif opcion == "3":
    resultado = primer_numero * segundo_numero
    print("Resultado:", resultado)

elif opcion == "4":
    if segundo_numero != 0:
        resultado = primer_numero / segundo_numero
        print("Resultado:", resultado)
    else:
        print("No se puede dividir entre cero")

else:
    print("La opción ingresada no es válida")
    
    print
    