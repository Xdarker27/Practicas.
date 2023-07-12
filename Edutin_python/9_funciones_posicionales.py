def lenguaje(nombre, **kwarg):
    print("Buscando informacíon sobre tus lenguajes favoritos.")
    print("Cargando información...")
    print("Tus lenguajes favoritos son: \n")
    
    contador=0
    for clave in kwarg:
        contador += 1
        print("hola ", nombre, "Tu", contador, "Lenguaje favorito es:", kwarg[clave])
lenguaje("jorge", lenguaje1="Python", lenguaje2="Ruby", lenguaje3="PHP")






