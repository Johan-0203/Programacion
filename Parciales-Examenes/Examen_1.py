#Constantes
bienvenida="Bienvenido, en este programa valoraremos los trigliceridos y la homocisteina"
pregunta_trigli="Ingresa el valor de los trigliceridos: "
pregunta_homocis="Ingresa el valor de la homocisteina: "
mensaje_optimo="El valor es optimo"
mensaje_sobre_opti="El valor esta sobre el limite optimo"
mensaje_alto="El valor es alto"
mensaje_muyalto="El valor es muy alto"
despedida="Nos vemos pronto"

#Entrada de los valores
print(bienvenida)
trigliceridos=int(input(pregunta_trigli))
homocisteina=int(input(pregunta_homocis))

#Booleanos
isOptimoTrigli = trigliceridos<150
isSobreoptTrigli = trigliceridos>=150 and trigliceridos<=199
isAltoTrigli = trigliceridos>=200 and trigliceridos<=499
isMuyaltTrigli = trigliceridos>=500

isOptimoHosmo = homocisteina>=2 and homocisteina<15
isSobreoptHosmo = homocisteina>=15 and homocisteina<30
isAltoHosmo = homocisteina>=30 and homocisteina<100
isMuyaltHosmo = homocisteina>=100

#condicionales
resultado=""
if(isOptimoTrigli):
    resultado=mensaje_optimo
elif(isSobreoptTrigli):
    resultado=mensaje_sobre_opti
elif(isAltoTrigli):
    resultado=mensaje_alto
elif(isMuyaltTrigli):
    resultado=mensaje_muyalto
else:
    print("Valor no reconocido")

print(resultado, "para los Trigliceridos")

resultado=""
if(isOptimoHosmo):
    resultado=mensaje_optimo
elif(isSobreoptHosmo):
    resultado=mensaje_sobre_opti
elif(isAltoHosmo):
    resultado=mensaje_alto
elif(isMuyaltHosmo):
    resultado=mensaje_muyalto
else:
    print("Valor no reconocido")

print(resultado, "para la Homocisteina")
print(despedida)