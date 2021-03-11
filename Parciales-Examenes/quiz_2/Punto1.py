listaPesos= [20000,30000,4000,2500,1000,7600]
preguntaMoneda='''
    C- Mostrar lista original en pesos Colombianos
    D- Mostrar lista en Dolares
    E- Mostrar lista en Euros
'''
mensaje_pesos='Mostrar lista original'
mensaje_dolares='Mostrar lista Dolares'
mensaje_euros='Mostrar lista Euros'
mensaje_error='Entrada no valida'
listaEuros=[]
for elemento in listaPesos:
    conversor = round(elemento*0.00023,2)
    listaEuros.append(conversor)
listaDolares=[]
for elemento in listaPesos:
    conversor = round(elemento*0.00028,2)
    listaDolares.append(conversor)

opcionMoneda= input(preguntaMoneda)
if (opcionMoneda =='C'):
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