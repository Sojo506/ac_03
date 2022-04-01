def lineaSup(largo):
    linea = "   ╔"
    for i in range(1, largo-1):
        linea += "═"
    linea += "╗"
    print(linea)


def lineaMed(largo):
    linea = "   ╠"
    for i in range(1, largo-1):
        linea += "═"
    linea += "╣"
    print(linea)


def lineaInf(largo):
    linea = "   ╚"
    for i in range(1, largo-1):
        linea += "═"
    linea += "╝" + "\n"
    print(linea)


def lineaBlanco(largo):
    linea = "   ║"
    for i in range(1, largo-1):
        linea += " "
    linea += "║"
    print(linea)


def lineaDato(d, largo):
    linea = ""
    linea += "   ║ "
    linea += d
    blancos = largo - len(d)
    for i in range(1, blancos-2):
        linea += " "
    linea += "║"
    print(linea)


def menuPrincipal():
    lineaSup(60)
    lineaBlanco(60)
    lineaDato("                 Condicionales y Listas", 60)
    lineaBlanco(60)
    lineaMed(60)
    lineaBlanco(60)
    lineaDato("01. Mostrar los elementos de la lista", 60)
    lineaDato("02. Agregar un elemento al final de la lista", 60)
    lineaDato("03. Agregar información del curso y profesor", 60)
    lineaDato("04. Mostrar los elementos y posición en la lista", 60)
    lineaDato("05. Calificar al estudiante", 60)
    lineaDato("06. Promedio del estudiante y su estado", 60)
    lineaDato("07. Salir", 60)
    lineaBlanco(60)
    lineaInf(60)
