# # creamos una funcion que nos devuelva los numeros primos entre 0 y el numero que le pasemos

# # creamos una funcion para verificar si un numero es primo
# def es_primo(num):
#     # verificamos que el numero pasado no pueda dividirse por ningun numero entre 2 y ese mismo numero - 1
#     for i in range(2, num - 1):
#         # si es divisible por alguno retornamos False y termina el bucle
#         if num % i == 0:
#             return False
#     # si termina el bucle, significa que no es divisible por ninguno, por lo tanto es primo
#     return True

# # creamos una funcion que retorne una lista con todos los numeros primos
# def primos_hasta(num):
#     # creamos la lista
#     primos = []
#     for i in range(3, num + 1):
#         # verificamos si es primo
#         resultado = es_primo(i)
#         # en caso de que sea primo, lo agregamos a la lista
#         if resultado == True:
#             primos.append(i)
#     # retornamos la lista
#     return primos

# # creamos el resultado llamando a la funcion y lo mostramos
# resultado = primos_hasta(23)
# print(resultado)