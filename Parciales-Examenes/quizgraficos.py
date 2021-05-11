import matplotlib.pyplot as plt
import pandas as pd
#Punto 1
pregunta_snack='Diga un snack favorito suyo: '
pregunta_precio='Digite el precio de ese snack respectivamente: '
snacks = []
n=5
while (n>0):
    snack = input(pregunta_snack)
    snacks.append(snack)
    n=n-1

precios = []
n=5
while (n>0):
    precio = int(input(pregunta_precio))
    precios.append(precio)
    n=n-1
plt.bar(snacks, precios, width=0.7, color='r')
#-----------------------
plt.title('Snacks favoritos segun su precio en el mercado')
plt.xlabel('Nombre de Snacks')
plt.ylabel('Precio de los snacks en Pesos')
plt.savefig('graficoSnacks.png')
#-----------------------
plt.show()

#Punto 2
pregunta_ciudad='Diga una de sus ciudades favoritas: '
pregunta_poblacion='¿Cuanta poblacion en millones de habitantes tiene esa ciudad respectivamente?: '
ciudades = []
n=5
while (n>0):
    ciudad = input(pregunta_ciudad)
    ciudades.append(ciudad)
    n=n-1

sizes = []
n=5
while (n>0):
    poblacion= int(input(pregunta_poblacion))
    sizes.append(poblacion)
    n=n-1


def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento

    for i in range (len(labels)):
        ciudades[i] += indicador+str(round(sizes[i]/acumulador*100,2)) +'%'

etiquetarElementosPorcentuales(sizes, ciudades , '-')
plt.pie(sizes,labels=ciudades,shadow=1,counterclock=1)
#----------------------------
plt.title('Ciudades favoritas')
plt.savefig('tortaCiudadesFav.png')
#----------------------------
plt.show()

#Punto 3
print('''Un electrocardiograma (EKG, por sus siglas en inglés) le mide la actividad del corazón.
En una prueba de esfuerzo durante el ejercicio,
 tiene un ECG mientras camina o trota en una caminadora (treadmill)
''')
ecgData = pd.read_csv('ecg.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
muestras = list(ecgData['muestra'].values())
valores = list(ecgData['valor'].values())
plt.plot(muestras,valores)
#-----------------
plt.title('Grafico Sensor Vs Tiempo')
plt.xlabel('Tiempo(s)')
plt.ylabel('Voltaje(mV)')
plt.savefig('Sensor.png')
#-----------------
plt.show()


ppgData = pd.read_csv('ppg.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
muestras = list(ppgData['muestra'].values())
valores = list(ppgData['valor'].values())
plt.plot(muestras,valores)
#-----------------
plt.title('Grafico Sensor Vs Tiempo')
plt.xlabel('Tiempo(s)')
plt.ylabel('Voltaje(mV)')
plt.savefig('Sensor.png')
#-----------------
plt.show()