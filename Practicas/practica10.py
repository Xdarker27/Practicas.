#Escribe un programa que pida al usuario que introduzca un número 
#y determine si es par o impar.
numero=int(input("Ingrese un numero: "))
resultado= numero / 2
if resultado %2 == 0:
    print(f" El numero {numero} es par")
else:
    print(f"El numero {numero} es impar ")

