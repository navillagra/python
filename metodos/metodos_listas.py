# lista = list(["hola", "nanu", 23]) # list() convierte una cadena en una lista. Por lo general, se usa para crear listas vacias (sin elementos).
# lista2 = list([23, 2023, 50, 1989])

# # resultado_len = len(lista) # len() devuelve la longitud de la lista. len es una funcion, no un metodo.

# # AGREGAR ELEMENTOS A UNA LISTA
# # resultado_append = lista.append("mundo") # append() agrega un elemento al final de la lista.
# # resultado_insert = lista.insert(1, "mundo") # insert() agrega un elemento en la posicion que le pasamos como primer parametro. El segundo parametro es el elemento que queremos agregar.
# # resultado_extend = lista.extend(["mundo", 532]) # extend() agrega varios elementos al final de la lista. El parametro es una lista de elementos (con corchetes). 

# # ELIMINAR ELEMENTOS DE UNA LISTA
# # resultado_pop = lista.pop(0) # pop() elimina el ultimo elemento de la lista. Si le pasamos un parametro, elimina el elemento que se encuentra en la posicion que le pasamos como parametro.
# # resultado_remove = lista.remove("nanu") # remove() elimina el elemento que le pasamos como parametro. Si el elemento no existe, nos lanza una excepcion.
# # resultado_clear = lista.clear() # clear() elimina todos los elementos de la lista.

# # print(lista)



# # ORDENAR ELEMENTOS DE UNA LISTA
# # resultado_sort = lista2.sort() # sort() ordena los elementos de la lista de menor a mayor. Si la lista contiene elementos de distinto tipo, nos lanza una excepcion.
# # resultado_reverse = lista2.reverse() # reverse() ordena los elementos de la lista de mayor a menor. 

# # print(lista2)

# elemento_encontrado = lista2.index(50) # index() devuelve la posicion del elemento que le pasamos como parametro. Si el elemento no existe, nos lanza una excepcion.
# # print(elemento_encontrado)

# #las tuplas y los conjuntos son inmutables, no se pueden modificar. Las listas si se pueden modificar.
# # print(dir(set(["asdasda","sdfasdasdasd"])))