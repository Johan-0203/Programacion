#Constantes
listaDolares = [20000,30000,4000,2500,1000,7600]
bienvenido='Hola, te doy la bienvenida al progama "Taller Recopilatorio"'
pregunta_opcion='''
    Elija la opcion que desea realizar
    1- Conversor
    2- Clasificacion de ingresos
    3- Informacion de los ingresos
    4- Salir
'''
preguntaMoneda='''
    C- Mostrar lista en pesos Colombianos
    D- Mostrar lista original en Dolares
    E- Mostrar lista en Euros
'''
mensaje_pesos='Mostrar lista en Pesos'
mensaje_dolares='Mostrar lista original'
mensaje_euros='Mostrar lista en Euros'
mensaje_menorIngreso='Ingresos bajos'
mensaje_mediosIngreso='Ingresos medios'
mensaje_altosIngreso='Ingresos altos'
mensaje_elevadosIngreso='Ingresos elevados'
mensaje_error='Entrada no valida'
mensaje_max='El ingreso mas alto es'
mensaje_min='El ingreso mas bajo es'
mensaje_prom='El promedio de ingresos es'
despedida='Hasta pronto'

listaPesos=[]
for elemento in listaDolares:
    conversor=round(elemento*3700,2)
    listaPesos.append(conversor)
listaEuros=[]
for elemento in listaDolares:
    conversor=round(elemento*0.84,2)
    listaEuros.append(conversor)
#programa
print(bienvenido)
opcion = int(input(pregunta_opcion))
while(opcion != 4):
    if(opcion==1):
        #opcion 1
        print('-----------Opcion 1 escogida------------')
        opcionMoneda=(input(preguntaMoneda))
        if(opcionMoneda =='C'):
            print(mensaje_pesos)
            print(listaPesos)
        elif(opcionMoneda=='D'):
            print(mensaje_dolares)
            print(listaDolares)
        elif(opcionMoneda=='E'):
            print(mensaje_euros)
            print(listaEuros)
        else:
            print(mensaje_error)
        print('-'*40)
    elif(opcion==2):
        #opcion 2
        print('-----------Opcion 2 escogida------------')
        for posicion in listaDolares:
            if (posicion<1000):
                print(posicion, '->',mensaje_menorIngreso)
            elif(posicion>=1000 and posicion<7000):
                print(posicion, '->',mensaje_mediosIngreso)
            elif(posicion>=700 and posicion<20000):
                print(posicion, '->',mensaje_altosIngreso)
            else:
                print(posicion, '->' , mensaje_elevadosIngreso)
        print('-'*40)
    elif(opcion==3):
        #opcion 3
        print('-----------Opcion 3 escogida------------')
        print(mensaje_max,max(listaDolares))
        print(mensaje_min,min(listaDolares))
        print(mensaje_prom,sum(listaDolares)/len(listaDolares))
        print('-'*40)
    else:
        print(mensaje_error)
    opcion = int(input(pregunta_opcion))

print(despedida)