#---------Punto 1-----------
print('Punto 1'.center(40))
#Mensajes
bienvenida = "Bienvenido, en el siguiente programa calcularemos tu IMC"
pregunta_estatura = "¿Cuanto mides?: "
pregunta_peso = "¿Cuanto pesas?: "
resultado_imc = "Tu IMC es:"

#Pedir Nombre
print(bienvenida)
isCorrectInfo=False
while(isCorrectInfo == False):
    try:
        nombre = input('Ingrese su nombre: ')
        assert(nombre.isalpha())
        isCorrectInfo=True
    except AssertionError:
        print('Ingresaste un dato no valido')

#IMC
isCorrectInfo=False
while(isCorrectInfo == False):
    try:
        peso = float(input(pregunta_peso))
        estatura = float(input(pregunta_estatura))
        IMC = peso/(estatura**2)
        isCorrectInfo=True
    except ValueError:
        print('Ingresaste un dato no valido')
    except ZeroDivisionError:
        print('La estatura ingresada es 0 por lo tanto es imposible dividir')

print(resultado_imc, round(IMC,2))

#---------Punto 2-----------
print('Punto 2'.center(40))
pregunta_parrafo='Ingrese un parrafo: '

isCorrectInfo=False
while(isCorrectInfo==False):
    parrafo = input(pregunta_parrafo)
    isCorrectInfo = parrafo.endswith('.')
    if (isCorrectInfo == False):
        print('El parrafo no termina en punto')

#---------Punto 3-----------
print('Punto 3'.center(40))

import sys
nombre_equipo = input('Ingrese el nombre del equipo medico: ')
descripcion_equipo =  input('Ingrese la descripcion: ')
precio_mantenimiento = int(input('Ingrese el precio del mantenimiento: '))

nombreArchivo = "mantenimiento.txt"
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    archivo = open(nombreArchivo, 'w')
    descripcion= 'archivo de manejo de los clientes'
    archivo.writelines(descripcion)
    sys.exit(1)

archivo = open(nombreArchivo,'a')
linea = '\nnombre del equipo: ' + nombre_equipo + ', descripcion: ' + str(descripcion_equipo) + ', precio del mantenimiento: ' + str(precio_mantenimiento)
archivo.writelines(linea)
archivo.close()

#leer
with open(nombreArchivo,'r') as reader:
    for line in reader:
        print(line)