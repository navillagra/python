# # creando diccionarios con dict()
# # si queremos crear diccionarios vacios, debemos usar dict()
# diccionario = dict(nombre="nadia", apellido="villagra", edad=34)

# # creando diccionarios con {}
# # no podemos crear diccionarios vacios con {}
# # {
# #     "nombre": "nadia",
# #     "apellido": "villagra",
# #     "edad": 34
# # }



# # las listas no pueden ser claves y usamos frozenset() para introducir conjuntos
# diccionario = {frozenset([1, 2, 3]): "hola"}

# # fromkeys() es un metodo de clase, en este caso un metodo de diccionario entonces se crea dict.fromkeys(). Podemos crear diccionarios vacios con fromkeys().

# # creando diccionarios con fromkeys() valor por defecto None
# diccionario = dict.fromkeys(["nombre", "apellido", "edad"])

# # si lo ponemos sin [] nos crea un diccionario con las letras de la palabra. Eso sucede porque es un iterador. El primer dato es iterado y se convierte en clave y el segundo dato es el valor. Por ej:
# diccionario = dict.fromkeys("ABCDE", "NADIA")

# # creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
# diccionario = dict.fromkeys(["nombre", "apellido", "edad"], "no se")
# print(diccionario)
