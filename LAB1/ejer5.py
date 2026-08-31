# Simulacion de sistema de registro para un estudiante universitario

# Registro de datos del alumno
alumno = "Jefferson Requeno"
edadd_estimada = 19
prom_acumulado = 8.7
tiene_beca = True

# Salida de informacion formateada
print("--- FICHA DEL ESTUDIANTE ---")
print(f"Nombre completo : {alumno}")
print(f"Edad            : {edadd_estimada} años")
print(f"Promedio        : {prom_acumulado}")
print(f"Estado de beca  : {tiene_beca}")

# Operaciones y calculos con las variables
años_para_graduar = 25 - edadd_estimada
puntos_faltantes = 10.0 - prom_acumulado

print("\n--- RESUMEN ACADÉMICO ---")
print(f"Edad proyectada al graduarse (25 años ref): le faltan {años_para_graduar} años")
print(f"Diferencia para el promedio perfecto (10.0): {puntos_faltantes:.2f} puntos")