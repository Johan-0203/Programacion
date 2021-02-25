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

#Entradas
num_ocul=6
print(bienvenido)
numero=int(input(pregunta_numero))
while(numero!=num_ocul):
    numero=int(input(mensaje_perder))

print(despedida)
