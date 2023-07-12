def conversor(moneda_actual, valor, moneda_a_convertir):
    if moneda_actual == 1:
        def dolarTo():


            if moneda_a_convertir == "1":
                print(f"{valor} dolares equivalentes a $ {valor * 3750} pesos colombianos")  
            elif moneda_a_convertir == "2":
                print(f"{valor} dolares equivalentes a $ {valor * 9.37} yuanes")    
            elif moneda_a_convertir == "3":
                print(f"{valor} dolares equivalentes a $ {valor * 0.76} libras esterlinas")
            else:
                print("No se reconoce la moneda a convertir")
        dolarTo()
    
    elif moneda_actual == 2:  
        

        def EuroTo():
            if moneda_a_convertir == "1":
                print(f"{valor} dolares equivalentes a $ {valor * 3750} pesos colombianos")  
            elif moneda_a_convertir == "2":
                print(f"{valor} dolares equivalentes a $ {valor * 9.37} yuanes")    
            elif moneda_a_convertir == "3":
                print(f"{valor} dolares equivalentes a $ {valor * 0.76} libras esterlinas")
            else:
                print("No se reconoce la moneda a convertir")
        EuroTo()

    else:
        print("no se reconoce la moneda a convertir")

moneda_actual=int(input("Ingrese su moneda actual:\n 1.Dollar 2.Euro "))
valor=float(input("Ingrese el valor a convertir: "))


moneda_a_convertir=input("¿A qué moneda quiere convertirlo? \n 1.Pesos colombianos,  2.Yuanes, 3.Libras Estrelinas")

conversor(moneda_actual, valor, moneda_a_convertir)
 
