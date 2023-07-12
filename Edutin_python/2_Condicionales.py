"""year = int(input("¿Cuantos años tiene su computadora? "))
if year >= 0 and year <= 2:
    print("Tu computadora es nueva")
else:
    print("Tu computadora es vieja")"""

#Condicionales if y else

"""year=int(input("¿Cuantos años tienes? "))
if year >= 18:
    print("Eres mayor de edad ")
else:
    print("No eres mayor de edad ")"""


 #COndicionales elif

#edad=int(input("Ingrese su edad "))
#if edad < 16:
 #print("No tienes la edad para conducir ")
#elif edad < 18:
 #print("Puedes obtener un permiso para conducir ")
#elif edad < 70:
 #print("Puedes obtener una licencia estadar ")
#else: 
    # print("necesitas obtener una licencia especial ")
 

#Condicional if anidado

contraseña=input("Ingrese su contraseña: ")

if (len(contraseña)>= 8):
    print("Contraseña segura ")

    if(contraseña != "123456789"):
        print("Contraseña incorrecta ")
    else:
       print("Contraseña correcta ")
else:
    print("Tu contraseña es muy corta ")



          
       
