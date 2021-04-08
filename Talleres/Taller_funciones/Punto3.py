preguntaSaludo='Digite cuantas veces quiere ser saludado: '
mensajeSaludo='Hola, ¿Como estas?'

def saludar(veces = 0):
    while (veces>0):
        print(mensajeSaludo)
        veces = veces - 1
    return None

#Numero de veces ingresado por programador
saludar(8)

#Numero de veces ingresado por cliente
saludar(int(input(preguntaSaludo)))