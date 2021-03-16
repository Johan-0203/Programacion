#Constantes
temperatura_coporal=[36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
bienvenido='Bienvenido al quiz 2'
pregunta_opcion='''
    1. Conversor
    2. Informacion salud
    3. Informacion lista
    4. Salir
'''
pregunta_grados='''
    Elija la temperatura a la que desea convertir
    C- Celsius
    F- Fahrenheit
    K- Kelvin
'''
mensaje_C='La conversion no es necesaria'
mensaje_F='Mostrar en Fahrenheit'
mensaje_K='Mostrar en Kelvin'
mensaje_hipotermia='Hipotermia'
mensaje_fiebre='Fiebre'
mensaje_Normal='Normal'
mensaje_max='La temperatura mas alta es'
mensaje_min='La temperatura mas baja es'
mensaje_tomado='La temperatura se tomaba cada'
mensaje_error='Entrada no valida'
despedida='Hasta pronto'
#Programa

listaKelvin=[]
for elemento in temperatura_coporal:
    conversor = round(elemento + 273.15,2)
    listaKelvin.append(conversor)
listaFahrenheit=[]
for elemento in temperatura_coporal:
    conversor = round((elemento*1.8) + 32,2)
    listaFahrenheit.append(conversor)
opcion=int(input(pregunta_opcion))
while (opcion!=4):
    if(opcion==1):
        print('-----------Opcion 1 escogida------------')
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
        print('-'*40)
    elif(opcion==2):
        print('-----------Opcion 2 escogida------------')
        for posicion in temperatura_coporal:
            if (posicion<36):
                print(posicion, '->',mensaje_hipotermia)
            elif(posicion>=36 and posicion<=37.5):
                print(posicion, '->',mensaje_Normal)
            else:
                print(posicion, '->',mensaje_fiebre)
        print('-'*40)
    elif(opcion==3):
        print('-----------Opcion 3 escogida------------')
        print(mensaje_max,max(temperatura_coporal))
        print(mensaje_min,min(temperatura_coporal))
        print(mensaje_tomado, len(temperatura_coporal)/24*60, 'minutos')
        print('-'*40)
    else:
        print(mensaje_error)
    opcion=int(input(pregunta_opcion))

print(despedida)