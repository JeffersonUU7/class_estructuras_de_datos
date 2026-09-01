#crear una lista de compras de frutas a comprar en el mercado por unidad que incluya: 2 manzanas, banana, uva, manzana

compras = ["manzana", "manzana", "banana", "uva", "manzana"] #Creacion de lista
print(compras[2]) #Imprime "banana"

#recibe un mensaje de agregue a la lista de la fruta pera y que solo traiga una manazana

compras.append("pera")
print(compras) #Imprime "manzana", "manzana", "banana", "uva", "manzana", "pera"


compras = list(dict.fromkeys(compras)) # deja solo una vez cada elemento
print(compras) #Imprime "manzana", "banana", "uva", "pera"