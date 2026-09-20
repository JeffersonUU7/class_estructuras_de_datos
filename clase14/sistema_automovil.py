#haz una sistema de aceleracion usando funciones donde cada vez presiones el acelerador aumente 10 km

def acelerar(velocidad_inicial):
    nueva_velocidad = velocidad_inicial + 10
    return nueva_velocidad


#Pedimos la velocidad inicial

velocidad = int(input("Ingrese la velocidad inicial del automovil (en km/h):"))

velocidad_inicial = acelerar(velocidad)

print("Despues de acelerar, tu velocidad es: " , velocidad_inicial , "km/h")
    

VELOCIDAD_MAXIMA = 180
ACELERACION = 10
FRENO = 20
RESISTENCIA = 2


def mostrar_estado(velocidad, acelerando, frenando):
    estado = "acelerando" if acelerando else "frenando" if frenando else "en marcha"
    print(f"Velocidad: {velocidad:.0f} km/h | Estado: {estado}")


def simular_carro():
    velocidad = 0
    print("Simulador de acelerador")
    print("Comandos: a = acelerar, f = frenar, s = soltar, q = salir")

    while True:
        comando = input("Accion: ").strip().lower()

        if comando == "q":
            print("Simulacion terminada.")
            break

        if comando not in {"a", "f", "s"}:
            print("Comando no valido.")
            continue

        acelerando = comando == "a"
        frenando = comando == "f"

        if acelerando:
            velocidad += ACELERACION
        elif frenando:
            velocidad -= FRENO
        else:
            velocidad -= RESISTENCIA

        velocidad = max(0, min(velocidad, VELOCIDAD_MAXIMA))
        mostrar_estado(velocidad, acelerando, frenando)


if __name__ == "__main__":
    simular_carro()


