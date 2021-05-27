#---------Punto 1---------
import matplotlib.pyplot as plt
pregunta_alimentos='Ingrese uno de sus alimentos favoritos: '
pregunta_precio='Digite el precio de ese alimento respectivamente: '
alimentos = []
n=8
while (n>0):
    alimento = input(pregunta_alimentos)
    alimentos.append(alimento)
    n=n-1

precios = []
n=8
while (n>0):
    precio = int(input(pregunta_precio))
    precios.append(precio)
    n=n-1
plt.bar(alimentos, precios, width=0.7, color='r')
#-----------------------
plt.title('Alimentos favoritos segun su precio en el mercado')
plt.xlabel('Nombre de Alimentos')
plt.ylabel('Precio de los alimentos en Pesos')
plt.savefig('graficoAlimentos.png')
#-----------------------
plt.show()


#---------Punto 2-----------
class Humano():
    '''
        Esta es la clase Humano exige atributos
        nombreEntrada: Hace referencia al nombre del usuario
        edadEntrada: Hace referencia al edad del usuario
        sexoEntrada: Hace referencia al sexo del usuario
        Tiene las siguientes acciones:
        *hablar(mensaje):
            dado un mensaje lo muestra en pantalla
        
        *mostrarAtributos()
            muestra los atributos del usuario
    '''
    def __init__(self, nombreEntrada, edadEntrada,sexoEntrada):
        print('Hola soy un humano nuevo')
        self.edad = edadEntrada
        self.nombre = nombreEntrada
        self.sexo = sexoEntrada
    
    def hablar(self,mensaje):
        print(f'Hola soy {self.nombre} y tengo por decir que ', mensaje)
    
    def mostrarAtributos(self):
        print(f'''Mi nombre es {self.nombre}
                    Mi sexo es {self.sexo} 
                    Mi edad es {self.edad} años
        ''')


class Doctor(Humano):
    def calcularIMC(self, estatura, peso):
        print(f'Hola soy el Doctor {self.nombre} y voy a calcular tu IMC')
        IMC = peso/(estatura**2)
        print('Tu IMC es de ', round(IMC,2))



humano1 = Humano('Daniel' ,27, 'Hombre')
humano2 = Humano('Mafer' ,27, 'Mujer')

humano1.hablar('Espero que esten muy bien')
humano2.hablar('chao')

doctor1 = Doctor('Juan' , 35 , 'Hombre')
doctor1.calcularIMC(float(input("¿Cuanto mides?: ")),float(input("¿Cuanto pesas?: ")))


#-----------Punto 3------------
isCorrectInfo=False
while(isCorrectInfo == False):
    try:
        nombre = input('Ingresa tu nombre: ')
        dinero = int(input('Ingresa el dinero que tiene en dolares: '))
        assert(nombre.isalpha())
        isCorrectInfo=True
    except ValueError:
        print('Los datos ingresados son erronos')
    except AssertionError:
        print('Ingreso un dato no valido')

euros = dinero * 0.82
print(f'Tu nombre es {nombre} y tienes {euros} en euros')

#-----------Punto 4-------------
import sys
nombre_paciente = input('Ingrese el nombre del paciente: ')
descripcion_enfermedad =  input('Ingrese la descripcion de la enfermedad del paciente: ')
precio_consulta = int(input('Ingrese el precio de la consulta: '))

nombreArchivo = "pacientes.txt"
try:
    archivo = open(nombreArchivo)
except FileNotFoundError:
    archivo = open(nombreArchivo, 'w')
    descripcion= 'archivo de manejo de los clientes'
    archivo.writelines(descripcion)
    sys.exit(1)

archivo = open(nombreArchivo,'a')
linea = '\nnombre del paciente: ' + nombre_paciente + ', descripcion enfermedad: ' + descripcion_enfermedad + ', precio de consulta: ' + str(precio_consulta)
archivo.writelines(linea)
archivo.close()

#leer
with open(nombreArchivo,'r') as reader:
    for line in reader:
        print(line)