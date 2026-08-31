#crear un diccionario 

estudiante = {
    "nombre": "Ana",
    "edad": 21,
    "cursos": ["Python", "Estrutura de datos"]
    
}

#Acceder a elementos
print(estudiante["nombre"])

#Acceder/modificar
estudiante["edad"] = 22
estudiante["carrera"] = "Ing. Software"

print(estudiante)

#Eliminar metodo del
del estudiante["edad"]
print(estudiante)

#eliminar metodo pop 
# persona.pop("ciudad")