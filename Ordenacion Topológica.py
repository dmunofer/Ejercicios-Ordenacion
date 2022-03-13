def ord_topo(tabla):

    ordenado = sorted(tabla.items(), key=lambda x: x[1])
    return dict(ordenado)

    #Esta funvión ordenara el diccionario de entrada en funcio de los valores (que los interpretariamos como las restricciones) y devuelve un nuevo diccionario ordenado