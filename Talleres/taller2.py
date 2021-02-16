#constantes
bienvenida = "Bienvenido, en este programa haremos operaciones con dos numeros que desees"
pregunta_numA = "Digita el primer numero que llamaremos A: "
pregunta_numB = "Digita el segundo numero que llamaremos B: "
mensaje_numeros= "Muy bien, asi que los numeros son: "
mensaje_nummayorA = "¿El numero A es mayor que el numero B?: "
mensaje_nummayorB = "¿El numero B es mayor que el numero A?: "
mensaje_numigual = "¿El numero A es igual que el numero B?: "
mensaje_suma = "La suma de A y B es: "
mensaje_resta = "La resta entre A y B es: "
mensaje_multiplicacion = "La multiplicacion entre A y B es: "
mensaje_division = "La division entre A y B es: "
mensaje_potencia = "La potencia entre A y B es: "
despedida = "Espero que hayas disfrutado del programa, hasta pronto"

#Entrada de mumeros
print(bienvenida)
numA = int(input(pregunta_numA))
numB = int(input(pregunta_numB))
print(mensaje_numeros, numA,"y", numB)

#Comparando los numeros
isMayorNumeroA = (numA>numB)
print(mensaje_nummayorA, isMayorNumeroA)

isMayorNumeroB = (numB>numA)
print(mensaje_nummayorB, isMayorNumeroB)

isIgualNumeros = (numA==numB)
print(mensaje_numigual, isIgualNumeros)

#operaciones
sumar= numA+numB
print(mensaje_suma, sumar)

restar= numA-numB
print(mensaje_resta, restar)

multiplicar= numA*numB
print(mensaje_multiplicacion, multiplicar)

dividir= numA/numB
print(mensaje_division, dividir)

potenciar= numA**numB
print(mensaje_potencia, potenciar)

print(despedida)