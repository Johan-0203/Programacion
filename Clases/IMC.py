#Constantes
bienvenida = "Bienvenido, en el siguiente programa calcularemos tu IMC"
pregunta_estatura = "¿Cuanto mides?: "
pregunta_peso = "¿Cuanto pesas?: "
resultado_imc = "Tu IMC es:"
mensaje_prueba = "¿Esta usted obeso?: "

#IMC
print(bienvenida)
peso = float(input(pregunta_peso))
estatura = float(input(pregunta_estatura))
IMC = peso/(estatura**2)
#Round es para redondear un numero decimal
print(resultado_imc, round(IMC,2))
ispeso = IMC>=30
print(mensaje_prueba, ispeso)