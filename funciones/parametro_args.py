# # forma no optima de sumar valores
# def suma(lista):
#     numeros_sumados = 0
#     for numero in lista:
#         numeros_sumados += numero
#     return numeros_sumados

# resultado = suma([1,2,10,85])
# print(resultado)



# # utilizando el parametro args
# # con el signo "*" le decimos que el parametro es una lista
# def suma(*numeros):
#     return sum(numeros)

# resultado = suma(2,3,5,19,89)
# print(resultado)



# # forma optima de sumar valores
# def suma_total(numeros):
#     print(numeros)
#     # no podemos usar type porque son muchos argumentos, solo debe ser 1. es por eso que usamos el "*", para que se convierta en 1 solo dato. 
#     # aqui el *numeros es una lista
#     return sum([*numeros])

# resultado = suma_total([1,2,10,85])
# print(resultado)



# # lo mismo que arriba pero utilizando el operador args como parametro (*args)
# # si usamos este parametro tenemos que usarlo al final. si lo usamos despues no podemos pasarle mas parametros. es el unico parametro que podemos usar. Por ej, aqui los primeros valores son nombre y apellido y al final esta el parametro args:
# def suma(nombre, apellido, *numeros):
#     return f" Tu nombre nombre y apellido es {nombre} {apellido}. Y la suma de los numeros es: {sum(numeros)}."

# resultado = suma("Juan", "Perez", 2,3,5,19,89)
# print(resultado)