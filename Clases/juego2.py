import random
#Mensajes
bienvenida='Bienvenido al juego con while'
pregunta_numero='''
        En este juego tienes que ingresar
        un numero que vaya del 1 al 10,
        la idea es que lo puedas intentar
        con 3 vidas, no existe vida 0...
        Ingresa tu numero: '''
pregunta_fallida='No manches we, ya la regaste, ese numero no era, vuelve a poner otro: '
mensaje_ganar='Felicidades, ganaste'
mensaje_sin_vidas='Ya no te quedan mas vidas'
despedida='Nos vemos pronto'
pregunta_dificultad='''
        1- Facil
        2- Moderado
        3- Dificil
'''
#Entradas
dificultad=int(input(pregunta_dificultad))
vidas=None
while(dificultad != 1 and dificultad != 2 and dificultad != 3):
        print('ingresa una opcion valida')
        dificultad=int(input(pregunta_dificultad))

if(dificultad == 1):
        vidas = 5
        print('Dificultad facil seleccionada')
elif(dificultad == 2):
        vidas = 3
        print('Dificultad normal seleccionada')
else:
        vidas =1
        print('Modo admin activado')


num_oculto=random.randint(1,10)
num_ingresado=int(input(pregunta_numero))
while(num_ingresado!=num_oculto and vidas>1):
    vidas=vidas-1
    print ('Te quedan', vidas, 'vidas')
    num_ingresado = int(input(pregunta_fallida))

if(vidas >= 0 and num_ingresado == num_oculto):
        print(mensaje_ganar)
else:
        print(mensaje_sin_vidas)
        print('El numero oculto era', num_oculto)
