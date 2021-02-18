#constantes
bienvenida="Bienvenido, en este programa compararemos dos años"
pregunta_añoactual= "¿En que año estamos?: "
pregunta_añoazar= "Di otro año, no importa si ya paso o aun no: "
mensaje_añopasado= "Los años que han pasado desde ese año hasta este son: "
mensaje_añofuruto= "Los años que faltan para llegar hasta ese año son: "
mensaje_añosiguales= "Los años que ingresaste son los mismos, asi que no ha pasado ningun año"
despedida="Espero hayas disfrutado del programa"

#años
print(bienvenida)
año_actual= int(input(pregunta_añoactual))
año_azar= int(input(pregunta_añoazar))
dif_años= año_actual-año_azar
isAño_pasado= dif_años>0
isAño_futuro= dif_años<0
resultado=""

#condicional
if (isAño_pasado):
    resultado=mensaje_añopasado
elif (isAño_futuro):
    resultado=mensaje_añofuruto
    dif_años= dif_años*(-1)
else:
    resultado=mensaje_añosiguales

print(resultado, dif_años)
print(despedida)