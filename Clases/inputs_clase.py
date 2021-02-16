#Constantes
pregunta_nombre = "¿Como te llamas?: "
mensaje_saludo = "Un gusto conocerte"
pregunta_edad = "¿Cuantos años tienes?: "
pregunta_estatura = "Y, ¿Cuanto mides?: "

#Uso de inputs
nombre = input(pregunta_nombre)
print (mensaje_saludo, nombre)

#Pasando input de strng a int
edad = int(input(pregunta_edad))

#Pasando input de strng a float
estatura= float(input(pregunta_estatura))

#operaciones con input
a= int(input("ingrese numero A: "))
b= int(input("ingrese numero B: "))
print (a+b)