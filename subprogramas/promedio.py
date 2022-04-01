
def obtener_promedio(p, lista):
    for i in range(len(lista)):
        p.append(lista[i][1])

    if sum(p)//len(lista) > 80:
        estado = True
    
    return p, lista