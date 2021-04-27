class Animal():
    '''
        Esta clase Animal exige atributos
        especieEntrada: Hace referencia a la especie del animal
        sexoEntrada: Hace referencia al sexo del animal
        nombreEntrada: Hace referencia al nombre que le dieron al animal
        edadEntrada: Hace referencia a si el usuario es "Adulto" o "Joven"
        Tiene las siguientes acciones:
        *hablar(mensaje):
            dado un mensaje lo mostrara en pantalla
        
        *mostrarAtributos()
            muestra los atributos
        
        *caminar(rango)
            dado un rango el usuario caminara hasta ese rango
    '''
    def __init__(self, nombreEntrada, especieEntrada, sexoEntrada, edadEntrada):
        print('Soy Dios, y he aqui un nuevo animal')
        self.nombre = nombreEntrada
        self.especie = especieEntrada
        self.sexo = sexoEntrada
        self.edad = edadEntrada
    
    def hablar(self, mensaje):
        print(f'{self.nombre}:', mensaje)
    
    def mostrarAtributos(self):
        print(f'''
                Hola de nuevo, soy Dios
                y te presentare a este animal para que lo conozcas
                Su nombre es {self.nombre}
                Es de la especie {self.especie}
                Ademas de que es {self.edad}
                Y por ultimo, es {self.sexo}
        ''')
    
    def caminar(self, distanciaMetros):
        for i in range (distanciaMetros):
            print(f'{self.nombre} ya ha recorrido {i+1} metros')


perro1 = Animal('Scott', 'Perro', 'Macho', 'Adulto')
gata1 = Animal('Dafne', 'Gata', 'Hembra', 'Joven')
perro2 = Animal('Lily', 'Perro', 'Hembra', 'Joven')
leon1 = Animal('Zeus', 'León', 'Macho', 'Adulto')
oso1 = Animal('Kenaje', 'Oso', 'Macho', 'Adulto')

perro1.hablar('*se echa en el piso* Zzzz,Zzzz,Zzzz')
gata1.hablar('miaaauuu, *ronronea* grrrrr')
perro2.hablar('guau guau guau ')
leon1.hablar('Rawr, Grrrr, Grgrgr')
oso1.hablar('Groar')

perro1.mostrarAtributos()
oso1.mostrarAtributos()

gata1.caminar(13)
leon1.caminar(20)
perro2.caminar(25)