# # creando un conjunto con set
# conjunto = set(["dato1", "dato2"])

# # agregando un conjunto dentro de otro conjunto con frozenset()
# conjunto1 = frozenset(["dato3", "dato4"])
# conjunto2 = {conjunto1, "dato5", "dato6"}

# # creando un conjunto con {}
# # conjunto = {"dato1", "dato2"}

# # creando un conjunto vacio
# # conjunto = set()

# # creando un conjunto con un solo dato
# # conjunto = {"dato1", }

# # print(conjunto2)



# # teoria de conjuntos
# conjunto1 = {1, 3, 7, 5, 9}
# conjunto2 = {1, 7, 9}
# conjunto3 = {2, 4, 8}

# # verificando si es un subconjunto
# resultado1 = conjunto1.issubset(conjunto2)
# # otra forma de verificar es con "<=" por ejemplo
# resultado_sub = conjunto2 <= conjunto1
# # print(resultado1)
# # print(resultado_sub)

# # verificando si es un superconjunto
# resultado2 = conjunto1.issuperset(conjunto2)
# # otra forma de verificar es con ">" por ejemplo
# resultado_super = conjunto2 > conjunto1
# # print(resultado_super)
# # print(resultado2)

# # verificar si hay algun numero en comun
# resultado3 = conjunto1.isdisjoint(conjunto3)
# # devuelve true si no hay ningun numero en comun
# resultado4 = conjunto1.isdisjoint(conjunto2)
# # devuelve false si hay algun numero en comun (aunque sea solo 1)
# print(resultado3)
# print(resultado4)