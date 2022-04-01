# importacion de subprogramas
from menu import menuPrincipal as menu
from subprogramas import elementos_lista
from subprogramas import posicion_elemento
from subprogramas import promedio
from subprogramas import info_prof_cur as d_info

# inicializamos el arreglo 
materias = [['Español', 0, ''], ['Matemáticas', 0, ''], 
['Economía', 0, ''], ['Programación', 0, ''], ['Inglés', 0, '']]

estado = ''

while True:
    print()
    menu()
    
    while True:
        try:
            opc = int(input("   Favor ingresar su opción: "))
            break
        except ValueError:
            print('Valor incorrecto u erróneo')
    print()

    if opc == 1:
        print(f'\t\t.:Elementos de la lista:.')
        # llamamos la funcion para mostrar los elementos de la lista
        elementos_lista.elementos(materias)

    elif opc == 2:
        # agregar materia
        materia = input('Agregar nueva materia: ')
        materias.append([materia, 0, ''])

    elif opc == 3:
        d_info.info(materias)

    elif opc == 4:
        # mostrar elementos y su posicion
        print('\t\t.:Posición y Elemento')
        posicion_elemento.posicion(materias)  

    elif opc == 5:
        # Agregamos la nota modificando el valor 0
        # bucle para obtener los datos requiridos y calificar l estuadiente
        for n in range(len(materias)):
            nota = float(input(f'Nota de {materias[n][0]}: '))
            materias[n][1] = nota
            
            # se verifica la nota para agregar si aprobo o reprobo
            if nota > 80:
                materias[n][2] = 'Aprobó'
            else:
                materias[n][2] = 'Reprobó'
        print()
            
    elif opc == 6:
        prom = []
        promedio.obtener_promedio(prom, materias)

        if sum(prom)//len(materias) > 80:
            estado = 'Aprobado'
        else:
            estado = 'Reprobado'

        if sum(prom) != 0:
            print(f'''\t\t.:Ponderado obtenido:.
Promedio: {sum(prom)//len(materias)}
Estado: {estado}    
    ''')
        else:
            print('No has realizado las suficientes calificaciones!')

    elif opc == 7:
        break
    else:
        print('Valor fuera de rango')
