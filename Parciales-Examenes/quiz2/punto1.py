temperatura_coporal=[36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
pregunta_grados='''
    Elija la temperatura a la que desea convertir
    C- Celsius
    F- Fahrenheit
    K- Kelvin
'''
mensaje_C='La conversion no es necesaria'
mensaje_F='Mostrar en Fahrenheit'
mensaje_K='Mostrar en Kelvin'
mensaje_error='Entrada no valida'

listaKelvin=[]
for elemento in temperatura_coporal:
    conversor = round(elemento + 273.15,2)
    listaKelvin.append(conversor)
listaFahrenheit=[]
for elemento in temperatura_coporal:
    conversor = round((elemento*1.8) + 32,2)
    listaFahrenheit.append(conversor)
opcion_grados=input(pregunta_grados)
if(opcion_grados=='C'):
    print(mensaje_C)
    print(temperatura_coporal)
elif(opcion_grados=='F'):
    print(mensaje_F)
    print(listaFahrenheit)
elif(opcion_grados=='K'):
    print(mensaje_K)
    print(listaKelvin)
else:
    print(mensaje_error)
