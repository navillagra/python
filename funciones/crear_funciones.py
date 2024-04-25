# # creando una funcion simple
# def saludar():
#     print('hola mundo')
# # ejecutando la funcion
# saludar()



# los parametros son "variables" que se definen y se usan dentro de una funcion.

# # crear una funcion que tenga parametros. puede tener mas de un parametro separado por coma ",".
# def saludar(nombre, sexo):
#     sexo = sexo.lower()
#     if(sexo == "mujer"):
#         adjetivo = "reina"
#     elif (sexo == "hombre"):
#         adjetivo = "rey"
#     else:
#         adjetivo = "amor"

#     print(f'hola {nombre}, mi {adjetivo} ¿como estas?')
# # ejecutando la funcion
# saludar('nanu', "mujer")



# # crear una funcion que nos retorne valores
# def crear_contraceña_random(num):
#     # creamos caracteres aleatorios para crear la contraseña
#     chars = "abcdefghij"
#     # convertimos en string el numero que nos pasan como parametro
#     num_entero = str(num)
#     # aqui convertimos en entero el numero que nos pase, devolviendo SOLO el primer numero
#     num = int(num_entero[0])
#     # de esta manera podemos usar el numero que nos pasan como parametro para crear la contraseña. por ej si nos pasan 5, la variable c1 (chars -2) seria igual a "d", c2 = "f" y c3 = "a"
#     c1 = num - 2
#     c2 = num
#     c3 = num - 5
#     # y por ultimo unimos las letras de la contraseña con el numero ingresado multiplicandolo por 2
#     contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
#     return contraseña, num
#     # (podemos retornar mas de un valor separandolos por coma ",")

# # desempaquetando la funcion
# password, numero_utilizado = crear_contraceña_random(398)
# # frase = f"tu contraseña nueva es: {password}"
# # print(frase)

# # mostrando los resultados obtenidos y los datos utilizados para obtenerlo
# print(f"tu contraseña nueva es: {password}")
# print(f"tu numero utilizado es: {numero_utilizado}")