import matplotlib.pyplot as plt

#Grafico de Barras
ingresos = [950,1000,800,750,875,900,925,930,890,850,780,690]
meses = ['Enero','Febrero','Marzo','Abril','Mayor','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
plt.bar(meses, ingresos, width=0.7, color='g')
#-----------------------
plt.title('Ingresos por mes de un empleado durante el 2020')
plt.xlabel('Meses del año')
plt.ylabel('Ingresos en miles de Pesos')
plt.savefig('graficoIngresos.png')
#-----------------------
plt.show()


#Grafico Torta
pieLabels =['Bogota','Medellin','Barranquilla','Cali','Bucaramanga']
sizes =[74.12,25.69,12.06,22.28,5.81]
explode = [0.1,0,0,0,0]
def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento

    for i in range (len(labels)):
        pieLabels[i] += indicador+str(round(sizes[i]/acumulador*100,2)) +'%'

etiquetarElementosPorcentuales(sizes, pieLabels , '-')
plt.pie(sizes,labels=pieLabels,explode=explode, shadow = 0.5, counterclock = 1)
#----------------------------
plt.title('Ciudades principales de Colombia')
plt.savefig('tortaCiudades.png')
#----------------------------
plt.show()
