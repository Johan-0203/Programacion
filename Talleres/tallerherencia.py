# Punto 1
print ('Punto 1')
class Persona ():
    def __init__ (self, nombreEntrada, edadEntrada, idEntrada):
        self.nombre = nombreEntrada
        self.edad = edadEntrada
        self.id = idEntrada
    def hablar (self, mensaje):
        print (f'Hola, soy  {self.nombre} y te voy a decir...', mensaje)
    def caminar (self, pasos):
        for i in range (pasos):
            print (f'Hola, soy  {self.nombre} y he caminado {i+1} pasos')

persona1 = Persona ('Sergio', 26, 1000737329)
persona1.hablar ('tas bien?')
persona1.caminar (5)

# Punto 2
print ('Punto 2')
class Doctor (Persona):
    def __init__(self, nombreEntrada, edadEntrada, idEntrada, especialidadEntrada):
        Persona.__init__(self,nombreEntrada,edadEntrada,idEntrada)
        self.especialidad = especialidadEntrada
    def mostrarAtributos (self):
        print (f'Buenas tardes, soy el doctor y mi nombre es {self.nombre}, tengo {self.edad} años, me especialice en {self.especialidad} y mi identificacion es {self.id}')
    def enfermedadTratada (self, enfermedad):
        print (f'Por tal razon yo {self.nombre} procedo a tratar la {enfermedad}')

doctor1 = Doctor ('Pedro', 37, 627272812, 'Oftamologia')
doctor1.mostrarAtributos ()
doctor1.enfermedadTratada ('Miopia')

# Punto 3
print ('Punto 3')
class Nutricionista (Persona):
    def __init__(self, nombreEntrada, edadEntrada, idEntrada, universidadEgresado):
        Persona.__init__(self,nombreEntrada,edadEntrada,idEntrada)
        self.universidad = universidadEgresado
    def mostrarAtributos (self):
        print (f'Buenas tardes soy la nutricionista y mi nombre es {self.nombre}, tengo {self.edad} años, mi identificacion es {self.id} y soy egresado de la universidad {self.universidad}')
    def imcPaciente (self, peso, altura):
        return round (peso/(altura**2))

nutricionista1 = Nutricionista ('Daniela', 29, 3392982, 'UdeA')
nutricionista1.mostrarAtributos ()
print (nutricionista1.imcPaciente (70, 1.63))

# Punto 4
print ('Punto 4')
class Abogado (Persona):
    def __init__(self, nombreEntrada, edadEntrada, idEntrada, especialidadEntrada, universidadEgresado):
        Persona.__init__(self,nombreEntrada,edadEntrada,idEntrada)
        self.especialidad = especialidadEntrada
        self.universidad = universidadEgresado
    def mostrarAtributos (self):
        print (f'Buenas tardes soy el abogado {self.nombre}, tengo {self.edad} años, me identifico con el numero {self.id}, me especialice en {self.especialidad} y soy egresado de la universidad {self.universidad}')
    def casoRepresentado (self, nombre, caso):
        print (f'Y yo como el abogado {self.nombre} procedo a representar al cliente {nombre} en el caso de {caso}')

abogado1 = Abogado ('Alfonso', 60, 28291891, 'derecho laboral y seguridad social', 'CES')
abogado1.mostrarAtributos ()
abogado1.casoRepresentado ('Oliver Atom', 'invasion de pago de salud y pension a sus empleados')