numeros = input("Introduce una lista de números separados por comas: ")

# Convertimos la cadena de entrada en una lista de números
numeros = [int(n) for n in numeros.split(",")]

# Calculamos el número más grande y el número más pequeño
maximo = max(numeros)
minimo = min(numeros)

# Mostramos el resultado en la consola
print("El número más grande es:", maximo)
print("El número más pequeño es:", minimo)
#destaco que no entiendo y yo no hice este codigo, lo dejo aqui para analizarlo y entenderlo.  # noqa: E501