ordenada = []
def recursiva(tabla):

    minimo = min(tabla)
    if len(tabla) == 1:
        ordenada.append(tabla[0])
        return ordenada
    else:
        ordenada.append(minimo)
        tabla.remove(minimo)
    return recursiva(tabla)

def ordenacion(tabla):
    ordenada = recursiva(tabla)
    return ordenada
