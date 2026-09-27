# Variables de configuración del vehículo
limite_velocidad = 180
aumento_aceleracion = 10
fuerza_freno = 20
friccion = 2  # Velocidad que se pierde por inercia al soltar el pedal

def mostrar_tablero(velocidad, estado):
    # Función simple para imprimir el estado actual del carro
    print(f"--> Tablero Outlander | Velocidad: {velocidad} km/h | Estado: {estado}")

def iniciar_simulador():
    print("=== SIMULADOR DE CONDUCCIÓN ===")
    
    # Integramos tu idea inicial: pedir la velocidad al principio
    velocidad_actual = int(input("Ingrese la velocidad inicial de su Mitsubishi Outlander (en km/h): "))
    
    print("\nControles de la simulación:")
    print(" 'a' = Acelerar (+10 km/h)")
    print(" 'f' = Frenar (-20 km/h)")
    print(" 's' = Soltar pedal (Pierde 2 km/h por inercia)")
    print(" 'q' = Apagar motor y salir")

    # Bucle principal de la simulación
    while True:
        accion = input("\n¿Qué desea hacer? (a/f/s/q): ").strip().lower()

        # Evaluamos la acción del usuario con un if-elif tradicional
        if accion == "q":
            print("Apagando motor. Simulación terminada.")
            break  # Rompe el ciclo while y termina el programa
            
        elif accion == "a":
            velocidad_actual += aumento_aceleracion
            estado_carro = "Acelerando"
            
        elif accion == "f":
            velocidad_actual -= fuerza_freno
            estado_carro = "Frenando"
            
        elif accion == "s":
            velocidad_actual -= friccion
            estado_carro = "En marcha (sin pisar pedales)"
            
        else:
            print("Comando no reconocido. Intente con a, f, s o q.")
            continue  # Salta a la siguiente iteración del bucle sin ejecutar lo de abajo

        # Validaciones de los límites de velocidad (sustituye al max/min de la IA)
        if velocidad_actual > limite_velocidad:
            velocidad_actual = limite_velocidad
            estado_carro += " (¡LÍMITE ALCANZADO!)"
            
        elif velocidad_actual < 0:
            velocidad_actual = 0
            estado_carro = "Detenido por completo"

        # Llamamos a la función para mostrar la información en pantalla
        mostrar_tablero(velocidad_actual, estado_carro)

# Ejecutamos el programa llamando a la función principal
iniciar_simulador()
