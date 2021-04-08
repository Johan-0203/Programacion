listaNum=[18,19,20,17,24,27,36,21,18,22]

def datosLista (listaEntrada=[]):
    maximo=max(listaEntrada)
    minimo=min(listaEntrada)
    prom=sum(listaEntrada)/len(listaEntrada)

    print(maximo)
    print(minimo)
    print(prom)

datosLista(listaNum)