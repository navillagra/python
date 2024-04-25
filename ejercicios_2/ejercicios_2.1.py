# # pedir nombre y edad de los compañeros que vinieron hoy a clases, para que el mayor sea el profe y el menor el asistente cuando el profe falta (?)

# def obtener_compañeros(cantidad_de_compañeros):
#     # creando lista con los compañeros
#     compañeros = []

#     # ejecutando un for para pedir info de los compañeros
#     for i in range(cantidad_de_compañeros):
#         nombre = input("Ingrese nombre: ")
#         edad = int(input("Ingrese edad: "))
#         compañero = (nombre, edad)

#         # agregando compañeros a la lista
#         compañeros.append([compañero])

#     # ordenandolos de menor a mayor segun la edad
#     compañeros.sort(key=lambda compañero:compañero[1])

#     # compañeros[x] devuelve una tupla con (nombre, edad) y despues accedemos al nombre para definir al asistente y al profesor
#     asistente = compañeros[0][0]
#     profesor = compañeros[-1][0]

#     # retornamos una tupla
#     return asistente, profesor

# # desempaquetamos lo que nos retorna la funcion
# asistente, profesor = obtener_compañeros(3)

# print(f"El asistente es {asistente} y el profesor es {profesor}")