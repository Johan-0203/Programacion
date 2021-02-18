#constantes
bienvenida="Bienvenido, en este programa convertiremos de cm a km, m o mm"
pregunta_distancia= "Ingrese una distancia en cm: "
mensaje_distancia="Las distancia es:"
pregunta_unidad="¿A que unidad desea pasar la distancia? ¿km, m o mm?: "
despedida="Espero hayas disfrutado el programa"

#distancia
print(bienvenida)
distancia=float(input(pregunta_distancia))
resp_unidad=input(pregunta_unidad)

#condicionales
if(resp_unidad=="km"):
    distancia= distancia/100000
    print(mensaje_distancia, distancia, "km")
elif(resp_unidad=="m"):
    distancia= distancia/100
    print(mensaje_distancia, distancia, "m")
elif(resp_unidad=="mm"):
    distancia= distancia*10
    print(mensaje_distancia, distancia, "mm")
else:
    print("Caracter no valido")

print(despedida)