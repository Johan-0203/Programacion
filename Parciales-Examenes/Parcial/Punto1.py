#Mensajes
preguntaNumero1='Ingrese el primer numero: '
preguntaNumero2='Ingrese el segundo numero: '
preguntaNumero3='Ingrese el tercer numero: '

numa = int(input(preguntaNumero1))
numb = int(input(preguntaNumero2))
numc = int(input(preguntaNumero3))
#-------sumar tres numeros----------
def sumar (a = 0, b = 0, c = 0):
    suma = a + b + c
    return suma
#-------restar tres numeros----------
def restar (a = 0, b = 0, c = 0):
    resta = a - b - c
    return resta
#-------multiplicar tres numeros----------
def multiplicar (a = 0, b = 0, c = 0):
    multiplica = a * b * c
    return multiplica
#-------dividir tres numeros----------
def dividir (a = 0, b = 1 , c = 1):
    dividi = a / b / c
    return dividi

#-------potenciar tres numeros----------
def potenciar(base = 0, exponente1 = 0, exponente2 = 1):
    potencia=base**(exponente1**exponente2)
    return potencia

print(sumar(numa, numb, numc))
print(restar(numa, numb, numc))
print(multiplicar(numa, numb, numc))
print(dividir(numa, numb, numc))
print(potenciar(numa, numb, numc))