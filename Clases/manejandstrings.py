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
nombre = 'maria alejandra'
nombres = nombre.split(' ')
nombre= ''
for elemento in nombres:
    nombre += elemento.capitalize() +' '
print(nombre)
print(saludo.center(50))
print(nombre.center(50))

enunciado = 'Hola hola ya me cansé de decir tantos Hola pero como vamos hola'
print (enunciado.upper().count('HOLA'))

print (enunciado.find('decir'))
print (enunciado[25:30])

txt = 'me gusta programar en java'
print (txt.replace('java', 'python'))

numeroId = '123124'
print(numeroId.isnumeric())

parrafo = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas debitis hic libero quos, aliquam nostrum officia! Unde, magnam ex? Vel aliquid ducimus aliquam error quod rem ut quos animi numquam.'

print (parrafo.endswith('.'))