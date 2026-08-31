# Declaracion de variables de diferentes tipos de datous
edad_alumno = 20
promedio_ciclo = 8.5
nombre_estudiante = "Josue"
estudiante_activo = True

# Muestra del valor y tipo de dato con type()
print(f"Variable: edad = {edad_alumno}, Tipo: {type(edad_alumno)}")
print(f"Variable: promedio = {promedio_ciclo}, Tipo: {type(promedio_ciclo)}")
print(f"Variable: nombre = \"{nombre_estudiante}\", Tipo: {type(nombre_estudiante)}")
print(f"Variable: activo = {estudiante_activo}, Tipo: {type(estudiante_activo)}")

# Operaciones compatibles entre variabless
saludo_completo = "Estudiante: " + nombre_estudiante
puntos_extra = promedio_ciclo + 0.5

print("\n--- Operaciones de ejemplo ---")
print(saludo_completo)
print(f"Promedio final con puntos extra: {puntos_extra}")