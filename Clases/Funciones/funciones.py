#----------Sumar dos números -----------#
def sumar (a = 0, b = 0):
    '''
        devuelve la suma de dos numeros a y b
        por defecto a y b valen 0
    '''
    suma = a + b
    return suma
#----------Restar dos números -----------#
def restar (a = 0, b = 0):
    '''
        devuelve la resta de dos numeros a y b
        por defecto a y b valen 0
    '''
    resta = a - b
    return resta
#----------Multiplicar dos números -----------#
def multiplicar (a = 0, b = 0):
    multiplica = a * b
    return multiplica
#----------dividir dos números -----------#
def dividir (a = 0, b = 1):
    dividi = a / b
    return dividi

#-------potenciar dos numeros----------
def potenciar(base = 0, exponente=1):
    potencia=base**exponente
    return potencia

#-------funciones depenientes de otras-------
def calcular (operacion, numA, numB):
    print(operacion(numA,numB))