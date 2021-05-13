texto = 'Hola Mundo'
lista = [1,43,25,63]
lista.sort()
lista.pop(2)
for i in lista:
    print(i)

for i in range(len(lista)):
    print(lista[i])

for letras in texto:
    print(letras)

print(texto[2])
palabras = texto.split(' ')
print(palabras)
print(type(palabras))
eliminarE = texto.split('e')
datos = 'nombre;apellido;edad'
print(datos.split(';'))
print(eliminarE)

uniendo = 'i'.join(eliminarE)
print(uniendo)
info= ' '.join(datos.split(';'))
print(info)

listaNombres=['Daniel','Juan','Maria','David','Vanessa','jesus']
print(max(listaNombres))
print(max(listaNombres,key=len))

respuesta = input('Ingrese si o no')
if respuesta.upper == 'SI':
    print('Hola, Bienvenido')
else:
    print('Chao')

nombre = input('Ingrese su nombre')
print(nombre.capitalize())

correo='ESPERO ESTES BIEN'
print(correo.casefold().capitalize())
saludo='Hola como estas?'
nombre='Maria Alejandra'
print(saludo.center(50))
print(saludo)