lista1 = [18,19,20,17,24,27,36,21,18,22]
lista2 = [36,37,38,35,36,38,37.5,38.2,41,37.4]
lista3 = [3,8,4,6,7,5,2,9,11,1]

def mostrasListas(listaEntrada1 = [], listaEntrada2 = [], listaEntrada3 = []):
    print('La primera lista lista es:')
    for elemento in listaEntrada1:
        print(elemento)
    print('La segunda lista lista es:')
    for elemento in listaEntrada2:
        print(elemento)
    print('La tercera lista lista es:')
    for elemento in listaEntrada3:
        print(elemento)
    return None

mostrasListas(lista1,lista2,lista3)