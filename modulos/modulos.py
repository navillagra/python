# import modulo_saludar
# saludo = modulo_saludar.saludar("Nadia")
# print(saludo)
# print(type(modulo_saludar))



# # con as podemos renombrar un modulo por ej:
# import modulo_saludar as md_sld
# saludo = md_sld.saludar("Nadia")
# print(saludo)
# # para ver las propiedades y los metodos de el namespace de un modulo, usamos dir
# # print(dir(md_sld)) # con dir podemos ver las funciones que tiene el modulo
# print(md_sld.__name__) # con __name__ podemos ver el nombre del modulo



# # con from podemos importar una funcion especifica de un modulo
# # si queres importar mas de una funcion, separalas con comas
# # con as tambien podemos renombrar funciones
# from modulo_saludar import saludar as saludar_normal,saludar_raro

# saludo = saludar_normal("Nadia")
# saludo_raro = saludar_raro("Nanux")
# print(saludo)
# print(saludo_raro)




# # para importar todo un modulo, usamos * (pero es una mala practica, ya que hace que el codigo sea mas dificil de leer, mas pesado y puede generar conflictos de nombres)
# from modulo_saludar import *
# saludo = saludar("Nadia")
# saludo_raro = saludar_raro("Nanux")
# print(saludo)
# print(saludo_raro)