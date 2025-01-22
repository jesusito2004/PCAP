
asignaturas = {'Matematicas':6, 'Fisica':4, 'Quimica':5}



cursocreditos = input('Que asignatura quiere saber los creditos: ')
total_creditos = 0
for asignatura, credito in asignaturas.items():
    print(f'{asignatura} tiene {credito} creditos')
    total_creditos += credito
    
print(f'El total de creditos es {total_creditos}')




    