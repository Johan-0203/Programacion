# Grupo 6 - Integrantres: Johan Chacon y Sara Nieto

#------Primer Punto------
class ElementoDigital():
    def __init__(self, nombreEntrada, creadorEntrada,fechaEntrada):
        self.nombre = nombreEntrada
        self.creador = creadorEntrada
        self.fecha = fechaEntrada
    def mostrarAtributos(self):
        print(f'Mi nombre es {self.nombre}, mi creador se llama {self.creador} y sali el {self.fecha}')

class Usuario ():
    def __init__ (self, edadEntrada, nombreEntrada, sexoEntrada, nacionalidadEntrada):
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.sexo = sexoEntrada
        self.nacionalidad= nacionalidadEntrada
    def mostrarAtributos (self):
        print (f'''Mi nombre es {self.nombre}
        tengo {self.edad} años,
        soy un/a {self.sexo}
        con nacionalidad {self.nacionalidad}''')
    def escucharCancion(self, cancionEntrada):
        print (f" Hola, soy {self.nombre} y estoy escuchando {cancionEntrada}")


class Pagina():
    def __init__(self, tipocontenidoEntrada, formatoEntrada, fechaEntrada):
        self.tipocontenido = tipocontenidoEntrada
        self.formato = formatoEntrada
        self.fecha = fechaEntrada
    def mostrarAtributos(self):
        print(f'Soy una pagina con un contenido centrado en {self.tipocontenido}, mi formato es {self.formato} y sali el {self.fecha}')


#------Segundo Punto------
listaFav = ['My propeller', 'Handle Bars', 'Heartbreak', 'Lemonade', 'Buttercup']
print(listaFav)
pregunta_n = '¿Cual posicion de la lista de canciones desea eliminar?: '
class Cancion(ElementoDigital):
    def __init__(self, nombreEntrada, creadorEntrada,fechaEntrada, generoEntrada, duracionEntrada):
        ElementoDigital.__init__(self,nombreEntrada, creadorEntrada,fechaEntrada)
        self.genero = generoEntrada
        self.duracion = duracionEntrada
        print(f'Esta nueva cancion se llama {self.nombre} y salio el {self.fecha}')
    def reproducir(self, veces):
        for i in range (veces):
            print (f'{self.nombre} sonando {i+1} veces')

class Artista (Usuario):
    def __init__(self, generoEntrada, numerocancionesEntrada, albumsEntrada, edadEntrada, nombreEntrada, sexoEntrada, nacionalidadEntrada):
        Usuario.__init__(self, edadEntrada, nombreEntrada, sexoEntrada, nacionalidadEntrada )
        self.generomusical = generoEntrada
        self.numerocanciones = numerocancionesEntrada
        self.numeroDeAlbums = albumsEntrada
    def asistirConcierto(self, localidadEntrada):
        self.localidadconcert = localidadEntrada
        print (f" Hola, soy {self.nombre}, iré a un concierto en {self.localidadconcert} del genero {self.generomusical} que tiene un total de albums de {self.numeroDeAlbums} con {self.numerocanciones} canciones. ¡QUE EMOCIÓN!")



class Favoritos(Pagina):
    def __init__(self, tipocontenidoEntrada, formatoEntrada, fechaEntrada, fechaactEntrada):
        Pagina.__init__(self, tipocontenidoEntrada, formatoEntrada, fechaEntrada)
        self.comunidad = listaFav
        self.fechaactualizacion = fechaactEntrada
    def agregarcancion(self, cancion, fechaactualizacion):
        listaFav.append(cancion)
        print(f'La fecha de actualizacion ahora es {fechaactualizacion}')
    def eliminarcancion(self, n=int(input(pregunta_n))):
        print(listaFav)
        listaFav.pop(n-1)
        print(listaFav)

print('-'*80)
favorito1 = Favoritos('Entretenimiento', 'MP4', '03 de febrero de 2003', '20 de junio de 2019')
favorito1.agregarcancion('On our way', '22 de abril de 2021')
favorito1.agregarcancion('Montero', '23 de abril de 2021')
favorito1.eliminarcancion()
print('-'*80)
cancion1 = Cancion('Counting Stars', 'One Republic', '31 de mayo de 2013', 'pop',240)
cancion1.reproducir(4)
print('-'*80)
Fabio= Artista("Country", "30", "22", "67", "Fabio", "hombre", "Colombiano")
Fabio.asistirConcierto("Estados Unidos")
print('-'*80)
