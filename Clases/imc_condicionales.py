#Constantes
bienvenida = "Bienvenido, en el siguiente programa calcularemos tu IMC"
pregunta_estatura = "¿Cuanto mides?: "
pregunta_peso = "¿Cuanto pesas?: "
mensaje_bajo_peso= "estas bajos de peso"
mensaje_normal= "estas en forma"
mensaje_sobre_peso= "ten cuidado, estas un poco en sobrepeso"
mensaje_obeso= "estas obeso, tu salud corre riesgo"
mensaje_IMC="Tu IMC es:"
despedida="Espero hayas disfrutado el programa"

#IMC
print(bienvenida)
peso = float(input(pregunta_peso))
estatura = float(input(pregunta_estatura))
IMC = peso/(estatura**2)
isBajoPeso = IMC < 18.5
isNormal = IMC>=18.5 and IMC<25
isSobrePeso = IMC>=25 and IMC<30
resultado=""
if(isBajoPeso):
    resultado=mensaje_bajo_peso
elif(isNormal):
    resultado=mensaje_normal
elif(isSobrePeso):
    resultado=mensaje_sobre_peso
else:
    resultado=mensaje_obeso

print(mensaje_IMC, round(IMC,2),",", resultado)
print(despedida)