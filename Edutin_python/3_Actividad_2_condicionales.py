# nombre=input("Ingrese su nombre: ")
# valor_de_compra=int(input("Ingrese el valor de su compra: "))

# if valor_de_compra <80:
#     print(f" hola {nombre} el valor de tu compra es: ${valor_de_compra}")
# elif valor_de_compra >=80:
#     descuento=0.10
# elif valor_de_compra >= 150 and valor_de_compra <= 300:
#     descuento=0.15
# elif valor_de_compra >= 300 and valor_de_compra <= 500:
#     descuento=0.20
# else:
#     descuento=0.25

# precio_final=(valor_de_compra * descuento)-valor_de_compra
# print(f"Hola {nombre} el valor de tu compra sin descuento es: ${valor_de_compra} y tu compra con descuento es: ${precio_final}") 


nombre=input("Ingrese a su nombre: ")
edad=int(input("Ingrese su edad: "))
precio=int(input("Ingrse el monto de su comprá: USD$ "))
if precio<100:
    print(f" Hola {nombre} el monto de compra es: USD${precio}")
elif precio >= 100 and precio <= 200:
    descuento=0.10
elif precio >= 201 and precio <= 300:
    descuento=0.15
elif precio >= 301 and precio <= 400:
    descuento=0.20
else:
    descuento=0.25
valor_final=(precio*descuento)-precio
print(f"Hola {nombre}, tu edad es {edad}\nel precio de tu compra sin descuento es: USD$ {precio},\ny el precio de compra con descuento es: USD$ {valor_final}")
            
        


