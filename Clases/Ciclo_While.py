#Constantes
Bienvenida="Bienvenido al programa donde miraremos como funciona while"
pregunta_valorPC="¿Cuanto cuentas tu PC?: "
pregunta_ahorro="¿Cuanto tienes ahorrado?: "
mensaje_ahorro="Llevas ahorrado:"
mensaje_compra="Ya puedes comprar tu PC"
despedida="Hasta luego"

#Entradas
print(Bienvenida)
ValorPC=float(input(pregunta_valorPC))
Ahorrado=float(input(pregunta_ahorro))
while(ValorPC>Ahorrado):
    print(mensaje_ahorro, Ahorrado, "te falta", ValorPC-Ahorrado)
    Ahorrado = Ahorrado+1000

print(mensaje_compra)
print(despedida)