listaNum = [18,19,20,17,24,27,36,21,18,22,55,1,11,13,200,3,9,10]

def datosLista(listaEntrada = 0):
    for elemento in listaEntrada:
        if (elemento%2==0):
            print(elemento)
    return None

datosLista(listaNum)