print("¡Bienvenido, hagamos unas operaciones!")
nombre=input("Nombre: ")

a=int(input("Ingresa el primera número: "))
b=int(input("Ingresa el segundo número: "))

operacion=int(input("¿Qué operación desea realizar?: 1.Suma 2.resta 3.multiplacicón 4.División 5.todas\n"))
if operacion == 1:
    print(f"Hola {nombre}, el resultado de tu suma es {a+b}")
elif operacion == 2:
    print(f"Hola {nombre}, el resultado de tu resta es {a-b}")
elif operacion == 3:
    print(f"Hola {nombre}, el resultado de tu multiplicación es {a*b}") 
elif operacion == 4:
    print(f"Hola {nombre}, el resultado de tu división es {a/b}")
elif operacion == 5:
    print(f"Hola {nombre}, el resultado de todas las operaciones son:\n {a+b} {a-b} {a*b} {a/b}")   