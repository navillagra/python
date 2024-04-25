# # keys(): Devuelve una lista de elementos, los cuales serán las claves de nuestro diccionario. Tambien sirve para iterar.
# # get(<key>): Devuelve el valor que corresponde con la clave introducida.
# # clear(): Vacía el diccionario.
# # pop(<key>): Devuelve el valor que corresponde con la clave introducida, y luego borra la clave y el valor.
# # popitem(): Devuelve el último valor introducido, y luego lo borra.
# # items(): Devuelve una lista de tuplas, cada tupla se compone de dos elementos: el primero será la clave y el segundo, su valor.
# # del: Elimina el diccionario.


# diccionario = {
#     "nombre": "Nanu",
#     "apellido": "Villagra",
#     "edad": 22,
# }


# # Ejemplo de keys()
# # claves = diccionario.keys() # devuelve una lista de las claves del diccionario
# # claves = diccionario.get("nombre") # no lanza excepcion si no encuentra la clave y el programa continua
# # claves = diccionario.clear() # vacia el diccionario
# # claves = diccionario.pop("nombre") # devuelve el valor de la clave y luego la borra
# # claves = diccionario.popitem() # devuelve el ultimo valor introducido y luego lo borra
# # claves = diccionario.items() # devuelve una lista de tuplas, cada tupla se compone de dos elementos: el primero será la clave y el segundo, su valor.
# # del(diccionario["nombre"]) # elimina la clave y el valor del diccionario
# print(claves)