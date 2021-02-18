#constates
bienvenida = "Bienvenido, en este programa compararas dos numeros"
pregunta_numa = "Ingrese el numero A: "
pregunta_numb = "Ingrese el numero B: "
mensaje_mayor= "El numero A es mayor que el numero B"
mensaje_menor= "El numero B es mayor que el numero A"
mensaje_igual = "El numero A es igual al numero B"
despedida= "Espero que hayas disfrutado el programa"

#entrada de numeros
print(bienvenida)
numA= int(input(pregunta_numa))
numB= int(input(pregunta_numb))
isMayor= numA>numB
isMenor= numB>numA

#condicional
resultado= ""
if (isMayor):
    resultado = mensaje_mayor
elif (isMenor):
    resultado = mensaje_menor
else:
    resultado = mensaje_igual

print(resultado)