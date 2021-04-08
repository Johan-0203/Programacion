listaNum=[18,19,20,17,24,27,36,21,18,22]

def datosLista (listaEntrada=[]):
    maximo=max(listaEntrada)
    minimo=min(listaEntrada)
    prom=sum(listaEntrada)/len(listaEntrada)

    print('El valor maximo es',maximo)
    print('El valor minimo es',minimo)
    print('El valor promedio es',prom)

datosLista(listaNum)