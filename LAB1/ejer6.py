# Gestion de lista de materias universitarias

# Crear lista inicial con 5 materias
materias = ["Programación", "Estructura de Datos", "Base de Datos", "Ingeniería de Software", "Redes"]

# a) Mostrar la lista completa
print(f"a) Lista inicial de materias: {materias}")

# b) Agregar 2 materias mas usando append()
materias.append("Servidores Web")
materias.append("Métodos Numéricos")
print(f"b) Lista tras agregar 2 materias: {materias}")

# c) Insertar una materia en la posicion 2 (indice 2)
materias.insert(2, "Sistemas Operativos")
print(f"c) Lista tras insertar en posicion 2: {materias}")

# d) Eliminar la ultima materia usando remove()
# Como pide remove() y no pop(), pasamos directamente el nombre de la ultima materia agregada
materias.remove("Métodos Numéricos")
print(f"d) Lista tras eliminar la última materia: {materias}")

# e) Mostrar el número total de materias
total_materias = len(materias)
print(f"e) El número total de materias es: {total_materias}")