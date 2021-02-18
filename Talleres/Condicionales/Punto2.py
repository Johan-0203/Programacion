#constantes
bienvenida = "Bienvenido, en este programa miraremos tu edad"
mensaje_menoredad = "Eres menor de edad, aun estas pollito"
mensaje_joven = "Estas joven, aprovecha y empieza a hacer cosas"
mensaje_adulto = "Ya eres todo un adulto"
mensaje_adultomayor = "Los ñaos te alcanzaron, ya eres un adulto mayor"
pregunta_edad="¿Cuantos años tienes?: "
despedida="Espero que hayas disfrutado el programa"

#IMC
print(bienvenida)
edad = int(input(pregunta_edad))
isMenor = edad<18
isJoven = edad>=18 and edad<=25
isAdulto= edad>25 and edad<60
resultado=""
if (isMenor):
    resultado=mensaje_menoredad
elif(isJoven):
    resultado=mensaje_joven
elif(isAdulto):
    resultado=mensaje_adulto
else:
    resultado=mensaje_adultomayor

print(resultado)
print(despedida)