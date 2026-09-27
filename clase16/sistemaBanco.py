# Sistema de un banco
# Banco los manguitos

Cola = []  # Cola vacía que será ocupada globalmente
numero_turno = 1  # Variable global para contabilizar los clientes


def registrar_cliente(nombre):
    global numero_turno

    # Generar el código del turno
    # T = letra que significa turno
    # :03d = mínimo 3 dígitos, rellena con ceros
    # Ejemplo: T001
    turno = f"T{numero_turno:03d}"
    cliente = [turno, nombre]
    Cola.append(cliente)
    numero_turno += 1

    # Imprimimos el resultado
    print("\nCliente registrado correctamente.")
    print("Turno asignado:", turno)
    print("Cliente:", nombre)


def ver_siguiente():
    if Cola:
        siguiente = Cola[0]
        print("\nPróximo cliente:")
        print("Turno del cliente:", siguiente[0])
        print("Cliente siguiente:", siguiente[1])
    else:
        print("No hay clientes en la cola.")

def atender_cliente():
    if Cola:
        cliente = Cola.pop(0)
        print('--- Llamamos al cliente ---')
        print("Turno: ", cliente[0])
        print("Cliente: ", cliente[1])
        
    else:
        print("\n No hay clientes que atender. =) ")
        
def mostrar_cola():
    if not Cola:
        print("No hay clientes esperando.")
        print("\nCantidad de clientes que esperan:", len(Cola))
        return

    for cliente in Cola:
        print(cliente[0], " - ", cliente[1])

    #Par saber cuantos clientes esperan
    print("\nCantidad de clientes que esperan:", len(Cola))

    #Para saeber quien es el ultimo cliente
    print("Ultimo turno:", Cola[-1][0])
    
    
def mostrar_menu():
    print("\n" + "=" * 30)
    print("Banco Los Manguitos")
    print("--- Menu de Turnos ---")
    print("1. Registrar clientes")
    print("2. Ver proximos clientes")
    print("3. Llamar al cliente")
    print("4. Mostrar todos los clientes")
    print("5. Salir")
    print("=" * 30)


if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion (Numero): ")

        if opcion == "1":
            nombre = input("Ingrese su nombre: ")
            registrar_cliente(nombre)

        elif opcion == "2":
            ver_siguiente()

        elif opcion == "3":
            atender_cliente()

        elif opcion == "4":
            mostrar_cola()

        elif opcion == "5":
            print("\nSistema finalizado")
            break

        else:
            print("\nLa opcion seleccionada no existe")