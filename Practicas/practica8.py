numero = int(input("Introduce un número: "))
es_primo = True
for i in range(2, numero):
    if numero % i == 0:
        es_primo = False
        break
if es_primo:
    print("El número es primo.")
else:
    print("El número no es primo.")
    