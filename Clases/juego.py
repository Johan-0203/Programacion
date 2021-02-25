#Mensajes
bienvenido='Bienvenido al juego con while'
pregunta_numero='''
        En este juego tienes que ingresar
        un numero que vaya del 1 al 10,
        la idea es que lo puedas intentar
        las veces que quieras...
        Ingresa tu numero: '''
mensaje_perder='No manches we, ya la regaste, ese numero no era, vuelve a poner otro: '
despedida='Felicidades, ganaste, hasta luego'
mensaje_sin_vidas='Ya no te quedan mas vidas'
#Entradas
num_ocul=6
life=3
print(bienvenido)
numero=int(input(pregunta_numero))
if(numero!=num_ocul):
    life=life-1
while(numero!=num_ocul and life>0):
    numero=int(input(mensaje_perder))
    life=life-1
if(life==0):
    print(mensaje_sin_vidas)
else:
    print(despedida)
