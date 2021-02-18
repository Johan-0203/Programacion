#constantes
bienvenida = "Bienvenido"
mensaje_mayoredad = "Eres mayor de edad, puedes seguir"
mensaje_menoredad = "Eres menor de edad, no puedes seguir"
pregunta_edad="¿Cuantos años tienes?"
despedida="Espero que hayas disfrutado el programa"

#IMC
print(bienvenida)
edad = int(input(pregunta_edad))
isMayor = edad>=18
resultado=""
if (isMayor):
    resultado=mensaje_mayoredad
else:
    resultado=mensaje_mayoredad

print(resultado)


