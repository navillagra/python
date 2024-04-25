# # promedio de duracion
# otros_cursos_min = 2.5
# otros_cursos_max = 7
# otros_cursos_promedio = 4
# dalto_curso = 1.5

# # duracion de crudos
# crudo_promedio = 5
# crudo_dalto = 3.5



# # mostrando diferencia de duracion (ejercicio a)
# diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
# # lo multiplicamos por 1000 para que no nos de un numero con coma y lo dividimos por 10 para que nos de el porcentaje con 1 decimal
# diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
# diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100
# # print(f"El curso de Dalto dura un {diferencia_con_min}% menos que el mas rapido de los demas cursos")
# # print(f"El curso de Dalto dura un {diferencia_con_max}% menos que el mas lento de los demas cursos")
# # print(f"El curso de Dalto dura un {diferencia_con_promedio}% menos que el promedio de los demas cursos")
# # 5



# # calculamos el porcentaje de tiempo vacio removido
# tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
# tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10


# # mostrando la cantidad de espacio vacio removido (ejercicio b)
# # print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio")
# # print(f"Este curso eliminó el {tiempo_vacio_dalto}% de tiempo vacio")



# # mostrando diferencias si los cursos duraran 10 horas (ejercicio c)
# print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otro curso')
# print(f'Ver 10 horas de otros curso equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de otro curso') 