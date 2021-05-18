isCorrectInfo=False
while(isCorrectInfo == False):
    try:
        edad = int(input('Ingrese su edad: '))
        isCorrectInfo=True
    except ValueError:
        print('Ingresaste un mensaje no valido')

nombreArchivo = input('Ingrese el archivo que desee encontrar: ')
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    print(f'El archivo {nombreArchivo} no se ha encontrado')

