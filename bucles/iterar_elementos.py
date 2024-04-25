# # creando lista para iterar. Con tuplas funciona igual.
# animales = ['perro', 'gato', 'loro', 'cocodrilo']
# numeros = [23, 5, 34, 1989]

# # animal es una variables creada solo para el bucle, y solo vive dentro del bucle. Si la llamamos fuera del bucle, nos dara error.
# # for animal in animales:
# #     print(animal)
    

# #  recorriendo la lista numeros y multiplicando por 2 cada numero
# # for numero in numeros:
# #     resultado = numero * 2
# #     print(resultado)



# # para irterar 2 listas, ambas deben tener la misma cantidad de elementos. 
# # for numero, animal in zip(numeros, animales):
# #     print(numero)
# #     print(animal)



# creando una lista con range. El primero numero es donde comienza, el segundo donde termina, y el tercero (si hubiera) es el salto (por ej. si colocamos 2, cuenta de 2 en 2. si colocamos 3, cuenta de 3 en 3 y asi...). Si solo ponemos 1 valor va del 0 al numero indicado. 
# for num in range(10, 20, 3):
#     print(num)

# #  recorriendo una lista por en indice con range y len. NO ES LA MANERA OPTIMA DE HACERLO. NO FUNCIONA EN CONJUNTOS.
# # for num in range(len(numeros)):
# #     print(numeros[num])

# #  la manera optima de recorrer una lista obteniendo su indice es con: enumerate.
# # for num in enumerate(numeros):
# #     indice = num[0]
# #     valor = num[1]
# #     print(f' el indice es: {indice} y el valor es: {valor}')

# # usando else
# for numero in numeros:
#     print(f'ejecutando el ultimo bucle, valor actual: {numero}')
# else:
#     print('no hay mas numeros en la lista')
# # else siempre se ejecuta al final del bucle, y solo si el bucle se ejecuto correctamente. Si el bucle se corta con un break, el else no se ejecuta.