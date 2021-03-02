Bienvenido='Bienvenido al programa menu'
pregunta_menu='''Ingrese
    1- Mostrar numeros del 1 al 5
    2- Preguntar nombre
    3- Para mostrar año que estamos
    4- Salir
'''
pregunta_nombre='Cual es tu nombre?: '

entrada=1
while(entrada >=1 and entrada <=3):
    entrada=int(input(pregunta_menu))
    if(entrada==1):
        print(1,2,3,4,5)
    elif(entrada==2):
        nombre=input(pregunta_nombre)
        print('Bienvenido', nombre, 'a este menu, sigue usando las opciones')
    elif(entrada==3):
        print('Estamos en el año 2021')
    elif(entrada==4):
        print('Muchas gracias por usar el programa, feliz dia')
    else:
        entrada = 1
        print(pregunta_menu)