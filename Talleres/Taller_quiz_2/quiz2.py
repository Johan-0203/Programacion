#Mensajes
listaPesos= [20000,30000,4000,2500,1000,7600]
bienvenido='Bienvenido al quiz 2'
pregunta_opcion='''
    1. Conversor
    2. Agregar nuevo valor
    3. Informacion
    4. Eliminar valor
    5. Salir
'''
preguntaMoneda='''
    C- Mostrar lista original en pesos Colombianos
    D- Mostrar lista en Dolares
    E- Mostrar lista en Euros
'''
mensaje_pesos='Mostrar lista original'
mensaje_dolares='Mostrar lista Dolares'
mensaje_euros='Mostrar lista Euros'
mensaje_error='Entrada no valida'
preguntarNumero = 'Ingrese un valor en COP :'
mensajeMayor='El Mayor numero ingresado es'
mensajeMenor='El Menor numero ingresado es'
mensajeProm='El promedio es'
preguntaBorrarPos='Ingrese la posicion que desa borrar'
mensaje_despedida='Hasta luego'
#Conversos punto 1
listaEuros=[]
for elemento in listaPesos:
    conversor = round(elemento*0.00023,2)
    listaEuros.append(conversor)
listaDolares=[]
for elemento in listaPesos:
    conversor = round(elemento*0.00028,2)
    listaDolares.append(conversor)

opcion=int(input(pregunta_opcion))
while(opcion!=5):
    #------------Opcon 1--------
    if(opcion==1):
        opcionMoneda= input(preguntaMoneda)
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
    elif(opcion==2):
        valorIngresado = int(input(preguntarNumero))
        listaPesos.append(valorIngresado)
        print(listaPesos)
    elif(opcion==3):
        #----------Opcion 3----------
        print(mensajeMayor, max(listaPesos))
        print(mensajeMenor, min(listaPesos))
        print(mensajeProm, sum(listaPesos)/len(listaPesos))
    elif(opcion==4):
        #----------Opcion 4----------
        print(listaPesos)
        posicion=int(input(preguntaBorrarPos)) - 1
        listaPesos.pop(posicion)
        print(listaPesos)
    else:
        print(mensaje_error)
    opcion=int(input(pregunta_opcion))

print(mensaje_despedida)