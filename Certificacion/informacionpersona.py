

informacion_persona = {}

continuar = True

while continuar:
    clave = input('Que dato quieres introducir')
    valor = input('Introduce el valor de ese dato')
    informacion_persona[clave] = valor

    print(informacion_persona)

    continuar = input('Quieres añadir mas informacion (Si/No)') == 'Si'
