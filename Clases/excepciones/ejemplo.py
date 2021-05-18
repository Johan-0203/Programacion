isCorrectInfo=False
while(isCorrectInfo == False):
    try:
        edad = int(input('Ingrese su edad: '))
        isCorrectInfo=True
    except ValueError:
        print('Ingresaste un dato no valido')

nombreArchivo = input('Ingrese el archivo que desee encontrar: ')
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    print(f'El archivo {nombreArchivo} no se ha encontrado')
base = 4
divisor = 0
try:
    dividir = base / divisor
except ZeroDivisionError:
    print('El divisor ingresado es 0 por lo tanto es imposible dividir')

nombre = 'Daniel'
print(nombre.isalpha())
assert(nombre.isalpha())

isCorrectInfo=False
while(isCorrectInfo == False):
    try:
        nombre = input('Ingrese su nombre: ')
        assert(nombre.isalpha())
        isCorrectInfo=True
    except AssertionError:
        print('Ingresaste un dato no valido')

isCorrectInfo=False
while(isCorrectInfo == False):
    try:
        edad = int(input('Ingrese su edad: '))
        assert(edad >= 18)
        isCorrectInfo=True
    except AssertionError:
        print('Los menores de edad no peuden entrar')
    except ValueError:
        print('Edades son numeros enteros')

lista=[2,8,7,6]
try:
    lista[5]
except IndexError:
    print('Indice es mayor al tamaño de la lista')