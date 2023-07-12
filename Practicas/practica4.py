cadena = input("Introduce una cadena de texto: ")

# Eliminamos los espacios en blanco y convertimos todo a minúsculas
cadena = cadena.replace(" ", "").lower()

# Comparamos la cadena original con su versión invertida
if cadena == cadena[::-1]:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")
#destaco que no entiendo y yo no hice este codigo, lo dejo aqui para analizarlo y entenderlo.  # noqa: E501