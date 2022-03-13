def compl_esp(tabla, num_segs):

    seg=len(tabla)//num_segs
    tabla[0:seg] = sorted(tabla[0:seg])
    tabla[seg:len(tabla)] = sorted(tabla[seg:len(tabla)])

    return tabla