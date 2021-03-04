import random
#Mensajes
bienvenida='Bienvenido al juego con while'
pregunta_numero='''
        En este juego tienes que ingresar
        un numero que vaya del 1 al 10,
        no existe vida 0...
        Ingresa tu numero: '''
pregunta_numero_2 = '''
        Vuelve a ingresar un numero
        del 1 al 10.
        Ya veremos si sigues con la misma suerte
        Ingresa tu numero: '''
pregunta_fallida='Ese no era, vuelve a poner otro: '
mensaje_ganar='Felicidades, ganaste'
mensaje_sin_vidas='Ya no te quedan mas vidas'
despedida='Nos vemos pronto'
pregunta_dificultad='''
        1- Facil
        2- Moderado
        3- Dificil
'''
mensaje_segundo_nivel = 'Entonces, has escogido el camino a la muertee, bienvenido al segundo nivel'
mensaje_caliente ='Caliente, bajale un poco'
mensaje_frio='Frio frio, como agua del rio'
#Entradas
dificultad=int(input(pregunta_dificultad))
vidas=None
while(dificultad != 1 and dificultad != 2 and dificultad != 3):
        print('ingresa una opcion valida')
        dificultad=int(input(pregunta_dificultad))

if(dificultad == 1):
        vidas = 10
        print('Dificultad facil seleccionada')
elif(dificultad == 2):
        vidas = 5
        print('Dificultad normal seleccionada')
else:
        vidas =2
        print('Modo admin activado')


num_oculto=random.randint(1,10)
num_oculto_2 = random.randint(1,10)
num_ingresado=int(input(pregunta_numero))
while(num_ingresado!=num_oculto and vidas>1):
        if(num_ingresado > num_oculto):
                print(mensaje_caliente)
        else:
                print(mensaje_frio)
        vidas=vidas-1
        print ('Te quedan', vidas, 'vidas')
        num_ingresado = int(input(pregunta_fallida))

if(num_ingresado == num_oculto and vidas >= 0):
        print('-'*30)
        print(mensaje_segundo_nivel)
        num_ingresado=int(input(pregunta_numero_2))
        while(num_ingresado!=num_oculto_2 and vidas>1):
                if(num_ingresado > num_oculto_2):
                        print(mensaje_caliente)
                else:
                        print(mensaje_frio)
                vidas=vidas-1
                print ('Te quedan', vidas, 'vidas')
                num_ingresado=int(input(pregunta_fallida))


if(vidas >= 0 and num_ingresado == num_oculto_2):
        print(mensaje_ganar)
else:
        print(mensaje_sin_vidas)
        print('El numero oculto 1 era', num_oculto, 'y el numero oculto 2 era', num_oculto_2)
print('-'*30)
