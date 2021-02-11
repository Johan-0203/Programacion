#Booleanos (datos verdadero o falso)
pruebaV = True
pruebaF = False
print(pruebaV)
print(pruebaF)
pruebaV=pruebaF
print(pruebaV)

edad = 18
estatura = 1.8
peso = 60
NOMBRE = "Johan Chacon"
#Calculando si es o no mayor de edad
print("-"*10, "Mayor de Edad", "-"*10)
isMayorEdad = (edad>=18)
print (isMayorEdad)
#Calculando si la estatura es mayor de la promedio
print("-"*8, "Mayor Estatura Promedio", "-"*8)
isMayorEstatura = (estatura>=1.7)
print(isMayorEstatura)
#Calculado si el peso es diferente a 60
print("-"*8, "Peso diferente 60", "-"*8)
isPesoDiferente = (peso!=60)
print(isPesoDiferente)
#Verificar un apellido en el nombre
print("-"*8, "Apellido en mi nombre", "-"*8)
apellido="Chacon"
isApellido= apellido in NOMBRE
print(isApellido)