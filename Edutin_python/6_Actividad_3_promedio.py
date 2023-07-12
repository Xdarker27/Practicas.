nombre=input("Nombre completo: ")
materia = 5
contador = 1
suma = 1
while contador <= materia:
    nombre_materia=input("Nombre de la " + str(contador) + " materia: ")
    calificacion=float(input("Calificación obtenida en " + str(nombre_materia) + ": "))
    suma=suma+calificacion
    contador = contador + 1
    promedio = suma/materia
print("Resultados")
print(f"Hola{nombre} tu promedio este semestre es de {promedio}.")
print("Hasta luego")
