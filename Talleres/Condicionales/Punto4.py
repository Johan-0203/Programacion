#constantes
bienvenida="Bienvenido, en este programa convertiremos de cm a m y km"
pregunta_distancia= "Ingrese una distancia en cm: "
mensaje_distancia="Las distancia es:"
pregunta_km="¿Quieres pasarla a km?: "
pregunta_m="¿Quieres pasarla a m?: "
despedida="Espero hayas disfrutado el programa"

#distancia
print(bienvenida)
distancia=float(input(pregunta_distancia))
resp_km=input(pregunta_km)
resp_m=input(pregunta_m)
isRespKm= resp_km=="si" or resp_km=="SI" or resp_km=="Si"
isRespm= resp_m=="si" or resp_km=="SI" or resp_km=="Si"

#condicionales
if(isRespKm and isRespm):
    distancia= distancia/100000
    print(mensaje_distancia, distancia, "km")
    distancia= distancia*1000
    print(mensaje_distancia, distancia, "m")
elif(isRespKm):
    distancia= distancia/100000
    print(mensaje_distancia, distancia, "km")
elif(isRespm):
    distancia= distancia/100
    print(mensaje_distancia, distancia, "m")
else:
    print(mensaje_distancia, distancia, "cm")

print(despedida)