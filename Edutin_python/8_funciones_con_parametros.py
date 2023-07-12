""" numero=int(input("Ingresa un numero: "))
def es_par(numero):
    if numero % 2 == 0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")

es_par(numero)

numero=int(input("Ingresa un valor: "))
def multiplicacion(numero):
    print(f"la tabla del {numero} es:")
    for i in range(1,11):
         print(f"{numero} x {i} = {i*numero}")
multiplicacion(numero)"""


def resta(a=None, b=None):
    if a == None or b == None:  # noqa: E711
        print("Ingresa dos numeros para continuar con la operacion")
        return
    return a-b
resultado =resta(1,2)
print(resultado) 
