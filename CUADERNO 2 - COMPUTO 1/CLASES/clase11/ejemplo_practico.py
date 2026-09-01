#supongamos que estamos desarrollando un sistema para una empresa 
#tenemos un producto:

producto = {
    "codigo": "P001",
    "nombre": "Teclado mecanico",
    "precio": 45.99,
    "stock": 20,
    "disponible": True
    
}

#Podemos consultar el nombre del producto:
print(producto["nombre"])

#cambiar la disponibilidad del producto y el stock a 0

producto["stock"] = 0
producto["disponible"] = None
