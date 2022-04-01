def info(lista):
    for i in range(len(lista)):
        print(f'Materia: {lista[i][0]}')
        curso = input('Curso de la materia: ')
        profe = input('Nombre del profesor: ')
        print()

        lista[i].append(curso)
        lista[i].append(profe)
    
    return lista
