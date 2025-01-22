def read_int(prompt, min, max):

    while True:
        try:
            valor = int(input(prompt))
            if  min <= valor <= max:
                return valor
            else:
             raise ValueError
        except ValueError:
            print("Error: Debes ingresar un valor entre", min, "y", max)
        
v = read_int("Ingresa un numero entre -10 a 10: ", -10, 10)

print("El numero es:", v)