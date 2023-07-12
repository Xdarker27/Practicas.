print("Bienvenido a la calculadora de INDICE DE MASA CORPORAL")
contador = 1
while contador != 2:
    contador=int(input("¿Quieres seguir calculando tu indice?: 1(si) 2(no) "))
    if contador == 1:
        altura=float(input("Ingrese su estatura en metros: "))
        peso=float(input("Ingrese su peso en kilogramos: "))
        resultado=round(peso/(altura**2),2)
        
        if resultado <=18.5:
            print(f"Su IMC es {resultado},se encuentra bajo de peso")
        elif resultado <= 29.4:
            print(f"Su IMC es {resultado},se encuentra en un peso normal") 
        elif resultado <= 30.5:
            print(f"Su IMC es {resultado},se encuentra en sobre peso") 
        elif resultado > 40:
            print(f"Su IMC es {resultado},se encuentra estado de obesidad")  
    elif contador == 2:
        print("Hasta luego")
print("Gracias por usar nuestra calculadora de IMC")

    
