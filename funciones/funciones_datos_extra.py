# # los argumentos no pueden cambiar de posicion, ya q deben ir ordenados. estos parametros son posicionales
# def frase(nombre, apellido, adjetivo): 
#     return f"Tu nombre es {nombre} {apellido} y sos muy {adjetivo}."

# frase_resultante = frase("Nadia", "genia total", "Villagra")
# print(frase_resultante)





# # creando una funcion de 3 parametros
# # para forzar un argumento para no tener que ordenarlo por ejemplo, podemos hacer esto:
# def frase(nombre, apellido, adjetivo):
#     return f"Tu nombre es {nombre} {apellido} y sos {adjetivo}."
# # utilizando keyword arguments
# # estos parametros no son posicionales
# # para que esto funcione, todos los argumentos ser declarados como clave-valor (key words parameters)
# frase_resultante = frase(adjetivo = "genia total", nombre = "Nadia", apellido ="Villagra")
# print(frase_resultante)



# # funcion con un parametro opcional y un valor por defecto. en este caso el adjetivo esta forzado pero se puede redefineir
# def frase(nombre, apellido, adjetivo="tonta"):
#     return f"Tu nombre es {nombre} {apellido} y sos {adjetivo}."

# # el adjetivo se convierte en un parametro opcional, si queres colocarlo, lo colocas, sino no
# frase_resultante = frase("Nadia", "Villagra", adjetivo="genia total")
# print(frase_resultante)