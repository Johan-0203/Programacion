import sys
nombre = input('Ingrese su nombre: ')
edad = int( input('Ingrese su edad: '))
estatura = float(input('Ingrese su estatura: '))

nombreArchivo = "estudiantes.txt"
try:
    archivo = open(nombreArchivo)
    print('1')
except FileNotFoundError:
    archivo = open(nombreArchivo, 'w')
    descripcion= 'archivo de nombre datos estudiantes'
    print('2')
    archivo.writelines(descripcion)
    sys.exit(1)

archivo = open(nombreArchivo,'a')
linea = '\nnombre: ' + nombre + ', edad: ' +str(edad) + ', estatura: ' + str(estatura)
archivo.writelines(linea)
archivo.close()

#leer
with open(nombreArchivo,'r') as reader:
    for line in reader:
        print(line)

import pandas as pd
diccionario = {}
diccionario["nombre"] = "Daniel"
diccionario["edad"] = 27
diccionario["estatura"] = 1.67
serie = pd.Series(diccionario)
print(serie)
serie.to_csv("datos.csv", sep=";")