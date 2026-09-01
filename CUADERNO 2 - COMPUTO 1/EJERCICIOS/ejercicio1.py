# Ejercicio 1: Sistema de configuración

# Tupla con los datos[cite: 1]
configuracion = ("Sistema Académico", "1.0.0", "localhost", 8080, "producción")

print("===== CONFIGURACIÓN DEL SISTEMA =====")

# A. Imprimir versión, servidor y puerto (índices 1, 2 y 3)[cite: 1]
print(f"Versión: {configuracion[1]}")
print(f"Servidor: {configuracion[2]}")
print(f"Puerto: {configuracion[3]}")

# B. Ver cuántos elementos tiene[cite: 1]
print(f"\nElementos en la tupla: {len(configuracion)}")