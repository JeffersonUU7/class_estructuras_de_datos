# Ejercicio 2: Ubicación

# (Código, Nombre, (X, Y), Estado)[cite: 1]
dispositivo1 = ("PC001", "Servidor principal", (150, 300), "Activo")
dispositivo2 = ("RTR002", "Router principal", (45, 90), "Inactivo") 
dispositivo3 = ("SW003", "Switch", (120, 200), "Activo") 

# Mostrar los datos del primer dispositivo[cite: 1]
print("Código:", dispositivo1[0])
print("Nombre:", dispositivo1[1])
print("Coordenada X:", dispositivo1[2][0])  # Entra a la tupla de coords y saca X[cite: 1]
print("Coordenada Y:", dispositivo1[2][1])  # Saca Y[cite: 1]
print("Estado:", dispositivo1[3])
print()

# Guardar los 3 en una sola tupla[cite: 1]
dispositivos = (dispositivo1, dispositivo2, dispositivo3)

# Imprimir solo la coord Y del segundo dispositivo[cite: 1]
# [1] es el disp2, [2] son sus coords, [1] es la Y
print("Coordenada Y del segundo dispositivo:", dispositivos[1][2][1])