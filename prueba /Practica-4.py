def resta(a=None, b=None):
    if a == None or b == None:  # Si uno o ambos argumentos no se proporcionan
        print("Ingresa dos numeros para continuar con la operacion")
        return  # Se imprime el mensaje de error y se devuelve None
    return a-b  # Si ambos argumentos se proporcionan, se devuelve la resta de a y b

resultado = resta(1, 2)  # Se llama a la función resta() con los argumentos 1 y 2
print(resultado)  # Se imprime el resultado, que es -1